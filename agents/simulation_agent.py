import json
from typing import Dict, List

class SimulationAgent:
    def __init__(self):
        with open("data/job_profiles.json", "r") as f:
            self.job_profiles = json.load(f)

    async def generate_daily_tasks(self, job_title: str, user_profile: Dict) -> List[Dict]:
        tasks = self.job_profiles.get(job_title, {}).get("tasks", [])
        return [
            {
                "task_id": str(i + 1),
                "description": task,
                "context": f"{job_title} simulation",
                "expected_output": "Your best attempt"
            }
            for i, task in enumerate(tasks[:3])
        ]

    async def evaluate_response(self, task_id: str, user_response: str) -> Dict:
        # Placeholder scoring
        return {
            "score": 0.7,
            "feedback": "Good try!",
            "areas_of_improvement": ["Be more concise", "Add structure"]
        }
