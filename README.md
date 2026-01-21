# Secure docker python production template

This repository shows a **real-world, production-grade Docker image strategy** used by DevOps teams.
The goal is to show how the **same application** can be packaged differently for **development, staging, and production**
with a strong focus on **security, image size, reproducibility, and best practices**.

---

## What This Project Demonstrates

- Proper Docker image versioning
- Multi-stage builds
- Environment separation (dev / staging / prod)
- Image size optimization
- Security hardening
- Non-root containers
- Read-only filesystems
- Healthchecks
- Centralized logging (stdout)
- Vulnerability scanning with Trivy
- Clean GitHub-ready structure

---

## Images Overview
Same application, different size
| Environment | Image Name | Tag | Size |
|------------|-----------|-----|------|
| Development | docker-prod-image-dev | v1.0.0 | ~1.62GB |
| Staging | docker-prod-image-staging | v1.0.0 | ~184MB |
| Production | docker-prod-image-prod | v1.0.0 | ~184MB |

### Why are sizes different?

- **dev**
  - Includes full Python image
  - Build tools
  - Source code
  - Designed for debugging and iteration

- **staging**
  - Multi-stage build
  - Only runtime dependencies
  - Close to production but still flexible

- **prod**
  - Multi-stage build
  - Minimal runtime
  - Increased security
---

## 📂 Project Structure

```text
.
├── app/
│   ├── main.py              # Flask application
│   └── requirements.txt     # Python dependencies
├── docker/
│   ├── Dockerfile.dev       # Development image
│   ├── Dockerfile.staging   # Staging image
│   └── Dockerfile.prod      # Production image
├── .github
│   └── workflows
│       └── docker-ci.yml
├── docker-compose.yml       # Orchestration for dev / staging / prod
├── .dockerignore            # Exclude unnecessary files from images
└── README.md
```


## Running the Project

### Build all images
```bash
docker compose build
```

### Run all environments
```bash
docker compose up
```


## Service Endpoints

| Environment | URL |
|------------|-----------| 
| dev | http://localhost:8081 |
| Staging | http://localhost:8082 | 
| prod | http://localhost:8083|


## Application Routes
| Endpoint | Description |
|------------|-----------| 
| / |Returns welcome message and environment |
| /health | Healthcheck endpoint | 
| /info | Runtime and version information|


#### Docker automatically tracks container health status.

### Production Security Hardening

What this means:

Root filesystem is read-only

Temporary files exist only in memory

All Linux capabilities are removed

Container runs as non-root user

Reduced attack surface

Safer default posture

### Logging Strategy

Logs are written to stdout

Compatible with: Docker logs, Kubernetes, ELK stack, Cloud logging systems


### Vulnerability Scanning with Trivy

Trivy is used to scan container images for vulnerabilities.
```bash
ubuntu@lab:~/secure-docker-python-production-template$ bash security/trivy-scan.sh 
```

What Trivy detects:

OS-level CVEs, Python dependency vulnerabilities, Misconfigurations, Secrets