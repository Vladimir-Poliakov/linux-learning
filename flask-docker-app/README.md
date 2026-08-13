# Flask Docker Application

A hands-on DevOps project demonstrating how to containerize a Python Flask application and integrate it with the GitHub Pull Requests API.

## Project Overview

This project demonstrates:

- Python Flask application
- REST API integration
- Docker containerization
- Docker Compose
- Bash build script
- Environment variables
- Bearer token authentication
- GitHub API integration

The application uses the GitHub Pull Requests API to retrieve pull requests from the boto3 repository.

## Technologies

- Python
- Flask
- Requests
- Docker
- Docker Compose
- Bash
- GitHub REST API

## Project Structure

```text
flask-docker-app/
├── handlers/
│   └── pull_requests.py
├── Dockerfile
├── build.sh
├── docker-compose.yml
├── requirements.txt
├── start.py
└── README.md
```

## Docker

The application is packaged into a Docker image using the provided Dockerfile.

The Dockerfile:

1. Uses Python 3.8
2. Creates `/app` as the working directory
3. Installs Python dependencies
4. Copies the application files
5. Starts the Flask application

## Docker Compose

Docker Compose is used to build and run the Flask application as a containerized service.

The application exposes port `5000`.

## GitHub API

The application communicates with:

```text
https://api.github.com/repos/boto/boto3/pulls
```

The API request supports:

- Pull request state filtering
- Pagination
- Optional Bearer token authentication

## Authentication

The GitHub API token is provided through the `TOKEN` environment variable.

The token is not stored directly in the source code.

When a token is available, the application sends:

```text
Authorization: Bearer <TOKEN>
```

This demonstrates basic handling of API credentials using environment variables.

## Build

Build the Docker image using:

```bash
./build.sh
```

Or build it directly with Docker:

```bash
docker build -t flask-app .
```

## Run with Docker Compose

```bash
docker compose up --build
```

The application will be available on:

```text
http://localhost:5000
```

## DevOps Relevance

This project demonstrates practical skills relevant to Junior DevOps and Cloud Engineer positions:

- Docker
- Containerization
- Docker Compose
- Linux/Bash
- Python automation
- REST APIs
- Environment variables
- API authentication
- Application deployment
- Infrastructure and application troubleshooting

## Future Improvements

Possible improvements include:

- Adding automated tests
- Adding GitHub Actions CI/CD
- Adding a Jinja2 web template
- Adding Docker health checks
- Adding production WSGI server configuration
- Adding logging and monitoring
