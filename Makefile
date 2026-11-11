.PHONY: install dev test lint format check

install:
	uv sync

dev:
	lk agent dev

test:
	uv run pytest -v

lint:
	uv run ruff check .

format:
	uv run ruff format .

check:
	uv run ruff check .
	uv run ruff format --check .
	uv run pytest -v