# Python API Testing Lab

Hands-on Python practice focused on REST API integration, unit testing, mocking external requests, authentication headers and test automation.

## Project Overview

This project demonstrates how to work with a REST API from Python and how to test API-related code without making real external requests.

The project uses the GitHub Pull Requests API as an example.

## Technologies

- Python
- Requests
- unittest
- unittest.mock
- REST API
- JSON
- Git
- GitHub

## Project Structure

python-api-testing/
├── handlers/
│   └── pull_requests.py
├── tests/
│   └── test_pull_requests.py
├── requirements.txt
└── README.md

## API Integration

The application sends a GET request to the GitHub API:

https://api.github.com/repos/boto/boto3/pulls

The request supports:

- Pull request state filtering
- Pagination configuration
- Optional Bearer token authentication

The response is converted into a simplified Python data structure containing:

- Pull request number
- Pull request title
- Pull request URL

## Authentication

The API token is read from an environment variable:

TOKEN

The token is not stored directly in the source code.

When the token is available, the application sends it using:

Authorization: Bearer <TOKEN>

This demonstrates basic secure handling of API credentials.

## Testing

The project contains unit tests for the API integration logic.

External HTTP requests are mocked using:

unittest.mock.patch

The tests verify:

- Correct API response processing
- Empty API responses
- Correct API endpoint
- Correct request parameters
- HTTP headers
- Bearer token authentication

The tests do not require a real request to GitHub.

## Example Test Scenarios

### Successful API Response

The test provides a mocked API response containing pull requests and verifies that the function returns the expected simplified data.

### Empty Response

The test verifies that an empty API response produces an empty list.

### Request Parameters

The test verifies that the correct API endpoint and parameters are used.

### Authentication

The test verifies that the Bearer token is correctly added to the Authorization header when the TOKEN environment variable is available.

## Running the Tests

Install dependencies:

pip install -r requirements.txt

Run the tests:

python -m unittest discover

## What This Project Demonstrates

- Python scripting
- REST API integration
- HTTP requests
- JSON data processing
- Unit testing
- Mocking external services
- Environment variables
- Basic API authentication
- Test-driven troubleshooting
- Clean project structure

## Cloud / DevOps Relevance

This project is part of my practical Cloud and DevOps learning.

The skills demonstrated here are relevant to:

- Cloud Operations
- Infrastructure automation
- API-based services
- CI/CD pipelines
- Automated testing
- Monitoring and operational tooling
- Python automation

The project can be extended with automated testing through GitHub Actions and integrated into a CI pipeline.
