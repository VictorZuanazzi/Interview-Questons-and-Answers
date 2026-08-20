FROM python:3.13-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --extra dev --no-install-project

COPY . .
ENV PATH="/app/.venv/bin:$PATH"
