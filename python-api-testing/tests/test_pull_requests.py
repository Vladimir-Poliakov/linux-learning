from unittest import TestCase
from unittest.mock import patch

from handlers.pull_requests import get_pull_requests


class TestPullRequests(TestCase):

    @patch("handlers.pull_requests.requests.get")
    def test_get_pull_requests(self, get_mock):
        get_mock.return_value.json.return_value = [
            {
                "number": 1,
                "title": "First PR",
                "html_url": "https://github.com/boto/boto3/pull/1",
            },
            {
                "number": 2,
                "title": "Second PR",
                "html_url": "https://github.com/boto/boto3/pull/2",
            },
        ]

        expected = [
            {
                "num": 1,
                "title": "First PR",
                "link": "https://github.com/boto/boto3/pull/1",
            },
            {
                "num": 2,
                "title": "Second PR",
                "link": "https://github.com/boto/boto3/pull/2",
            },
        ]

        result = get_pull_requests("open")

        self.assertEqual(result, expected)

        get_mock.assert_called_once()

    @patch("handlers.pull_requests.requests.get")
    def test_get_pull_requests_empty(self, get_mock):
        get_mock.return_value.json.return_value = []

        result = get_pull_requests("closed")

        self.assertEqual(result, [])

        get_mock.assert_called_once()

    @patch("handlers.pull_requests.requests.get")
    def test_requests_called_with_correct_params(self, get_mock):
        get_mock.return_value.json.return_value = []

        get_pull_requests("closed")

        args, kwargs = get_mock.call_args

        self.assertEqual(
            args[0],
            "https://api.github.com/repos/boto/boto3/pulls",
        )

        self.assertEqual(kwargs["params"]["state"], "closed")
        self.assertEqual(kwargs["params"]["per_page"], 100)

    @patch("handlers.pull_requests.requests.get")
    def test_requests_headers(self, get_mock):
        get_mock.return_value.json.return_value = []

        get_pull_requests("open")

        _, kwargs = get_mock.call_args

        self.assertIn("headers", kwargs)

    @patch("handlers.pull_requests.TOKEN", "my_token")
    @patch("handlers.pull_requests.requests.get")
    def test_request_with_token(self, get_mock):
        get_mock.return_value.json.return_value = []

        get_pull_requests("open")

        _, kwargs = get_mock.call_args

        self.assertEqual(
            kwargs["headers"],
            {"Authorization": "Bearer my_token"},
        )
