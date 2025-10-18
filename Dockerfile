FROM python:3.14-slim-bookworm
COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/

WORKDIR /app

ADD . /app

RUN uv sync --locked

EXPOSE 8080

ENTRYPOINT ["uv", "run", "chainlit", "run", "-h", "--host=0.0.0.0", "--port=8080", "main.py"]