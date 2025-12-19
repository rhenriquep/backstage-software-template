# ${{ values.component_id }}

${{ values.description }}

## Overview

This is a FastAPI service generated from the Python FastAPI template.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
uvicorn src.${{ values.component_id | replace('-', '_') }}.main:app --reload
```

The API will be available at `http://localhost:8000`.

### API Documentation

Once the application is running, you can access:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### Health Check

```http
GET /health
```

Returns the health status of the service.

### Root

```http
GET /
```

Returns a welcome message.

### API Root

```http
GET /api/v1/
```

Returns API information.

## Development

### Running Tests

```bash
pytest
```

### Project Structure

```
src/
└── ${{ values.component_id | replace('-', '_') }}/
    ├── __init__.py
    ├── main.py          # FastAPI application
    └── api/
        ├── __init__.py
        └── routes.py    # API routes

tests/
└── test_main.py         # Test suite
```

## Docker

Build and run with Docker:

```bash
docker build -t ${{ values.component_id }} .
docker run -p 8000:8000 ${{ values.component_id }}
```

## Kubernetes Deployment

The project includes Kubernetes manifests in the `k8s/` directory for easy deployment.

### Deployment Configuration

The Kubernetes deployment includes:

- **Health Probes**: Liveness and readiness probes using the `/health` endpoint on port 8000
- **Resource Limits**: Configurable CPU and memory requests/limits
- **Replicas**: Configurable number of replicas
- **Namespace**: Configurable Kubernetes namespace

### Deploy to Kubernetes

```bash
# Apply deployment
kubectl apply -f k8s/deployment.yaml

# Apply service
kubectl apply -f k8s/service.yaml

# Check deployment status
kubectl get deployment ${{ values.component_id }} -n ${{ values.namespace }}

# Check service
kubectl get service ${{ values.component_id }} -n ${{ values.namespace }}
```

### Kubernetes Manifests

- **k8s/deployment.yaml**: Defines the Deployment with:
  - Container image configuration
  - Resource requests and limits
  - Health probes (liveness and readiness)
  - Environment variables
  - Port configuration (8000)

- **k8s/service.yaml**: Defines the Service with:
  - ClusterIP type
  - Port mapping (80 -> 8000)
  - Selector for the deployment

## Contributing

Please follow the project's coding standards and submit pull requests for any improvements.

