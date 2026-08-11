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

server1 acts as a router and provides NAT and packet forwarding for the internal network.

### Technologies

Ubuntu Linux
VirtualBox
Netplan
iptables
TCP/IP

### Configuration

Enable IP forwarding:

echo 1 > /proc/sys/net/ipv4/ip_forward

Configure NAT:

iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE

Configure forwarding:

iptables -A FORWARD -i enp0s8 -o enp0s3 -j ACCEPT

iptables -A FORWARD -i enp0s3 -o enp0s8 -m state --state RELATED,ESTABLISHED -j ACCEPT

### Verification

- Connectivity between internal clients
- Internet access through the router
- Routing and forwarding behaviour

The labs are also used to practice a structured troubleshooting workflow:

Problem
   ↓
Check symptoms
   ↓
Check system status
   ↓
Inspect logs
   ↓
Check networking
   ↓
Identify root cause
   ↓
Apply fix
   ↓
Verify service availability
   ↓
Document the solution

### Typical Linux tools used during troubleshooting:

systemctl
journalctl
ps
top
htop
df
du
ip
ss
ping
traceroute
curl
ssh
tcpdump

### DevOps & Cloud Roadmap

The repository is continuously expanded with practical labs covering:

Linux administration
Networking
Containers
Kubernetes
Infrastructure as Code
Cloud fundamentals
Monitoring
Automation
CI/CD

The goal is to build practical skills for Junior Cloud Engineer, Cloud Operations and Junior DevOps roles.

### Learning Approach

The focus of this repository is hands-on practice.

### Typical workflow:

Learn
  ↓
Build
  ↓
Test
  ↓
Break
  ↓
Troubleshoot
  ↓
Fix
  ↓
Document

The labs are designed to practice not only configuration, but also troubleshooting and operational thinking.

### Disclaimer

This is a personal learning and laboratory repository.

The projects are intended to demonstrate hands-on learning, experimentation and practical understanding rather than production experience.
