FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    make \
    gcc \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# Create app directory
WORKDIR /app

# Copy project files
COPY . .

# Create virtualenv and install the application
RUN uv venv /app/.venv && \
    uv pip install --python /app/.venv/bin/python .

# Make the venv the default Python environment
ENV PATH="/app/.venv/bin:${PATH}"

# Run the application
# Replace `your_package` with your package/module name
CMD ["uv", "run", "dungeondice-matrix"]
