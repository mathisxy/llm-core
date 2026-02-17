# Intermediate Representation for LLM Chats

[![Pipy](https://img.shields.io/pypi/v/llmir)](https://pypi.org/project/llmir/)
[![Downloads](https://img.shields.io/pypi/dm/llmir)](https://pypi.org/project/llmir/#files)
[![Issues](https://img.shields.io/github/issues/mathisxy/llmir)](https://github.com/mathisxy/llmir/issues)
[![Type Check](https://github.com/mathisxy/llmir/actions/workflows/typecheck.yml/badge.svg?branch=main)](https://github.com/mathisxy/llmir/actions/workflows/typecheck.yml)
[![Deploy Docs](https://github.com/mathisxy/llmir/actions/workflows/docs.yml/badge.svg)](https://github.com/mathisxy/llmir/actions/workflows/docs.yml)
[![Documentation](https://img.shields.io/badge/Docs-GitHub%20Pages-blue)](https://mathisxy.github.io/llmir/)

This repository provides the core types for a standardized way to represent messages for LLMs. Additional chunk-types will be added in the future.

## Installation via Pypi:

```bash
pip install llm-ir
```

## Imports:

```python
from llm_ir import AIMessage, AIRoles, AIChunks, AIChunkText, AIChunkFile, AIChunkImageURL
```
