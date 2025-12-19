"""Main application entry point for ${{ values.component_id }}."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ${{ values.component_id | replace('-', '_') }}.api import routes

app = FastAPI(
    title="${{ values.component_id }}",
    description="${{ values.description }}",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes.router, prefix="/api/v1", tags=["api"])


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to ${{ values.component_id }}",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}

