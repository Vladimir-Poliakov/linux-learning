# Linux & DevOps Practice

Hands-on learning repository focused on Linux administration, Cloud and DevOps engineering, automation, containers, networking and infrastructure.

This repository contains practical labs and small projects developed during my Cloud & DevOps training and personal practice.

The main goal is to build practical engineering skills through implementation, troubleshooting, testing and automation.

## Core Skills

- Linux administration
- Bash scripting
- Python automation
- Git and GitHub
- Docker
- Docker Compose
- Kubernetes
- Terraform
- CI/CD
- GitHub Actions
- REST APIs
- Unit testing
- Mocking
- Networking fundamentals
- NGINX
- systemd
- SSH
- iptables
- Infrastructure as Code
- Troubleshooting

---

# Featured Projects

## 1. Python API Testing

A Python project demonstrating REST API integration with the GitHub Pull Requests API.

### Technologies

- Python
- Requests
- REST API
- JSON
- unittest
- unittest.mock
- Environment variables
- Bearer token authentication
- GitHub Actions

### Project

`python-api-testing/`

### What I implemented

- GitHub Pull Requests API integration
- Pull request state filtering
- API request parameters
- Pagination configuration
- Optional Bearer token authentication
- Environment variable based token handling
- JSON response processing
- Unit tests
- Mocking of external HTTP requests
- Validation of API endpoint and request parameters
- Validation of HTTP headers
- Automated test execution with GitHub Actions

The tests use mocked HTTP requests, so they do not depend on the real GitHub API.

---

## 2. Flask Docker Application

A Flask web application integrated with the GitHub Pull Requests API and packaged as a Docker container.

### Technologies

- Python
- Flask
- Requests
- Docker
- Docker Compose
- Bash
- REST API
- Environment variables

### Project

`fflask-docker-app/`

### What I implemented

- Flask application
- REST API integration
- Dockerfile
- Python dependency management
- Docker image creation
- Docker container execution
- Docker Compose configuration
- Application startup configuration
- Integration with GitHub Pull Requests functionality

The project demonstrates how a Python web application can be packaged and run as a containerized service.

---

## 3. Python Archive Cleaner

A Python automation utility for processing and cleaning ZIP archives.

### Technologies

- Python
- Linux
- ZIP
- tempfile
- zipfile
- os
- os.walk
- shutil
- logging
- CLI arguments

### Project

`python-archive-cleaner/`

### What I implemented

- ZIP archive extraction
- Temporary directory management
- Recursive filesystem inspection
- Directory validation
- Detection of directories without `__init__.py`
- Automatic removal of unnecessary directories
- Cleanup report generation
- Creation of `cleaned.txt`
- Rebuilding of the cleaned ZIP archive
- Logging
- Command-line argument handling

The project demonstrates practical Python filesystem automation and archive processing.

---

## 4. Bash File Transfer Tool

A command-line Bash utility for uploading and downloading files using `curl`.

### Technologies

- Bash
- Linux
- curl
- CLI
- Shell scripting
- Error handling

### Project

`transfer-tool/`

### Features

- File upload
- File download
- Multiple file uploads
- Help command
- Version command
- Command-line flags
- File path validation
- Error handling
- Functions
- Local variables
- Readonly configuration values

Example commands:

    ./transfer.sh file.txt
    ./transfer.sh file1.txt file2.txt
    ./transfer.sh -d ./downloads FILE_ID file.txt
    ./transfer.sh -h
    ./transfer.sh -v

The project demonstrates practical Bash scripting and command-line tool development.

---

## 5. Linux Network Router Lab

Practical Linux networking exercises using virtual machines.

### Technologies

- Linux
- VirtualBox
- TCP/IP
- Routing
- NAT
- IP forwarding
- iptables
- Network troubleshooting

### Project

`server/`

### What I practiced

- Static IP configuration
- Network interfaces
- Routing tables
- IP forwarding
- NAT configuration
- Firewall rules
- Connectivity testing
- Network troubleshooting

The lab demonstrates how Linux can be configured to route traffic between virtual networks.

---

## 6. Kubernetes Practice

Practical Kubernetes configuration and deployment exercises.

### Technologies

- Kubernetes
- kubectl
- Deployments
- Services
- NGINX
- Containers
- YAML

### Project

`kubernetes/`

### What I practiced

- Kubernetes Deployments
- Replica configuration
- Labels
- Selectors
- Container configuration
- Container ports
- Services
- NGINX deployment
- Basic Kubernetes troubleshooting

The project demonstrates fundamental Kubernetes concepts and application deployment.

---

## 7. Terraform + Docker

Infrastructure as Code practice using Terraform and Docker.

### Technologies

