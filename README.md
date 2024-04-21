# QSolver

## Overview

QSolver is a project aimed at generating study notes for exams using an open-source language model (LLM). It takes a bunch of questions as input from a `questions.txt` file, processes them to generate answers, and creates well-structured study notes.

## Motivation

The motivation behind QSolver is to empower students and learners by providing them with a tool to create high-quality study materials for exams. With the rise of open-source language models like GPT (Generative Pre-trained Transformer), there's an opportunity to leverage these models to automate the process of generating study notes from questions. By integrating with the LLMs, QSolver aims to streamline the creation of study materials, saving students time and effort while ensuring accuracy and comprehensiveness.

## Features

-   Takes questions as input from `questions.txt` file.
-   Utilizes the OLLAMA API to generate answers to the questions.
-   Generates well-structured study notes based on the questions and answers.
-   Provides an easy-to-use interface for generating study materials.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/snoofox/QSolver.git
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your questions in the `questions.txt` file. Each question should be on a separate line.
2. Run the QSolver script:
    ```
    python main.py
    ```
3. QSolver will process the questions using the OLLAMA API and generate study notes.

## Configuration

-   You need to obtain an API from OLLAMA and configure it in the `main.py` file.

## Contribution

Contributions are welcome! If you have ideas for improvements or find any issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
