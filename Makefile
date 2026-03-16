```makefile
.PHONY: help install dev test lint format migrate upgrade downgrade clean docker-build docker-up docker-down

help:
	@echo "Available commands:"
	@echo "  install      Install production dependencies"
	@echo "  dev          Install development dependencies"
	@echo "  test         Run tests"
	@echo "  lint         Run linters (flake8, mypy)"
	@echo "  format       Format code with black and isort"
	@echo "  migrate      Create new migration (message required: make migrate msg='your message')"
	@echo "  upgrade      Apply all migrations"
	@echo "  downgrade    Rollback last migration"
	@echo "  clean        Remove cache files and build artifacts"
	@echo "  docker-build Build Docker image"
	@echo "  docker-up    Start Docker Compose environment"
	@echo "  docker-down  Stop Docker Compose environment"

install:
	pip install -r requirements.txt

dev: install
	pip install -r requirements-dev.txt
	pre-commit install

test:
	pytest tests/ -v --cov=src/agentloopgen --cov-report=term-missing

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/
	isort src/ tests/

migrate:
	@if [ -z "$(msg)" ]; then \
		echo "Error: message required. Usage: make migrate msg='your message'"; \
		exit 1; \
	fi
	alembic revision --autogenerate -m "$(msg)"

upgrade:
	alembic upgrade head

downgrade:
	alembic downgrade -1

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docker-build:
	docker build -t agentloopgen:latest .

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down
```