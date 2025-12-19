"""Tests for the main application."""

import pytest
from fastapi.testclient import TestClient

from ${{ values.component_id | replace('-', '_') }}.main import app

client = TestClient(app)


def test_root():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_api_root():
    """Test API root endpoint."""
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert "message" in response.json()

