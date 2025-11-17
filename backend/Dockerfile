FROM python:3.12-slim

# Install uv using pip
RUN pip install uv

# Set working directory
WORKDIR /backend

# Copy dependency files first
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-cache

# Copy the rest of the application
COPY . .

# Run using uvicorn (more reliable than fastapi cli)
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]