# Kubernetes Nginx Deployment

Hands-on Kubernetes practice focused on application deployment and basic container orchestration.

The project contains a Kubernetes Deployment manifest for running an Nginx-based web application.

## Technologies

- Kubernetes
- Docker
- Nginx
- YAML
- kubectl
- Linux

## Current Deployment

The Kubernetes manifest creates a Deployment named `my-web-app`.

The current configuration uses:

- Kubernetes API version: `apps/v1`
- Resource type: `Deployment`
- Deployment name: `my-web-app`
- Replicas: `6`
- Application label: `app: web`
- Container name: `nginx`
- Container image: `nginx:1.21`
- Container port: `80`

## Architecture

```text
Kubernetes Cluster
        |
        v
Deployment: my-web-app
        |
        +---- Pod 1 ---- Nginx :80
        |
        +---- Pod 2 ---- Nginx :80
        |
        +---- Pod 3 ---- Nginx :80
        |
        +---- Pod 4 ---- Nginx :80
        |
        +---- Pod 5 ---- Nginx :80
        |
        +---- Pod 6 ---- Nginx :80
```

The Deployment uses labels and selectors to associate the Pods with the Deployment.

## Deployment Manifest

The current manifest is stored in:

```text
app-deployment.yaml
```

It defines a Kubernetes Deployment with six Nginx replicas.

## How to Deploy

Make sure a Kubernetes cluster is available and `kubectl` is configured.

Check the cluster:

```bash
kubectl cluster-info
```

Check available nodes:

```bash
kubectl get nodes
```

Apply the Deployment:

```bash
kubectl apply -f app-deployment.yaml
```

Check the Deployment:

```bash
kubectl get deployment
```

Check Pods:

```bash
kubectl get pods
```

Get more detailed information:

```bash
kubectl describe deployment my-web-app
```

Check individual Pods:

```bash
kubectl describe pod <pod-name>
```

## Verification

Check whether all replicas are running:

```bash
kubectl get pods -o wide
```

Check the Deployment status:

```bash
kubectl get deployment my-web-app
```

The expected result is six Pods managed by the Deployment.

## Troubleshooting Workflow

The project is also used to practice a structured Kubernetes troubleshooting workflow.

```text
Application problem
        ↓
Check Pods
        ↓
kubectl get pods
        ↓
Inspect Pod status
        ↓
kubectl describe pod
        ↓
Check container logs
        ↓
kubectl logs
        ↓
Check Deployment
        ↓
kubectl describe deployment
        ↓
Check events
        ↓
kubectl get events
        ↓
Identify root cause
        ↓
Apply fix
        ↓
Verify application availability
```

Useful commands:

```bash
kubectl get pods
kubectl get pods -o wide
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl get deployment
kubectl describe deployment my-web-app
kubectl get events
```

## Scaling

The Deployment can be scaled using:

```bash
kubectl scale deployment my-web-app --replicas=3
```

Check the result:

```bash
kubectl get pods
```

The original configuration can then be restored:

```bash
kubectl scale deployment my-web-app --replicas=6
```

## Cleanup

Remove the Deployment:

```bash
kubectl delete -f app-deployment.yaml
```

Verify that the Pods have been removed:

```bash
kubectl get pods
```

## Learning Goals

This project is intended to practice:

- Kubernetes Deployments
- Pod management
- Replica configuration
- Labels and selectors
- Container configuration
- Application deployment
- Basic Kubernetes troubleshooting
- kubectl commands
- Scaling applications

## Next Practice Steps

The next stage of the laboratory will extend this Deployment with:

- a Kubernetes Service
- application access from outside the Pod
- health checks
- resource configuration
- intentional failure scenarios
- troubleshooting and root-cause analysis
- deployment verification
- basic application operations

## Disclaimer

This is a personal learning and laboratory project.

The repository demonstrates hands-on learning and experimentation and is not intended to represent a production Kubernetes deployment.
