import os
import requests


TOKEN = os.getenv("TOKEN")


def get_pull_requests(state):
    """
    Get pull requests from GitHub API.

    Returns a list containing:
    - pull request title
    - pull request number
    - pull request URL
    """

    headers = {}

    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    response = requests.get(
        "https://api.github.com/repos/boto/boto3/pulls",
        headers=headers,
        params={
            "state": state,
            "per_page": 100,
        },
    )

    return [
        {
            "title": pr["title"],
            "num": pr["number"],
            "link": pr["html_url"],
        }
        for pr in response.json()
    ]