- Terraform
- Docker
- Infrastructure as Code
- NGINX

### Project

`terraform-docker/`

### What I practiced

- Terraform configuration
- Provider configuration
- Docker image management
- Docker container creation
- Container configuration
- Port mapping
- Declarative infrastructure management

The project demonstrates the basic principles of Infrastructure as Code using Terraform.

---

## 8. Docker & NGINX Practice

Hands-on containerization and web server configuration.

### Technologies

- Docker
- NGINX
- Linux
- Networking

### Project

`docker-nginx-practice/`

### What I practiced

- Docker images
- Docker containers
- NGINX configuration
- Container networking
- Port mapping
- Service troubleshooting
- Linux-based web server configuration

---

## 9. systemd Practice

Linux service management and system administration exercises.

### Technologies

- Linux
- systemd
- Services
- Processes
- journalctl
- Logging

### Project

`systemd-practice/`

### What I practiced

- systemd services
- Service configuration
- Starting and stopping services
- Enabling services
- Service status checking
- journalctl
- Log analysis
- Troubleshooting Linux services

---

# CI/CD and GitHub Actions

The repository contains GitHub Actions workflows used to automate repository checks and Python testing.

### CI practice includes

- Automated workflow execution
- Python environment setup
- Dependency installation
- Unit test execution
- Repository checks
- Automated validation after Git pushes

The CI workflows demonstrate the basic principles of Continuous Integration and automated testing.

---

# Linux Administration Practice

The repository also contains practical Linux exercises covering:

- File and directory management
- Linux permissions
- Users and groups
- Processes
- Services
- Package management
- SSH
- Networking
- NGINX
- Apache
- systemd
- journalctl
- cron
- logrotate
- Bash scripting
- Backup automation
- Filesystem operations
- Troubleshooting

---

# Networking Practice

Networking labs cover fundamental Linux networking concepts:

- IPv4
- TCP/IP
- Network interfaces
- IP addressing
- Routing
- NAT
- IP forwarding
- DNS
- HTTP/HTTPS
- SSH
- Virtual networks
- iptables
- Network troubleshooting

Tools used during practice include:

- ip
- ping
- traceroute
- ss
- curl
- ssh
- scp
- tcpdump
- iptables

---

# Python Automation

Python is used in several practical automation projects in this repository.

The projects demonstrate:

- REST API integration
- JSON processing
- HTTP requests
- Unit testing
- Mocking
- Environment variables
- Filesystem automation
- ZIP archive processing
- Logging
- CLI arguments
- Error handling

---

# DevOps Technologies

The repository combines several areas of DevOps practice:

    Linux
       ↓
    Bash / Python
       ↓
    Git / GitHub
       ↓
    Docker / Docker Compose
       ↓
    NGINX
       ↓
    Kubernetes
       ↓
    Terraform
       ↓
    CI/CD / GitHub Actions

---

# Learning Focus

My current learning focus is building practical experience in:

1. Linux administration
2. Networking
3. Bash automation
4. Python automation
5. Docker and containerization
6. Kubernetes
7. Terraform / Infrastructure as Code
8. CI/CD
9. Cloud fundamentals
10. Troubleshooting
11. Automation
12. Infrastructure and operations

---

# DevOps Approach

My learning approach is:

    Learn
      ↓
    Build
      ↓
    Test
      ↓
    Troubleshoot
      ↓
    Fix
      ↓
    Verify
      ↓
    Document

I focus on understanding how systems work and developing practical troubleshooting and automation skills.

---

# Career Goal

I am building practical skills for a career as a:

- Junior DevOps Engineer
- Junior Cloud Engineer
- Cloud Operations Engineer
- Infrastructure Engineer
- Junior Site Reliability / Operations Engineer

I am particularly interested in Linux infrastructure, automation, containers, CI/CD and cloud technologies.

---

# Repository Structure

    linux-learning/
    │
    ├── .github/
    │   └── workflows/
    │
    ├── config/
    ├── docker-nginx-practice/
    ├── fflask-docker-app/
    ├── kubernetes/
    ├── permissions-practice/
    ├── python-api-testing/
    ├── python-archive-cleaner/
    ├── server/
    ├── systemd-practice/
    ├── terraform-docker/
    ├── transfer-tool/
    ├── src/
    ├── test_restore/
    │
    ├── backup.sh
    ├── myserver.sh
    ├── networking-practice.md
    ├── software-management.md
    ├── ssh-practice.md
    └── README.md

---

# About

This repository represents my practical Cloud and DevOps learning journey.

It contains hands-on labs, automation scripts and small projects covering Linux administration, networking, Python, Bash, Docker, Kubernetes, Terraform and CI/CD.

The repository is continuously updated as I learn and build new projects.
