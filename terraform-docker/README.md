# Terraform + Docker Nginx

Hands-on Infrastructure as Code practice using Terraform and the Docker provider.

The project demonstrates how Terraform can be used to declaratively manage a Docker image and container.

## Architecture

```text
Terraform
    |
    v
Docker Provider
    |
    +----> nginx:latest
    |
    v
Docker Container
    |
    +----> container port 80
              |
              v
        host port 8080
```

## Technologies

- Terraform
- Docker
- Nginx
- Infrastructure as Code
- Git

## What This Project Demonstrates

- Terraform provider configuration
- Docker provider usage
- Declarative infrastructure configuration
- Docker image management
- Docker container creation
- Container port mapping
- Basic Infrastructure as Code workflow

## Configuration

The Terraform configuration uses the Docker provider.

The project pulls the Nginx Docker image and creates a Docker container.

The container exposes port 80 and maps it to port 8080 on the host.

```text
localhost:8080
        |
        v
Docker container
        |
        v
Nginx :80
```

## How to Run

Make sure Docker and Terraform are installed.

Initialize Terraform:

```bash
terraform init
```

Validate the configuration:

```bash
terraform validate
```

Review the planned changes:

```bash
terraform plan
```

Apply the configuration:

```bash
terraform apply
```

Confirm the deployment when prompted.

Check the running container:

```bash
docker ps
```

Test Nginx:

```bash
curl http://localhost:8080
```

Or open the following address in a browser:

```text
http://localhost:8080
```

## Troubleshooting

Typical troubleshooting workflow:

```text
Check Terraform configuration
        ↓
terraform validate
        ↓
terraform plan
        ↓
Check Docker status
        ↓
docker ps
        ↓
Check container logs
        ↓
docker logs terraform-nginx
        ↓
Check port availability
        ↓
curl http://localhost:8080
```

Useful commands:

```bash
terraform validate
terraform plan
terraform apply
terraform destroy

docker ps
docker logs terraform-nginx
docker inspect terraform-nginx
curl http://localhost:8080
```

## Cleanup

To remove the infrastructure created by Terraform:

```bash
terraform destroy
```

## Learning Goal

This is a personal learning project created to practice Infrastructure as Code and understand how Terraform can declaratively manage containerized applications.

The project is intended for learning and experimentation rather than production use.
