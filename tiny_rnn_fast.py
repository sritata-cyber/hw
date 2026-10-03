import os

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")

import numpy as np
import tensorflow as tf

np.random.seed(7)
tf.random.set_seed(7)

# A small corpus of short English sentences.
tiny_lines = [
    "I like cats.",
    "I like dogs.",
    "I like noodles.",
    "I like tacos.",
    "I like books.",
    "I like robots.",
    "I like music.",
    "I like pizza.",
    "I like puzzles.",
    "I like coding.",
]
text = "\n".join(tiny_lines)

# Map each English character to an integer for the model.
chars = sorted(set(text))
stoi = {char: index for index, char in enumerate(chars)}
itos = {index: char for char, index in stoi.items()}
vocab_size = len(chars)

# Turn the corpus into short input sequences and their next characters.
seq_len = 16
X = []
y = []
for start in range(len(text) - seq_len):
    X.append([stoi[char] for char in text[start : start + seq_len]])
    y.append(stoi[text[start + seq_len]])

X = np.asarray(X, dtype=np.int32)
y = np.asarray(y, dtype=np.int32)

# Train a compact character-level recurrent neural network.
model = tf.keras.Sequential(
    [
        tf.keras.layers.Embedding(vocab_size, 12),
        tf.keras.layers.SimpleRNN(32),
        tf.keras.layers.Dense(vocab_size),
    ]
)
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
)
history = model.fit(X, y, batch_size=32, epochs=35, verbose=0)
print(f"Trained on {len(X)} character sequences; final loss: {history.history['loss'][-1]:.3f}")


def generate(seed="I like ", n_chars=80, temperature=0.7):
    padded_seed = (" " * seq_len + seed)[-seq_len:]
    context = [stoi.get(char, stoi[" "]) for char in padded_seed]
    output = []

    for _ in range(n_chars):
        inputs = np.asarray([context], dtype=np.int32)
        logits = model(inputs, training=False)[0].numpy()

        if temperature <= 0:
            next_index = int(np.argmax(logits))
        else:
            probabilities = tf.nn.softmax(logits / temperature).numpy()
            next_index = int(np.random.choice(vocab_size, p=probabilities))

        output.append(itos[next_index])
        context = context[1:] + [next_index]

    return seed + "".join(output)


# Higher temperatures make character choices less predictable.
for temperature in (0.1, 0.5, 0.7, 1.0):
    print(f"\n=== Temperature {temperature} ===")
    print(generate(temperature=temperature))