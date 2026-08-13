# Linux & DevOps Practice

> Hands-on Cloud & DevOps learning portfolio focused on Linux administration, automation, containerization, Infrastructure as Code and CI/CD.

This repository contains practical labs and projects completed during my Cloud & DevOps training and independent practice.

The projects cover Linux, Bash, Python, REST APIs, automated testing, Docker, Docker Compose, NGINX, Kubernetes, Terraform, networking and GitHub Actions.

---

## Technologies

| Category | Technologies |
|---|---|
| Operating Systems | Linux, Ubuntu |
| Scripting | Bash, Python |
| Version Control | Git, GitHub |
| Containers | Docker, Docker Compose |
| Orchestration | Kubernetes |
| Infrastructure as Code | Terraform, HCL |
| Web Servers | NGINX, Apache |
| Networking | TCP/IP, Routing, NAT, iptables |
| Remote Access | SSH, SCP |
| Linux Services | systemd, systemctl, journalctl |
| APIs | REST API, HTTP, JSON |
| Testing | unittest, unittest.mock |
| CI/CD | GitHub Actions |
| Virtualization | VirtualBox |

---

## Repository Structure

```text
linux-learning/
│
├── .github/
│   └── workflows/
│
├── config/
├── docker-nginx-practice/
├── flask-docker-app/
├── kubernetes/
├── permissions-practice/
├── python-api-testing/
├── python-archive-cleaner/
├── server/
├── src/
├── systemd-practice/
├── terraform-docker/
├── test_restore/
├── transfer-tool/
│
├── app.py
├── backup.sh
├── networking-practice.md
├── software-management.md
├── ssh-practice.md
└── README.md
```

---

# Projects & Labs

## 1. Python API Testing

**REST API integration and automated unit testing with Python.**

The project uses the GitHub Pull Requests API and demonstrates how to work with external APIs while keeping unit tests independent from real HTTP requests.

### Technologies

- Python
- Requests
- REST API
- JSON
- unittest
- unittest.mock
- GitHub API
- GitHub Actions

### What I practiced

- HTTP GET requests
- API response processing
- Request parameters
- Pagination
- Environment variables
- Bearer token authentication
- HTTP headers
- Mocking external requests
- Unit testing

### Testing

External HTTP requests are mocked with:

```python
unittest.mock.patch
```

The tests verify:

- successful API response processing
- empty API responses
- correct API endpoint
- correct request parameters
- HTTP headers
- Bearer token authentication

### Project structure

```text
python-api-testing/
├── handlers/
│   └── pull_requests.py
├── tests/
│   └── test_pull_requests.py
├── requirements.txt
└── README.md
```

[Open Python API Testing project](./python-api-testing)

---

## 2. Flask Docker Application

**Containerized Flask application integrated with the GitHub Pull Requests API.**

The project demonstrates how a Python web application can be packaged into a Docker image and executed as a container.

### Technologies

- Python
- Flask
- Docker
- Docker Compose
- REST API
- Git

### What I practiced

- Flask application structure
- Dockerfile creation
- Docker image building
- Python dependency installation
- Container execution
- Docker Compose
- Port mapping
- API integration

### Application flow

```text
Flask Application
        │
        ▼
GitHub API Handler
        │
        ▼
GitHub Pull Requests API
        │
        ▼
JSON Response
```

### Project structure

```text
flask-docker-app/
├── handlers/
│   └── pull_requests.py
├── Dockerfile
├── build.sh
├── docker-compose.yml
├── requirements.txt
└── start.py
```

[Open Flask Docker project](./flask-docker-app)

---

## 3. Python Archive Cleaner

**Python automation tool for cleaning ZIP archives.**

The script processes a ZIP archive, identifies directories that do not contain `__init__.py`, removes them and creates a new cleaned archive.

### Technologies

- Python
- os
- os.walk
- tempfile
- zipfile
- shutil
- logging

### What I practiced

- Command-line arguments
- Temporary directories
- ZIP archive processing
- File-system traversal
- Directory management
- Logging
- File creation
- Archive creation

### Processing flow

