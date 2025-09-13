run:
	python -m src.main

lint:
	ruff check . && ruff check . --diff

format:
	ruff check . --fix && ruff format .
