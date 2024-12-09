FROM python:3.12-alpine

WORKDIR /app


COPY . /app

RUN pip install poetry

RUN poetry install --no-dev

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["poetry", "run", "python", "-m", "main"]