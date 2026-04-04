.PHONY: run migrate worker seed lint

run:
	uvicorn app.main:app --reload --port 8000

migrate:
	alembic upgrade head

worker:
	celery -A app.agent_loop.worker worker --loglevel=info

seed:
	python seed.py

lint:
	ruff check app/
