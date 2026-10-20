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