# audiobook
Simple Audiobook manager

## Idea
1. Store each audiobook in separate direcoty
2. Have book meta-data stored in `audiobook.yaml` file in the root directory of the audiobook
3. Provide a command line tool to scan recursively directory and find all the meta-files inside
4. Provide `init` command which will create the meta-data template file and optionaly search third party for the meta-data

## Sample yaml file

```yaml
title: "Calculating the Cosmos: How Mathematics Unveils the Universe"
authors:
  - Ian Stewart
ISBN: '9780465096107'
cover: 'Calculating the Cosmos.jpg'
tags:
  - science
  - mathematics
rating: 4.13
language: English

```

## Usage
```
$ audiobook
Usage: audiobook [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  init  Initialize the current directory as audio...
  scan  Scans directory for audio books and prints the...
  ```
