class PreferenceAgent:
    """
    Preference Agent responsible for analyzing
    user travel preferences.
    """

    def __init__(self):
        self.name = "Preference Agent"

    def process_request(self, user_request):

        budget_type = user_request.get("budget_type", "Medium")
        travel_style = user_request.get("travel_style", "General")
        interests = user_request.get("interests", [])

        response = {
            "sender": self.name,

            "preferences": {
                "budget_type": budget_type,
                "travel_style": travel_style,
                "interests": interests
            },

            "recommendations": []
        }


        # Generate recommendations based on preferences

        if "Adventure" in interests:
            response["recommendations"].append(
                "Consider adventure destinations such as Kitulgala"
            )

        if "Beach" in interests:
            response["recommendations"].append(
                "Consider coastal destinations such as Mirissa or Bentota"
            )

        if budget_type == "Low":
            response["recommendations"].append(
                "Prefer budget accommodation and public transportation"
            )


        return response



if __name__ == "__main__":

    preference_agent = PreferenceAgent()


    user_request = {
        "budget_type": "Low",
        "travel_style": "Adventure",
        "interests": [
            "Adventure",
            "Nature"
        ]
    }


    result = preference_agent.process_request(
        user_request
    )


    print(result)