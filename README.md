# ToxASCII

ToxASCII is the official code repository accompanying the paper "*Read Over the Lines: Attacking LLMs and Toxicity Detection Systems with ASCII Art to Mask Profanity*," available on [arXiv](https://arxiv.org/abs/2409.18708). This repository provides the necessary tools and data to replicate the experiments detailed in the paper, showcasing how ASCII art can be used to bypass modern toxicity detection systems.

## Overview

The ToxASCII project introduces a novel family of adversarial attacks that exploit the inability of language models (LLMs) and toxicity detection systems to interpret ASCII art. By leveraging custom fonts and embedding toxic language in spatial patterns, ToxASCII successfully bypasses content moderation. Key contributions include:

- **ToxASCII Benchmark**: A dataset of manually selected toxic phrases embedded in ASCII art.
- **Adversarial Attacks**: Techniques using both ASCII art and special tokens to evade detection.
- **Evaluation Results**: Demonstrated a 1.0 attack success rate across multiple LLMs, including OpenAI and LLaMA models.

#
