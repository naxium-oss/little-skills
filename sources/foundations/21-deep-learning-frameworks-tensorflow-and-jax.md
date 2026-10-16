# Deep Learning Frameworks (TensorFlow & JAX)

## Framework Version and Hardware Backend Grounding
TensorFlow and JAX behavior, performance, and even numerical results can shift across versions and hardware backends (CPU, CUDA GPU, TPU); verify the exact framework version, backend, and accelerator visibility before debugging performance or correctness issues.
```python
import tensorflow as tf
print(tf.__version__, tf.config.list_physical_devices())

import jax
print(jax.__version__, jax.devices(), jax.default_backend())
```
Confirm CUDA/cuDNN version compatibility against the framework's official support matrix for the installed version, since a mismatch silently falls back to CPU or crashes with an unhelpful error.
**Pitfalls:** assuming GPU is in use because code "runs" without checking `tf.config.list_physical_devices('GPU')`/`jax.devices()` actually lists an accelerator; mixing TensorFlow versions with incompatible Keras versions installed separately.

## TensorFlow's tf.function and Graph Tracing
`tf.function` compiles Python functions into graphs for performance, but Python control flow and side effects (print statements, list appends) behave differently during tracing versus eager execution, verify actual traced behavior since a function can silently retrace on every call if inputs have varying shapes/types (a major hidden performance bug).
```python
@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape:
        loss = loss_fn(model(x), y)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    return loss
```
Check retracing counts by adding `print` statements (which only execute during tracing, not on cached graph calls) or use `tf.function(experimental_relax_shapes=True)` and confirm with profiling that retracing isn't happening every step.
**Pitfalls:** passing Python scalars/lists with varying values as arguments to a `tf.function`, triggering a full retrace on every distinct value instead of reusing a compiled graph; relying on Python `print()` for runtime debugging inside a traced function, which only fires during tracing, not every execution.

## JAX Functional Transformations: jit, grad, vmap
JAX requires pure functions (no in-place mutation, no hidden state) to safely apply its core transformations: `jit` for XLA compilation, `grad` for automatic differentiation, `vmap` for automatic vectorization, and arrays are immutable, so updates use functional indexing (`.at[idx].set(value)`) instead of assignment.
```python
import jax.numpy as jnp
from jax import jit, grad, vmap

def loss(params, x, y):
    pred = params["w"] * x + params["b"]
    return jnp.mean((pred - y) ** 2)

grad_loss = jit(grad(loss))
batched_predict = vmap(lambda w, x: w * x, in_axes=(0, None))
```
Verify a function is actually pure and side-effect-free before wrapping in `jit`, since JAX traces it once with abstract values and caches the compiled result, impure functions produce misleading results on subsequent calls with different concrete inputs.
**Pitfalls:** attempting in-place array mutation (`arr[0] = 1`) instead of `arr.at[0].set(1)`, hitting an immutability error; wrapping a function with Python-level side effects (logging counters, random without an explicit PRNG key) in `jit` and getting inconsistent behavior across calls.

## Mixed Precision and Numerical Stability
Mixed precision training (float16/bfloat16 compute with float32 master weights) speeds up training and reduces memory on supporting hardware, but can introduce numerical instability (overflow, underflow) without careful loss scaling; verify actual speedup and stability empirically on the target hardware rather than assuming uniform benefit across all model architectures.
```python
policy = tf.keras.mixed_precision.Policy("mixed_float16")
tf.keras.mixed_precision.set_global_policy(policy)
# JAX equivalent: cast compute arrays to bfloat16 explicitly, keep optimizer state in float32
```
Monitor for `NaN`/`Inf` losses when introducing mixed precision, and verify whether the specific hardware (older GPUs without Tensor Cores, or CPU-only) actually benefits at all before adopting it broadly.
**Pitfalls:** enabling mixed precision on hardware without Tensor Core support, gaining no speedup while adding complexity; skipping loss scaling with float16, causing gradient underflow that silently stalls training with no error message.

# Natural Language Processing Fundamentals

