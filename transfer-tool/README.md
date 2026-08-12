# Bash File Transfer Tool

A hands-on Bash automation project demonstrating command-line file upload and download operations using a remote file transfer service.

## Project Overview

The project provides a command-line Bash tool for transferring files.

The script supports:

- File upload
- File download
- Multiple file uploads
- Help command
- Version command
- Input validation
- Error handling
- Command-line argument processing

## Technologies

- Bash
- Linux
- curl
- Shell scripting
- Command-line utilities

## Project Structure

```text
transfer-tool/
├── transfer.sh
└── README.md
```

## Version

Current version:

```text
0.0.1
```

## Upload

Upload a single file:

```bash
./transfer.sh test.txt
```

Upload multiple files:

```bash
./transfer.sh test.txt test2.txt
```

The script validates the local file path and uploads the file using `curl`.

## Download

Download a file:

```bash
./transfer.sh -d ./downloads <file_id> <file_name>
```

The destination directory is created automatically when it does not exist.

## Help

Display the help message:

```bash
./transfer.sh -h
```

## Version

Display the current version:

```bash
./transfer.sh -v
```

## Error Handling

The script checks for:

- Invalid file paths
- Invalid download arguments
- Failed upload operations
- Failed download operations

The script exits with a non-zero status when an operation fails.

## Bash Features Demonstrated

This project demonstrates practical Bash scripting concepts:

- Functions
- Local variables
- Read-only variables
- `case` statements
- `if` conditions
- Loops
- Command-line arguments
- Exit codes
- `curl`
- Command substitution
- Here documents
- Basic error handling

## DevOps Relevance

This project demonstrates skills useful for Junior DevOps and Cloud Engineer roles:

- Linux command line
- Bash automation
- Shell scripting
- File operations
- HTTP-based file transfer
- CLI tool development
- Error handling
- Automation of repetitive operational tasks

## Possible Improvements

Future improvements could include:

- Better argument validation
- Automated tests
- ShellCheck integration
- CI/CD with GitHub Actions
- Configuration through environment variables
- More detailed logging
- Download progress and retry support
