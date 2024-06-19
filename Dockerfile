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

FROM python:3.11.8-slim as prod

COPY --from=builder --chown=65534:65534 /venv /venv
COPY --from=builder --chown=65534:65534 /app/dist .

ENV PATH="/venv/bin:$PATH"

# harden
# update util-linux
RUN apt-get update && apt-get install -y --no-install-recommends \
    util-linux \
    libc-bin \
    && rm -rf /var/lib/apt/lists/*

# update pypa-setuptool
RUN pip install --upgrade pip setuptools wheel

# switch to the nobody user
USER 65534

RUN pip install  *.whl

EXPOSE 8000

# Since the virtual environment is activated in a RUN instruction, it will not persist to the ENTRYPOINT or CMD.
ENTRYPOINT ["/bin/bash", "-c", "source /venv/bin/activate && exec $0 \"$@\"", "uvicorn"]
CMD ["--port", "8000", "swiftpack.src.main:create_app", "--factory", "--workers", "1", "--host", "0.0.0.0"]
