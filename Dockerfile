FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build tools (only if needed for compiling extensions)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade packaging tools
RUN python -m pip install --upgrade pip setuptools wheel

# Copy pyproject first to leverage layer cache
#COPY pyproject.toml README.md ./

# Copy project files
COPY . .

# Install package in editable mode including dev deps (pytest)
RUN pip install -e .[dev]

# Default: run tests
CMD ["pytest", "-q"]
