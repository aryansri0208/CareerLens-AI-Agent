from typing import Dict, List

class SimulationAgent:
    def __init__(self):
        self.current_job = None
        self.user_profile = None

    async def generate_daily_tasks(self, job_title: str, user_profile: Dict) -> List[Dict]:
        # TODO: Generate job-specific tasks
        return [
            {
                "task_id": "1",
                "description": "Sample task",
                "context": "Work scenario",
                "expected_output": "Expected response"
            }
        ]

    async def evaluate_response(self, task_id: str, user_response: str) -> Dict:
        # TODO: Evaluate user's task response
        return {
            "score": 0.0,
            "feedback": "",
            "areas_of_improvement": []
        } 