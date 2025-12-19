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
├── requirements.txt
├── catalog-info.yaml
├── mkdocs.yaml
└── README.md
```

## Documentation

Full documentation is available in the `docs/` directory and can be viewed in Backstage TechDocs.

## License

[Add your license here]

