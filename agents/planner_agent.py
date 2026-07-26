class PlannerAgent:
    """
    Planner Agent responsible for understanding
    user travel requests and creating structured
    tasks for other AI agents.
    """

    def __init__(self):
        self.name = "Planner Agent"

    def analyze_request(self, user_request):
        """
        Analyze the user's travel request
        and create structured messages
        for other agents.
        """

        message = {
            "sender": self.name,
            "user_request": user_request,

            "travel_details": {
                "destination": "Pallekele",
                "date": "Friday evening",
                "budget": 5000
            },

            "required_agents": [
                {
                    "agent": "Transport Agent",
                    "task": "Find the fastest and cheapest transportation method"
                },
                {
                    "agent": "Accommodation Agent",
                    "task": "Find budget accommodation options"
                }
            ]
        }

        return message


# Test the Planner Agent
if __name__ == "__main__":

    planner = PlannerAgent()

    user_request = """
    I want to visit Pallekele this Friday evening.
    I need a low budget hotel.
    My total budget is Rs.5000.
    """

    result = planner.analyze_request(user_request)

    print(result)