```text
ZIP archive
     │
     ▼
Temporary directory
     │
     ▼
Extract archive
     │
     ▼
Analyze directories
     │
     ▼
Find directories without __init__.py
     │
     ▼
Remove directories
     │
     ▼
Create cleaned.txt
     │
     ▼
Create new ZIP archive
```

### Main Python modules

```python
os
sys
tempfile
zipfile
shutil
logging
```

[Open Python Archive Cleaner](./python-archive-cleaner)

---

## 4. Bash Transfer Tool

**Command-line Bash utility for uploading and downloading files.**

The tool uses `curl` and `free.keep.sh` to transfer files from the command line.

### Technologies

- Bash
- curl
- Shell scripting
- Command-line tools

### Upload a file

```bash
./transfer.sh file.txt
```

### Upload multiple files

```bash
./transfer.sh file1.txt file2.txt
```

### Download a file

```bash
./transfer.sh -d ./downloads FILE_ID file.txt
```

### Show help

```bash
./transfer.sh -h
```

### Show version

```bash
./transfer.sh -v
```

### What I practiced

- Bash functions
- Variables
- Command-line arguments
- Flags
- `case`
- `readonly`
- `curl`
- File validation
- Error handling

[Open Bash Transfer Tool](./transfer-tool)

---

## 5. Linux Network Router Lab

**Practical Linux networking exercises using virtual machines.**

### Technologies

- Linux
- VirtualBox
- TCP/IP
- Routing
- NAT
- IP forwarding
- iptables

### What I practiced

- Network interfaces
- IP addresses
- Routing tables
- Packet forwarding
- NAT
- Linux firewall configuration
- Virtual machine networking
- Network troubleshooting

### Network concept

```text
Client VM
    │
    ▼
Linux Router
    │
    ├── IP forwarding
    ├── Routing
    ├── NAT
    └── iptables
    │
    ▼
External Network
```

[Open networking practice](./networking-practice.md)

---

## 6. Kubernetes Practice

**Hands-on Kubernetes deployment practice for a web application.**

### Technologies

- Kubernetes
- YAML
- Pods
- Deployments
- Services
- NGINX

### What I practiced

- Kubernetes Deployments
- Kubernetes Services
- YAML configuration
- Containerized applications
- Application exposure
- Basic Kubernetes operations

### Deployment concept

```text
Kubernetes
    │
    ▼
Deployment
    │
    ▼
Pod
    │
    ▼
Container
    │
    ▼
NGINX
    │
    ▼
Service
```

[Open Kubernetes project](./kubernetes)

---

## 7. Terraform + Docker

**Infrastructure as Code practice using Terraform and Docker.**

### Technologies

- Terraform
- Docker
- HCL
- Infrastructure as Code

### What I practiced

- Terraform configuration
- Docker resources
- Declarative infrastructure
- Infrastructure provisioning
- Terraform workflow
- Infrastructure as Code concepts

### Infrastructure flow

```text
Terraform configuration
          │
          ▼
      Terraform
          │
          ▼
     Docker provider
          │
          ▼
   Docker resources
```

[Open Terraform + Docker project](./terraform-docker)

---

## 8. Docker + NGINX Practice

**Practical containerization and web-server deployment using Docker and NGINX.**

### Technologies

- Docker
- NGINX
- Linux
- Docker Compose

### What I practiced

- Docker containers
- NGINX configuration
- Port mapping
- Container configuration
- Web-server deployment
- Container troubleshooting

---

## 9. ⚙️ systemd Practice

**Linux service management and troubleshooting using systemd.**

### Topics:

