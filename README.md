<!-- TOC -->
* [What is that?](#what-is-that)
  * [Local run](#local-run)
  * [Deploy](#deploy)
<!-- TOC -->

# What is that?

A small website with a bunch of jockes


## Local run

```bash
poetry run uvicorn stuff_website.main:app --reload --app-dir src
```

## Deploy


```bash
ruff check
```

```bash
poetry lock
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

```bash
pytest --cov=. --cov-report=term
```