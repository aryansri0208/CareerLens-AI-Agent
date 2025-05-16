from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from agents.simulation_agent import SimulationAgent
from agents.intake_agent import IntakeAgent


app = FastAPI(title="CareerLens AI Agent")
simulation_agent = SimulationAgent()

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

class SimulationRequest(BaseModel):
    profile: UserProfile

class TaskResponseRequest(BaseModel):
    task_id: str
    user_response: str
    profile: UserProfile

@app.get("/")
async def root():
    return {"message": "Welcome to CareerLens AI git Agent"}

@app.post("/intake")
async def user_intake(profile: UserProfile):
    # TODO: Connect with intake agent
    return {"status": "success", "profile": profile}

@app.post("/simulate/{job_title}")
async def simulate_job(job_title: str, req: SimulationRequest):
    tasks = await simulation_agent.generate_daily_tasks(job_title, req.profile.dict())
    return {"status": "success", "tasks": tasks}

@app.post("/compare")
async def compare_jobs(job1: str, job2: str):
    # TODO: Connect with comparison agent
    return {"status": "success", "comparison": {"job1": job1, "job2": job2}}

@app.post("/evaluate")
async def evaluate_task_response(request: TaskResponseRequest):
    result = await simulation_agent.evaluate_response(
        request.task_id,
        request.user_response,
        request.profile.dict()
    )
    return {"status": "success", "result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
#hi
#hiii