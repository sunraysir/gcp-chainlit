# Venturenix Next-Gen AI Development Class Cohort #5

## Lesson 6: Building and Containerizing a Simple AI Chat App

This lesson demonstrates how to build a simple AI chat application using PydanticAI and Chainlit, then containerize it for deployment.

### What We Built

- **AI Chat Application**: A simple chat interface using PydanticAI with Chainlit
- **Model Integration**: Uses Google's Gemini 2.5 Flash Lite model via OpenRouter
- **Language Support**: Configured to respond in Hong Kong Traditional Chinese
- **Containerization**: Ready for Docker deployment

### Key Components

- `main.py`: Main application with PydanticAI agent and Chainlit interface
- `pyproject.toml`: Python project configuration with dependencies
- `uv.lock`: Dependency lock file for reproducible builds

### Next Steps: GCP Cloud Run Deployment

The next phase of this lesson will cover:

1. **Containerization**: Creating a Dockerfile for the application
2. **GCP Setup**: Configuring Google Cloud Platform
3. **Cloud Run Deployment**: Deploying the containerized app to Google Cloud Run
4. **Environment Configuration**: Setting up environment variables and secrets
5. **Monitoring**: Basic logging and monitoring setup

### Prerequisites

- Python 3.8+
- UV package manager
- Docker (for containerization)
- Google Cloud SDK (for deployment)

### Running Locally

```bash
# Install dependencies
uv sync

# Run the application
uv run chainlit run main.py
```

### Dockerfile Explanation

The `Dockerfile` containerizes our application for deployment:

```dockerfile
FROM python:3.14-slim-bookworm
COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/
```
- Uses Python 3.14 slim image for smaller container size
- Installs UV package manager from the official Astral UV image

```dockerfile
WORKDIR /app
ADD . /app
```
- Sets `/app` as the working directory
- Copies all project files into the container

```dockerfile
RUN uv sync --locked
```
- Installs dependencies using the locked versions from `uv.lock`
- Ensures reproducible builds across environments

```dockerfile
EXPOSE 8080
ENTRYPOINT ["uv", "run", "chainlit", "run", "-h", "--host=0.0.0.0", "--port=8080", "main.py"]
```
- Exposes port 8080 for the web application
- Runs Chainlit with host binding to `0.0.0.0` (required for container networking)
- Uses UV to run the application with proper dependency resolution

### Project Structure

```
cohort5/
├── main.py          # Main application
├── pyproject.toml   # Project configuration
├── uv.lock         # Dependency lock file
├── Dockerfile      # Container configuration
└── README.md       # This file
```
