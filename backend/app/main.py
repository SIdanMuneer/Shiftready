from fastapi import FastAPI

app =  FastAPI(
    title = "ShiftReady API",
    description="AI-assisted workforce onboarding system",
    version="0.1.0"
)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "shiftready-api",
    }