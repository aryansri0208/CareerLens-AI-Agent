from typing import Dict, List
#gathers basic profile info
class IntakeAgent:
    def __init__(self):
        self.questions = [
            "What is your highest degree and field of study?",
            "What are your favorite courses or subjects?",
            "What technical skills do you possess?",
            "Which careers are you most interested in exploring?"
        ]

    async def conduct_interview(self, initial_data: Dict) -> Dict:
        # TODO: Implement GPT-based interview logic
        return {
            "profile": initial_data,
            "recommendations": [],
            "next_steps": []
        }

    async def build_profile(self, interview_responses: Dict) -> Dict:
        # TODO: Process responses into structured profile
        return {
            "skills": [],
            "interests": [],
            "potential_fits": []
        } 