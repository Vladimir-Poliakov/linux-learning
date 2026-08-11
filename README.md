# Linux & DevOps Learning Lab

Hands-on Linux and DevOps practice focused on system administration,
networking, troubleshooting, containerization, Kubernetes and Infrastructure as Code.

This repository contains practical labs and configuration examples built while
developing Linux, DevOps and Cloud Engineering skills.

## Skills Practiced

- Linux system administration
- Bash scripting
- Python automation
- Networking and troubleshooting
- TCP/IP, routing and NAT
- iptables and firewall rules
- SSH and remote access
- systemd and service management
- Log analysis with journalctl
- Docker and Nginx
- Kubernetes fundamentals
- Terraform with Docker
- Git and GitHub
- Virtualization with VirtualBox

---

## Repository Structure

### Networking

`networking-practice.md`

Practical Linux networking exercises covering:

- static IP configuration
- routing
- IP forwarding
- NAT
- iptables
- connectivity testing
- network troubleshooting

### Kubernetes

`kubernetes/`

Kubernetes deployment practice using an Nginx container.

The current manifest demonstrates:

- Kubernetes Deployment
- replica configuration
- pod labels and selectors
- container configuration
- container ports
- Nginx image deployment

### Terraform + Docker

`terraform-docker/`

Infrastructure as Code practice using Terraform and the Docker provider.

The configuration demonstrates:

- Terraform provider configuration
- Docker image management
- Docker container creation
- port mapping
- declarative infrastructure configuration

### Docker + Nginx

`docker-nginx-practice/`

Containerization practice with Docker and Nginx.

### systemd

`systemd-practice/`

Practice with Linux services and systemd, including custom service configuration
and automatic service startup.

### Permissions

`permissions-practice/`

Linux users, groups, permissions and filesystem access control.

### SSH

`ssh-practice.md`

Practice with SSH configuration and remote Linux access.

### Linux Logs & Troubleshooting

`journalctl-nginx.md`

Practice with system logs and service troubleshooting using journalctl.

### Bash & Automation

Examples of Bash scripts for:

- file operations
- backups
- system tasks
- automation
- command execution
- error handling

### Python

Python scripts for practical automation and system-related tasks.

---

## Linux Network Lab

The repository includes a small Linux network lab built with VirtualBox.

### Architecture

```text
              Internet
                  |
              server1
          Router / NAT
             /      \
        client1    client2
