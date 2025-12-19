"""API routes for ${{ values.component_id }}."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def api_root():
    """API root endpoint."""
    return {"message": "${{ values.component_id }} API", "version": "0.1.0"}


@router.get("/items")
async def get_items():
    """Get items endpoint."""
    return {"items": []}


