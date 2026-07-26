from agents.llm_service import openrouter_chat



class RecommendationAgent:
    """
    Recommendation Agent generates the final travel recommendation
    using OpenRouter LLM reasoning based on outputs from other agents.
    """


    def __init__(self):

        self.name = "Recommendation Agent"



    def process_request(self, planner_data):


        destination = planner_data["destination"]



        # Prepare prompt for OpenRouter reasoning model

        prompt = f"""

You are an expert Sri Lankan travel recommendation assistant.

Create the best travel plan based on the information provided by different AI agents.

Destination:
{destination}


User Preference Information:
{planner_data.get("preference_information")}


Budget Information:
{planner_data.get("budget_information")}


Weather Information:
{planner_data.get("weather_information")}


Transportation Information:
{planner_data.get("transport_information")}


Accommodation Information:
{planner_data.get("accommodation_information")}


Itinerary Information:
{planner_data.get("itinerary_information")}



Generate a clear travel recommendation.

Your response should include:

1. Recommended transportation method
2. Recommended accommodation
3. Recommended activities
4. Budget suitability
5. Weather consideration
6. Reasons for your recommendation


Write the answer in a friendly way suitable for a traveller.

"""



        # Use OpenRouter for reasoning

        ai_response = openrouter_chat(prompt)



        return {


            "sender": self.name,


            "received_from": "Planner Agent",


            "destination": destination,


            "final_recommendation": ai_response

        }





if __name__ == "__main__":


    recommendation_agent = RecommendationAgent()



    sample_data = {


        "destination": "Kitulgala",


        "preference_information": {

            "budget_type": "Low",

            "travel_style": "Adventure",

            "interests": [

                "Nature",

                "Adventure"

            ]

        },


        "budget_information": {

            "available_budget": 5000,

            "estimated_cost": 5000

        },


        "weather_information": {

            "weather_information": {

                "condition": "Warm and humid",

                "temperature": "25°C - 30°C"

            }

        },


        "transport_information": {


            "transport_options": [

                {

                    "method": "Public Bus",

                    "estimated_cost": "Rs.500-800"

                },

                {

                    "method": "Taxi",

                    "estimated_cost": "Rs.4000-5000"

                }

            ]

        },


        "accommodation_information": {


            "accommodation_options": [

                {

                    "name": "Budget Guest House",

                    "price_per_night": 2500

                },

                {

                    "name": "Affordable Homestay",

                    "price_per_night": 2000

                }

            ]

        },


        "itinerary_information": {


            "itinerary": [

                {

                    "day": 1,

                    "activities": [

                        "Visit Kelani River",

                        "Explore rainforest"

                    ]

                }

            ]

        }

    }



    result = recommendation_agent.process_request(
        sample_data
    )



    print(result)