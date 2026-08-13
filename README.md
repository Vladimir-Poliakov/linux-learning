Linux & DevOps Practice

A practical DevOps learning portfolio covering Linux administration, Bash scripting, Python automation, Docker, Kubernetes, Terraform, networking, CI/CD, REST APIs and automated testing.

This repository contains hands-on labs and projects completed during my Cloud & DevOps training and independent practice.

Technologies

Linux / Ubuntu

Bash

Python

Git / GitHub

Docker

Docker Compose

Kubernetes

Terraform

NGINX

systemd

REST API

HTTP / JSON

unittest

unittest.mock

GitHub Actions

CI/CD

TCP/IP

SSH

iptables

VirtualBox

Repository Structure

linux-learning/
├── .github/
│   └── workflows/
├── config/
├── docker-nginx-practice/
├── flask-docker-app/
│   └── handlers/
│       └── pull_requests.py
├── kubernetes/
├── permissions-practice/
├── python-api-testing/
│   ├── handlers/
│   │   └── pull_requests.py
│   ├── tests/
│   │   └── test_pull_requests.py
│   ├── requirements.txt
│   └── README.md
├── server/
├── src/
├── systemd-practice/
├── terraform-docker/
├── test_restore/
├── app.py
├── backup.sh
├── networking-practice.md
├── software-management.md
├── ssh-practice.md
└── README.md

Projects

1. Python API Testing

Hands-on Python project focused on REST API integration and automated testing.

The project uses the GitHub Pull Requests API and demonstrates how to work with external APIs without making real requests during unit tests.

Technologies

Python

Requests

REST API

JSON

unittest

unittest.mock

GitHub API

Git

GitHub Actions

Key Topics

HTTP GET requests

API response processing

Request parameters

Pagination

Bearer token authentication

Environment variables

Mocking external HTTP requests

Unit testing

The project contains tests for:

API response processing

Empty API responses

Correct API endpoint

Request parameters

HTTP headers

Bearer token authentication

The tests use unittest.mock.patch so that they do not require a real request to GitHub.

2. Flask Docker Application

A Flask application packaged and executed as a Docker container.

The project demonstrates how a Python web application can be containerized and run using Docker and Docker Compose.

Technologies

Python

Flask

Docker

Docker Compose

Git

REST API

Key Topics

Flask application structure

Dockerfile

Docker image creation

Python dependencies

Containerized application execution

Docker Compose

Application configuration

API integration

The application includes a route for retrieving GitHub pull requests through the Python API handler.

3. Python Archive Cleaner

A Python automation script for processing ZIP archives and removing directories that do not contain __init__.py.

Technologies

Python

ZIP archives

File system operations

Temporary directories

Logging

Key Topics

os

os.walk

tempfile

zipfile

shutil

command-line arguments

logging

file and directory management

The script:

Receives a ZIP archive as a command-line argument.

Creates a temporary directory.

Extracts the archive.

Analyses the directory structure.

Finds directories without __init__.py.

Removes the selected directories.

Creates cleaned.txt with the removed directory paths.

Creates a new cleaned archive.

This project demonstrates practical Python automation for file-system operations.

4. Bash Transfer Tool

A Bash command-line tool for uploading and downloading files using free.keep.sh.

Technologies

Bash

curl

command-line arguments

shell scripting

Supported Operations

Upload a file:

./transfer.sh file.txt

Upload multiple files:

./transfer.sh file1.txt file2.txt

Download a file:

./transfer.sh -d ./downloads FILE_ID file.txt

Display help:

./transfer.sh -h

Display the tool version:

./transfer.sh -v

Key Topics

Bash functions

command-line argument processing

flags

case

variables

readonly

curl

error handling

file validation

command-line tools

The project demonstrates practical Bash scripting and command-line tool development.

5. Linux Network Router Lab

Practical Linux networking exercises using virtual machines.

Technologies

Linux

VirtualBox

TCP/IP

Routing

NAT

IP forwarding

iptables

Key Topics

Network interfaces

IP addresses

Routing

NAT

Packet forwarding

Linux firewall configuration

Virtual machine networking

