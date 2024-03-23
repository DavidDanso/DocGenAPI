# Import required modules and components
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import app_settings
from .preview import router as preview_router
from .download import router as download_router

# Create a FastAPI application instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

###################### INCLUDE ROUTERS * #####################

# Import and include the routers defined in the respective modules into the FastAPI application

# Include the 'preview' router for preview-related endpoints
app.include_router(preview_router)

# Include the 'download' router for download-related endpoints
app.include_router(download_router)

# Define a root endpoint that responds to HTTP GET requests at the base URL ("/")

@app.get("/")
def read_root():
    return {"response": "doc template with fastapi and jinja2"}