## Tokenization Algorithms and Vocabulary Grounding
Different tokenization schemes (whitespace, WordPiece, BPE, SentencePiece, byte-level BPE) produce different token counts, sequence lengths, and out-of-vocabulary behavior for the same text; verify the exact tokenizer and vocabulary/merges file version tied to a specific model checkpoint, since mismatched tokenizers silently produce garbage input.
```python
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("bert-base-uncased")
print(tok.tokenize("unbelievably"))     # ['un', '##believ', '##ably'], verify actual subword split
print(tok("hello world", return_tensors="pt"))
```
Confirm the tokenizer version pinned matches the exact model checkpoint's expected preprocessing (special tokens, casing, truncation strategy) rather than assuming any "BERT tokenizer" is interchangeable across checkpoints.
**Pitfalls:** using a different model's tokenizer against a target model's weights, producing token IDs that map to entirely wrong embeddings; ignoring subword splitting when counting "words," leading to inaccurate length/cost estimates.

## Text Preprocessing and Normalization Tradeoffs
Preprocessing decisions (lowercasing, stemming, lemmatization, stopword removal, Unicode normalization) can help or hurt depending on the downstream task and model type, modern transformer-based pipelines typically need far less manual preprocessing than classic bag-of-words pipelines. Verify a preprocessing step actually improves the target metric via an ablation rather than applying it as unquestioned convention.
```python
import unicodedata

def normalize(text: str) -> str:
    return unicodedata.normalize("NFKC", text).strip()
```
Confirm lowercasing/stemming isn't destroying information a transformer-based model would otherwise use effectively (case can carry meaning, e.g., named entities), by comparing metrics with and without the step.
**Pitfalls:** applying classic NLP preprocessing (aggressive stemming, stopword removal) unmodified to a modern transformer pipeline, discarding signal the model would otherwise use; skipping Unicode normalization, causing visually identical strings to compare as unequal or tokenize inconsistently.

## Embeddings and Semantic Similarity
Word/sentence embeddings map text into vector space where geometric distance approximates semantic similarity; verify which embedding model and distance metric (cosine vs. Euclidean) is actually appropriate, since embeddings from different model families/versions are not comparable in the same space.
```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(["a cat sat on the mat", "a dog lay on the rug"])
cos_sim = np.dot(embeddings[0], embeddings[1]) / (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))
```
Confirm embeddings used for retrieval/search are all generated by the exact same model version, mixing embeddings from different model checkpoints in one vector index silently produces meaningless similarity scores.
**Pitfalls:** comparing embeddings generated by two different model versions/checkpoints as if they share a common space; using raw Euclidean distance on non-normalized embeddings when the model was trained/evaluated using cosine similarity.

## Evaluation Metrics for NLP Tasks
Classification metrics (accuracy, F1) suit categorical tasks, but generation tasks need different metrics (BLEU/ROUGE for reference-based overlap, perplexity for language modeling, or human/LLM-judge evaluation for open-ended quality), verify a chosen metric actually correlates with the quality dimension being optimized, since surface-overlap metrics can reward fluent-but-wrong outputs.
```python
from rouge_score import rouge_scorer
scorer = rouge_scorer.RougeScorer(["rouge1", "rougeL"], use_stemmer=True)
scores = scorer.score("the cat sat on the mat", "a cat was sitting on the mat")
```
Cross-check automated metric results against a small human-reviewed sample before trusting them as the sole signal for model comparison, since known metric weaknesses (BLEU penalizing valid paraphrases) can mislead automated leaderboards.
**Pitfalls:** relying solely on BLEU/ROUGE for open-ended generation quality, missing valid paraphrases or coherence issues these metrics don't capture; comparing perplexity scores across models using different tokenizers, which are not directly comparable.

# Deep Learning Frameworks (TensorFlow & JAX)

## Keras Model APIs: Sequential, Functional, and Subclassing
Keras (bundled with TensorFlow, also usable multi-backend in Keras 3) offers three model-building approaches with different flexibility tradeoffs: Sequential for simple linear stacks, the Functional API for models with branching/multiple inputs-outputs, and subclassing `tf.keras.Model` for full custom control over the forward pass; verify the chosen API actually supports the architecture's structure (Sequential cannot express skip connections) before committing to it.
```python
inputs = tf.keras.Input(shape=(224, 224, 3))
x = tf.keras.layers.Conv2D(32, 3, activation="relu")(inputs)
skip = x
x = tf.keras.layers.Conv2D(32, 3, activation="relu", padding="same")(x)
x = tf.keras.layers.Add()([x, skip])   # requires Functional API; Sequential can't express this
outputs = tf.keras.layers.GlobalAveragePooling2D()(x)
model = tf.keras.Model(inputs, outputs)
```
Verify Keras 3's multi-backend behavior (TensorFlow, JAX, or PyTorch backend) if used, since some layer behaviors and serialization formats can differ subtly by backend, confirm the actual `keras.backend.backend()` in use rather than assuming TensorFlow by default.
**Pitfalls:** attempting to express a branching/residual architecture in the Sequential API, hitting a hard structural limitation; assuming Keras 3 code behaves identically regardless of backend without verifying the specific backend-dependent operations actually used.

