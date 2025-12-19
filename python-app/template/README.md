# ${{ values.component_id }}

${{ values.description }}

## Quick Start

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
uvicorn src.${{ values.component_id | replace('-', '_') }}.main:app --reload
```

Visit `http://localhost:8000/docs` for interactive API documentation.

### Run Tests

```bash
pytest
```

## Project Structure

```
.
├── src/
│   └── ${{ values.component_id | replace('-', '_') }}/
│       ├── __init__.py
│       ├── main.py
│       └── api/
│           ├── __init__.py
│           └── routes.py
├── tests/
│   └── test_main.py
├── docs/
│   └── index.md
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── requirements.txt
├── catalog-info.yaml
├── mkdocs.yaml
├── Dockerfile
└── README.md
```

## Kubernetes Deployment

The project includes Kubernetes manifests in the `k8s/` directory:

- **deployment.yaml**: Kubernetes Deployment with configurable resources, probes, and replicas
- **service.yaml**: Kubernetes Service exposing the application

### Deploy to Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

The deployment includes:
- Health checks using the `/health` endpoint
- Configurable CPU and memory resources
- Liveness and readiness probes
- Environment-specific configuration

## Documentation

Full documentation is available in the `docs/` directory and can be viewed in Backstage TechDocs.

## License

[Add your license here]

