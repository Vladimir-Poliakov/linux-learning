# Python Archive Cleaner

A hands-on Python automation project for processing ZIP archives and cleaning unnecessary directories based on Python package structure.

## Project Overview

This project demonstrates how to automate archive processing using Python.

The script:

1. Accepts a ZIP archive from the command line.
2. Creates a temporary working directory.
3. Extracts the archive.
4. Searches directories inside the extracted project.
5. Detects directories that do not contain `__init__.py`.
6. Removes the detected directories.
7. Creates a `cleaned.txt` report.
8. Creates a new cleaned ZIP archive.
9. Logs the main processing steps.

## Technologies

- Python
- Linux
- Bash / CLI
- ZIP archives
- File system automation
- Logging

## Python Modules

The project uses standard Python libraries:

- `os`
- `sys`
- `tempfile`
- `zipfile`
- `shutil`
- `logging`

No external Python packages are required.

## Project Structure

```text
python-archive-cleaner/
├── clean_app.py
└── README.md
```

## How It Works

The script receives a ZIP archive as a command-line argument:

```bash
python clean_app.py project.zip
```

The archive is extracted into a temporary directory.

The script then walks through the extracted directory tree and checks whether directories contain:

```text
__init__.py
```

Directories without this file are collected and removed.

A report is generated in:

```text
cleaned.txt
```

Finally, a new archive is created using the original archive name with `_new` added before the extension.

Example:

```text
project.zip
project_new.zip
```

## Logging

The application uses Python logging to report important processing stages:

- Temporary directory creation
- Archive extraction
- Folders selected for removal
- Folder removal
- New archive creation
- Completion

## Example

```bash
python clean_app.py project.zip
```

Example output:

```text
INFO: Temporary directory created
INFO: Archive extracted
INFO: Folders to remove:
docs
examples
INFO: Removed: docs
INFO: Removed: examples

Remaining folders:
['src', 'tests', 'cleaned.txt']

INFO: Creating archive: project_new.zip
INFO: Done
```

## DevOps Relevance

This project demonstrates practical automation skills relevant to DevOps:

- Linux file system operations
- Python automation
- CLI tools
- Archive processing
- Temporary environments
- Logging
- File cleanup
- Automation of repetitive operational tasks

## Possible Improvements

Future improvements could include:

- Unit tests
- Input validation
- Safe ZIP extraction
- Configurable cleanup rules
- Docker containerization
- CI testing with GitHub Actions
