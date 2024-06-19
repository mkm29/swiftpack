FROM python:3.11.8-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gcc libffi-dev g++
WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.8.2

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN . /venv/bin/activate && poetry install --no-dev --no-root

COPY . .
RUN . /venv/bin/activate && poetry build

FROM base as final

COPY --from=builder /venv /venv
COPY --from=builder /app/dist .

ENV PATH="/venv/bin:$PATH"

RUN pip install *.whl

# Since the virtual environment is activated in a RUN instruction, it will not persist to the ENTRYPOINT or CMD.
ENTRYPOINT ["/bin/bash", "-c", "source /venv/bin/activate && exec $0 \"$@\"", "uvicorn"]
CMD ["--port", "8000", "swiftpack.src.main:create_app", "--factory", "--workers", "1", "--host", "0.0.0.0"]
