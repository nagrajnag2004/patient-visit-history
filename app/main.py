from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models
from app.routes import patients, visits


# Lifespan context manager: Runs once when the application starts and shuts down
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Auto-create MySQL tables if they do not exist
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Patient Visit History System API",
    description="A robust backend system to manage patient records and their medical visit history, built with FastAPI, SQLAlchemy, and MySQL.",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS (Cross-Origin Resource Sharing) for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route modules
app.include_router(patients.router)
app.include_router(visits.router)


@app.get("/", tags=["Root"])
def root():
    """
    Health check and entry point.
    """
    return {
        "status": "online",
        "message": "Patient Visit History API is running successfully!",
        "interactive_docs": "/docs",
        "alternative_docs": "/redoc"
    }