- systemd
- systemctl
- service management
- service startup
- journalctl
- Linux troubleshooting
```

[Open systemd practice](./systemd-practice)

---

## 10. Linux Permissions Practice

**Hands-on Linux exercises with users, groups, ownership and permissions.**

### Technologies

- Linux
- Bash
- File permissions

### What I practiced

- Users
- Groups
- File ownership
- `chmod`
- `chown`
- `umask`
- Access control

### Main commands

```bash
chmod
chown
umask
```

[Open permissions practice](./permissions-practice)

---

## 11. Linux Software Management

**Practical Linux package and software-management exercises.**

### Technologies

- Linux
- Ubuntu
- APT
- NGINX
- Apache

### What I practiced

- Package installation
- Package removal
- Package updates
- Package management
- Web-server installation
- Service troubleshooting

[Open software management practice](./software-management.md)

---

## 12. SSH Practice

**Practical SSH administration and secure remote-access exercises.**

### Technologies

- Linux
- SSH
- SCP
- Bash

### What I practiced

- SSH connections
- SSH keys
- SSH configuration
- Secure remote access
- File transfer with SCP

### SSH example

```bash
ssh user@host
```

### SCP example

```bash
scp file.txt user@host:/path/
```

[Open SSH practice](./ssh-practice.md)

---

## 13. Backup Automation

**Bash scripting practice for automated backup operations.**

### Technologies

- Bash
- Linux
- Shell scripting

### What I practiced

- Backup automation
- Command-line arguments
- File operations
- Hostname detection
- Error handling
- Shell scripting

[Open backup script](./backup.sh)

---

# CI/CD & GitHub Actions

The repository contains GitHub Actions workflows used to automate repository checks and Python testing.

### CI/CD workflow

```text
Git push
   │
   ▼
GitHub Actions
   │
   ▼
Checkout repository
   │
   ▼
Setup Python
   │
   ▼
Install dependencies
   │
   ▼
Run automated tests
   │
   ▼
Report result
```

### What I practiced

- GitHub Actions workflows
- YAML configuration
- Automated execution on push
- Python environment setup
- Dependency installation
- Automated testing
- Repository validation
- CI concepts

---

# DevOps Skills Demonstrated

## Linux

- Linux command line
- File-system management
- Users and groups
- Permissions
- SSH
- Networking
- Processes
- systemd
- Logs
- Package management

## Bash

- Shell scripting
- Automation
- Command-line tools
- Argument parsing
- Flags
- Error handling
- File operations

## Python

- Scripting
- Automation
- REST API integration
- JSON processing
- File-system automation
- Unit testing
- Mocking

## Docker

- Dockerfiles
- Images
- Containers
- Port mapping
- Docker Compose
- Application containerization

## Kubernetes

- Pods
- Deployments
- Services
- YAML configuration
- Container orchestration basics

## Terraform

- Infrastructure as Code
- Declarative configuration
- Docker resource management
- Infrastructure provisioning

## Networking

- TCP/IP
- IP addressing
- Routing
- NAT
- IP forwarding
- iptables
- Virtual machine networking

## CI/CD

- GitHub Actions
- Automated testing
- Workflow configuration
- Repository checks

---

# Learning Path

The repository follows a practical progression from Linux fundamentals to DevOps automation and infrastructure.

```text
Linux
  │
  ▼
Bash
  │
  ▼
Git / GitHub
  │
  ▼
Python
  │
  ▼
REST APIs
  │
  ▼
Unit Testing
  │
  ▼
Docker
  │
  ▼
Docker Compose
  │
  ▼
NGINX
  │
  ▼
Kubernetes
  │
  ▼
Terraform
  │
  ▼
CI/CD
  │
  ▼
Cloud / DevOps
```

---

# Goal

The goal of this repository is to demonstrate practical skills required for a **Junior DevOps / Cloud Engineer** role.

The main focus areas are:

- Linux administration
- Bash automation
- Python automation
- REST APIs
- Automated testing
- Docker
- Docker Compose
- Kubernetes
- Terraform
- Infrastructure as Code
- Networking
- CI/CD
- GitHub Actions

The projects are based on hands-on tasks rather than only theoretical study.

---

# Training & Practice

This repository is part of my practical Cloud & DevOps learning journey.

The labs are designed to build practical experience with:

```text
Operating Systems
       │
       ▼
Automation
       │
       ▼
Programming
       │
       ▼
Containers
       │
       ▼
Infrastructure
       │
       ▼
Orchestration
       │
       ▼
CI/CD
```

---

# Author

**Vladimir Poliakov**

Junior DevOps / Cloud Engineer

`Linux` · `Bash` · `Python` · `Docker` · `Kubernetes` · `Terraform` · `CI/CD`
