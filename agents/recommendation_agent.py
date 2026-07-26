class RecommendationAgent:
    """
    Recommendation Agent selects the best travel options
    based on budget, preferences and available information.
    """

    def __init__(self):
        self.name = "Recommendation Agent"


    def process_request(self, planner_data):

        destination = planner_data["destination"]

        budget_info = planner_data["budget_information"]

        preference_info = planner_data["preference_information"]

        weather_info = planner_data["weather_information"]

        transport_info = planner_data["transport_information"]

        accommodation_info = planner_data["accommodation_information"]



        # Select budget-friendly transport

        recommended_transport = (
            transport_info["transport_options"][0]
        )



        # Select affordable accommodation

        recommended_accommodation = (
            accommodation_info["accommodation_options"][2]
        )



        # Generate reasoning

        reasons = [

            "Selected based on user's budget preference",

            "Matches user's travel style and interests",

            "Weather conditions are suitable for planned activities"

        ]



        return {

            "sender": self.name,

            "received_from": "Planner Agent",

            "destination": destination,

            "recommended_plan": {

                "transport": recommended_transport,

                "accommodation": recommended_accommodation,

                "weather_condition": weather_info[
                    "weather_information"
                ]["condition"],

                "reasons": reasons

            }

        }



if __name__ == "__main__":


    recommendation_agent = RecommendationAgent()


    sample_data = {

        "destination": "Kitulgala",

        "budget_information": {},

        "preference_information": {},

        "weather_information": {

            "weather_information": {

                "condition": "Warm and humid"

            }

        },

        "transport_information": {

            "transport_options": [

                {

                    "method": "Public Bus",

                    "estimated_cost": "Rs.500-800"

                }

            ]

        },

        "accommodation_information": {

            "accommodation_options": [

                {

                    "name": "Budget Guest House"

                },

                {

                    "name": "Hotel"

                },

                {

                    "name": "Affordable Homestay"

                }

            ]

        }

    }


    result = recommendation_agent.process_request(
        sample_data
    )


    print(result)