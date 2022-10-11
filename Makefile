install:
	poetry install

test:
	QT_QPA_PLATFORM=offscreen poetry run pytest tests

build:
	poetry build -n

ci: install test

.PHONY: ci install test build
