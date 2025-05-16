import json
from typing import Dict, List
from utils.scoring import calculate_job_fit_score, generate_feedback_report


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

    async def evaluate_response(self, task_id: str, user_response: str, user_profile: Dict) -> Dict:
        user_skills = user_profile.get("skills", [])

        # Step 1: Try to find the job from user profile's target_jobs
        job_title = user_profile.get("target_jobs", [])[0]  # assuming one job for now
        job_data = self.job_profiles.get(job_title)

        if not job_data:
            return {
                "score": 0.0,
                "feedback": "Unknown job title.",
                "areas_of_improvement": ["Please select a valid job"]
            }

        required_skills = job_data.get("required_skills", [])

        # Step 2: Score user skills against job requirements
        score = calculate_job_fit_score(
            {"skills": user_skills},
            {"required_skills": required_skills}
        )

        # Step 3: Generate feedback
        feedback = generate_feedback_report({
            "score": score,
            "response": user_response
        })

        return feedback