## Custom Training Loops and GradientTape
While `model.fit()` covers common training patterns, custom training loops using `tf.GradientTape` (TensorFlow) provide full control needed for non-standard losses, multiple optimizers, or research-style architecture experiments; verify gradients are actually flowing to all intended trainable variables by inspecting `tape.gradient()` output for `None` values, which silently indicates a broken computational graph connection.
```python
with tf.GradientTape() as tape:
    predictions = model(x_batch, training=True)
    loss = loss_fn(y_batch, predictions)
grads = tape.gradient(loss, model.trainable_variables)
for var, grad in zip(model.trainable_variables, grads):
    if grad is None:
        print(f"WARNING: no gradient for {var.name}")   # indicates a disconnected graph path
optimizer.apply_gradients(zip(grads, model.trainable_variables))
```
Verify `training=True`/`training=False` is passed correctly to layers with different train/inference behavior (BatchNorm, Dropout), since a custom loop must set this explicitly, unlike `model.fit()` which handles it automatically.
**Pitfalls:** forgetting to pass `training=True` during custom-loop training, causing BatchNorm/Dropout layers to behave as if in inference mode and silently degrading training quality; not checking for `None` gradients, missing a completely disconnected branch of the model that never receives updates.

## Model Checkpointing and Reproducible Training Resumption
Long training runs must checkpoint model weights, optimizer state, and training step/epoch count so an interrupted run can resume exactly rather than restarting or silently losing optimizer momentum/schedule state; verify a resumed run's loss curve continues smoothly from the checkpoint (not with a sudden spike) as evidence that optimizer state was actually restored correctly, not just model weights.
```python
checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer, step=tf.Variable(0))
manager = tf.train.CheckpointManager(checkpoint, "./ckpts", max_to_keep=3)
checkpoint.restore(manager.latest_checkpoint)
```
Verify random seed and data pipeline shuffling state are also considered when exact reproducibility (not just "reasonable resumption") is required, since model+optimizer checkpointing alone doesn't guarantee bit-identical continuation without also controlling data order.
**Pitfalls:** checkpointing only model weights and not optimizer state, causing a resumed run's adaptive optimizer (Adam, etc.) to restart its momentum/variance estimates from scratch and destabilize training; assuming a restored checkpoint guarantees full reproducibility without also fixing the data pipeline's shuffle seed and iteration position.

## Distributed Training Strategies
TensorFlow's `tf.distribute.Strategy` (MirroredStrategy for single-machine multi-GPU, MultiWorkerMirroredStrategy/TPUStrategy for larger scale) and JAX's `pmap`/`jit` with sharding abstract away multi-device training, but verify the actual achieved scaling efficiency empirically (near-linear speedup rarely holds perfectly due to communication overhead) rather than assuming a strategy wrapper automatically yields proportional speedup with added devices.
```python
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
    model = build_model()
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")
model.fit(dataset, epochs=10)
```
Verify batch size scaling assumptions (global batch size = per-replica batch size × number of replicas) and corresponding learning-rate adjustments are actually applied, since naively keeping a small per-replica batch size wastes available parallelism, while keeping the original single-device learning rate at a much larger global batch size can destabilize training.
**Pitfalls:** assuming multi-GPU training scales linearly without measuring actual wall-clock speedup, missing that communication overhead can dominate for small models or slow interconnects; forgetting to scale the learning rate (or use a warmup) when increasing global batch size for distributed training, causing convergence instability.

# Natural Language Processing Fundamentals