The lab demonstrates practical configuration and troubleshooting of Linux networking between virtual machines.

6. Kubernetes Practice

Hands-on Kubernetes deployment practice for a web application.

Technologies

Kubernetes

YAML

Pods

Deployments

Services

NGINX

Key Topics

Kubernetes Deployment

Kubernetes Service

Containerized applications

Application exposure

YAML configuration

Basic Kubernetes operations

The project demonstrates how a containerized web application can be deployed and exposed using Kubernetes resources.

7. Terraform + Docker

Infrastructure as Code practice using Terraform and Docker.

Technologies

Terraform

Docker

HCL

Infrastructure as Code

Key Topics

Terraform configuration

Docker resources

Infrastructure provisioning

Declarative configuration

Infrastructure as Code workflow

The project demonstrates how infrastructure can be described and managed using Terraform instead of manually creating Docker resources.

8. Docker + NGINX Practice

Practical containerization and web server exercises using Docker and NGINX.

Technologies

Docker

NGINX

Linux

Docker Compose

Key Topics

Docker containers

NGINX

Port mapping

Container configuration

Web server deployment

Container troubleshooting

9. systemd Practice

Linux service management and troubleshooting practice using systemd.

Technologies

Linux

systemd

journalctl

Bash

Key Topics

systemd services

Service lifecycle

Service configuration

systemctl

journalctl

Service troubleshooting

Linux process management

10. Linux Permissions Practice

Hands-on Linux exercises focused on users, groups, permissions and file access.

Technologies

Linux

Bash

File permissions

Key Topics

Users

Groups

Ownership

chmod

chown

umask

File access control

11. Linux Software Management

Practical Linux package and software management exercises.

Technologies

Linux

Ubuntu

APT

NGINX

Apache

Key Topics

Package installation

Package removal

Package updates

Service troubleshooting

Web server installation and configuration

12. SSH Practice

Practical SSH administration exercises.

Technologies

Linux

SSH

SCP

Bash

Key Topics

SSH connections

SSH keys

SSH configuration

Secure remote access

File transfer with SCP

13. Backup Automation

Bash scripting practice for automated backup operations.

Technologies

Bash

Linux

Shell scripting

Key Topics

Backup automation

Command-line arguments

File operations

Hostname detection

Error handling

CI/CD and GitHub Actions

The repository also contains GitHub Actions workflows used to automate repository checks and Python testing.

The workflows demonstrate:

Workflow configuration

Automated execution on push

Python environment setup

Dependency installation

Automated testing

Repository checks

The goal is to connect development work with automated validation through CI.

DevOps Skills Demonstrated

Linux

Linux command line

File system management

Permissions

Users and groups

SSH

Networking

Processes

systemd

Logs

Package management

Bash

Shell scripting

Automation

Command-line tools

Argument parsing

Error handling

File operations

Python

Scripting

Automation

REST API integration

JSON processing

File-system automation

Unit testing

Mocking

Docker

Dockerfiles

Images

Containers

Port mapping

Docker Compose

Application containerization

Kubernetes

Deployments

Services

YAML configuration

Container orchestration basics

Terraform

Infrastructure as Code

Declarative configuration

Docker resource management

CI/CD

GitHub Actions

Automated testing

Workflow configuration

Repository checks

Learning Approach

The repository is built around hands-on practice.

Each lab focuses on solving a practical task and documenting the technologies and techniques used to solve it.

The progression covers:

Linux
  ↓
Bash
  ↓
Git
  ↓
Python
  ↓
REST APIs
  ↓
Testing
  ↓
Docker
  ↓
Docker Compose
  ↓
NGINX
  ↓
Kubernetes
  ↓
Terraform
  ↓
CI/CD

Goal

The goal of this repository is to demonstrate practical skills required for a Junior DevOps / Cloud Engineer role, with a focus on:

Linux administration

Automation

Python scripting

Bash scripting

REST APIs

Automated testing

Docker

Docker Compose

Kubernetes

Terraform

Infrastructure as Code

CI/CD

GitHub Actions

Networking

Author

Vladimir Poliakov

Junior DevOps / Cloud Engineer
