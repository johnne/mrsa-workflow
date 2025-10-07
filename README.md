# MRSA Workflow

[![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)
[![PyPI - Version](https://img.shields.io/pypi/v/mrsa-workflow.svg)](https://pypi.org/project/mrsa-workflow)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mrsa-workflow.svg)](https://pypi.org/project/mrsa-workflow)

-----

## Description

This repository shows how to package a Snakemake workflow into a command line
interface using [snk-cli](https://github.com/Wytamma/snk-cli). The
`pyproject.toml` file is a configuration file for packaging python tools. It is
supplemented with a tool-specific entries for `pixi`, making it possible to
install both the workflow and its dependencies with Pixi.

## Table of Contents

- [Installation](#installation)
- [Running](#running)
- [License](#license)

## Installation

With Pixi:

```console
pixi shell
```

## Running

To see available parameters run:

```console
mrsa-workflow run -h
```

Run with default parameters:

```console
mrsa-workflow run
```

## License

`mrsa-workflow` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
