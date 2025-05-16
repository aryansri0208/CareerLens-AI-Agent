from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="CareerLens AI Agent")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserProfile(BaseModel):
    degree: str
    experience: Optional[str]
    interests: List[str]
    target_jobs: List[str]

@app.get("/")
async def root():
    return {"message": "Welcome to CareerLens AI Agent"}

@app.post("/intake")
async def user_intake(profile: UserProfile):
    # TODO: Connect with intake agent
    return {"status": "success", "profile": profile}

@app.post("/simulate/{job_title}")
async def simulate_job(job_title: str):
    # TODO: Connect with simulation agent
    return {"status": "success", "job": job_title}

@app.post("/compare")
async def compare_jobs(job1: str, job2: str):
    # TODO: Connect with comparison agent
    return {"status": "success", "comparison": {"job1": job1, "job2": job2}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
#hi