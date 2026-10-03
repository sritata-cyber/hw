# HW4 starter: a tiny text generator

GLBL 5053 · Homework 4

`tiny_rnn.py` trains a very small neural network on ten short sentences and then generates new text one character at a time. You will run it, add comments to understand it, and track your work with Git.

## 1. Make your own copy

1. Near the top of this page, click **Use this template** → **Create a new repository**.
2. Owner: your GitHub account. Name: `hw4`, or anything you like. Visibility: **Private** is recommended. Your instructor will tell you how to share access.
3. Click **Create repository**. You now have your own repository, and your commits go there.

## 2. Clone it in VS Code

1. Open a new VS Code window and click **Clone Git Repository...**
2. Paste the link to *your* new repository (`https://github.com/<your-username>/hw4`), then choose a folder to put it in.
3. Open a terminal (**Terminal → New Terminal**), type `ls`, and press Enter. You should see `README.md`, `requirements.txt` and `tiny_rnn.py`.

## 3. Check your Python version

You need **Python 3.10–3.13**. TensorFlow does not support Python 3.14 yet.

```
python3 --version
```

If it says 3.14 or later, install Python 3.13 from [python.org](https://www.python.org/downloads/) and use `python3.13` in the next step (on Windows, use `py -3.13`).

If you have an **Intel Mac**, use Python 3.12 or earlier. TensorFlow 2.16 is the last TensorFlow release with Intel Mac support. If this is a problem, use the Google Colab option at the end instead.

## 4. Create a virtual environment

A virtual environment keeps this homework's packages separate from the rest of your computer. Run the commands for your operating system.

- macOS/Linux:
  ```
  python3 -m venv .venv
  source .venv/bin/activate
  ```
  (Replace `python3` with `python3.13` if you installed it in step 3.)
- Windows (PowerShell):
  ```
  py -3.13 -m venv .venv
  .venv\Scripts\activate
  ```

If this worked, you will see `(.venv)` at the start of the line in your terminal.

## 5. Install TensorFlow

```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

This download is large, so it can take a few minutes. Confirm that the installation worked:

```
python -c "import tensorflow as tf; print(tf.__version__)"
```

If VS Code asks which Python interpreter to use, choose the one whose path contains `.venv`.

If you close the terminal and come back later, activate the environment again before running the homework:

- macOS/Linux: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`

## 6. Run the starter code

```
python tiny_rnn.py
```

It takes about a minute. TensorFlow prints some warning lines first; those are normal. At the end, you should see generated text like `I like puzzles.` at four different temperatures.

## If installing gets stuck

You can run the same file in [Google Colab](https://colab.research.google.com/), which already has TensorFlow: upload `tiny_rnn.py` using the folder icon on the left, then run `%run tiny_rnn.py` in a code cell. Keep committing your edits to your repository in VS Code as usual.

This setup guide was drafted by Codex (OpenAI), based on the direction of Xiuye Chen.
