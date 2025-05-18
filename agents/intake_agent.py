from typing import Dict, List, Optional
from datetime import datetime

#gathers basic profile info
class IntakeAgent:
    def __init__(self):
        # Core interview questions
        self.questions = [
            {
                "id": "degree",
                "question": "What is your highest degree and field of study?",
                "required": True
            },
            {
                "id": "experience",
                "question": "How many years of professional experience do you have?",
                "required": True
            },
            {
                "id": "interests",
                "question": "What type of work interests you the most?",
                "required": True
            },
            {
                "id": "target_jobs",
                "question": "Which specific roles are you interested in exploring?",
                "required": True
            }
        ]

    async def conduct_interview(self, initial_data: Dict) -> Dict:
        """
        Conducts the interview process and checks for missing information.
        """
        profile_data = initial_data.copy()
        missing_info = self._identify_missing_information(profile_data)
        
        if missing_info:
            # Generate follow-up questions for missing required information
            follow_ups = self._generate_follow_up_questions(missing_info)
            return {
                "status": "incomplete",
                "follow_up_questions": follow_ups,
                "partial_profile": profile_data
            }
        
        # If all required info is present, build the profile
        complete_profile = await self.build_profile(profile_data)
        return {
            "status": "complete",
            "profile": complete_profile
        }

    async def build_profile(self, interview_responses: Dict) -> Dict:
        """
        Creates a structured profile from interview responses.
        """
        return {
            "user_id": f"user_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "created_at": datetime.now().isoformat(),
            "degree": interview_responses.get("degree", ""),
            "experience": interview_responses.get("experience", ""),
            "interests": interview_responses.get("interests", []),
            "target_jobs": interview_responses.get("target_jobs", [])
        }

    def _identify_missing_information(self, profile_data: Dict) -> List[str]:
        """
        Identifies which required fields are missing.
        """
        missing = []
        for question in self.questions:
            if question["required"] and not profile_data.get(question["id"]):
                missing.append(question["id"])
        return missing

    def _generate_follow_up_questions(self, missing_fields: List[str]) -> List[Dict]:
        """
        Creates follow-up questions for missing fields.
        """
        follow_ups = []
        for question in self.questions:
            if question["id"] in missing_fields:
                follow_ups.append({
                    "id": question["id"],
                    "question": question["question"]
                })
        return follow_ups 

