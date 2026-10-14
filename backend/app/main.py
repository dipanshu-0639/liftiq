from fastapi import FastAPI

app = FastAPI(
    title="LiftIQ API",
    description="Strength Progression and Plateau Detection",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to LiftIQ API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "liftiq-backend",
    }