## Named Entity Recognition and Sequence Labeling
NER assigns labels (person, organization, location) to spans of text, typically framed as token-level sequence labeling (BIO/BIOES tagging schemes); verify the exact tagging scheme and label set a pretrained model was trained on before feeding its output into downstream logic, since a mismatched scheme interpretation (treating BIOES `I-` tags as `B-` tags) silently corrupts span boundaries.
```python
from transformers import pipeline

ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
results = ner("Marie Curie worked at the Sorbonne in Paris.")
for entity in results:
    print(entity["entity_group"], entity["word"], entity["score"])
```
Verify entity boundary aggregation (`aggregation_strategy`) actually merges sub-word tokens into complete entity spans correctly for the specific tokenizer, since a wrong aggregation strategy can split or merge entities incorrectly for multi-token names.
**Pitfalls:** assuming all NER models share the same label taxonomy (PERSON vs. PER, ORGANIZATION vs. ORG) without checking the specific model's label list; not aggregating sub-word tokens correctly, producing fragmented partial-entity outputs instead of complete spans.

## Prompt Engineering and In-Context Learning
Large language model behavior is highly sensitive to prompt phrasing, few-shot example selection/order, and formatting details (whitespace, delimiter choice); verify a prompt's effectiveness empirically across multiple test cases and paraphrased variants rather than trusting a single anecdotal success, since LLM outputs can be brittle to superficial prompt changes that shouldn't matter semantically.
```python
prompt = """Classify the sentiment as positive, negative, or neutral.

Text: "The film exceeded every expectation I had."
Sentiment: positive

Text: "{user_text}"
Sentiment:"""
```
Verify few-shot example order doesn't introduce recency bias (models can overweight the last example) by testing with reordered example sets, and confirm the exact model version/checkpoint used, since prompt-sensitivity characteristics change materially between model versions.
**Pitfalls:** drawing conclusions about "the right way to prompt" from a handful of anecdotal tests instead of a systematic evaluation set covering edge cases; assuming a prompt engineered for one model version transfers unchanged in effectiveness to a different model or a new version of the same model family.

## Retrieval-Augmented Generation Pipeline Design
RAG combines a retrieval step (vector search over a document corpus) with a generation step (an LLM conditioned on retrieved context) to ground responses in specific data and reduce hallucination; verify retrieval quality independently of generation quality (measure retrieval precision/recall against a labeled query set) since a RAG system can fail either because retrieval finds the wrong documents or because generation ignores good retrieved context.
```python
query_embedding = embed_model.encode(query)
results = vector_db.search(query_embedding, top_k=5)
context = "\n\n".join(r.text for r in results)
prompt = f"Answer using only the following context:\n{context}\n\nQuestion: {query}"
response = llm.generate(prompt)
```
Verify chunk size and overlap settings for the document corpus actually preserve enough context per chunk for coherent retrieval by testing with representative real queries, since overly small chunks lose context while overly large ones dilute embedding relevance.
**Pitfalls:** evaluating only end-to-end answer quality without isolating whether retrieval or generation is the actual failure point, making it hard to know what to fix; chunking documents by a fixed token count without regard to semantic boundaries (mid-sentence splits), degrading both retrieval relevance and generated answer coherence.

## Bias, Toxicity, and Safety Evaluation in NLP Systems
Language models can reproduce and amplify biases present in training data, and safety behavior (refusing harmful requests, avoiding toxic outputs) varies significantly by model version and even by prompt phrasing; verify actual model behavior with a structured, documented test set covering known bias/safety dimensions rather than relying on informal spot-checks or assuming a vendor's safety claims transfer unchanged to a fine-tuned or quantized variant of the model.
```python
test_prompts = load_bias_eval_set("stereotype_pairs.jsonl")
for pair in test_prompts:
    resp_a = model.generate(pair["prompt_a"])
    resp_b = model.generate(pair["prompt_b"])
    compare_sentiment_and_associations(resp_a, resp_b)
```
Verify safety behavior is re-tested after any fine-tuning, quantization, or system-prompt change, since these can measurably shift refusal rates and bias characteristics away from the base model's evaluated behavior.
**Pitfalls:** assuming a base model's published safety/bias evaluation results still apply unchanged after fine-tuning or quantizing it for deployment; relying on informal manual spot-checks instead of a structured, repeatable evaluation set, making regressions hard to detect systematically over time.
