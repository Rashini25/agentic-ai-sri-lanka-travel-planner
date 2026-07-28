from agents.llm_service import openrouter_chat



class RecommendationAgent:
    """
    Recommendation Agent creates the final travel plan
    by combining outputs from all specialized agents.
    """



    def __init__(self):

        self.name = "Recommendation Agent"



    def process_request(self, planner_data):


        destination = planner_data.get(
            "destination",
            "Sri Lanka"
        )


        prompt = f"""

You are a professional Sri Lankan travel planning assistant.

Create a personalized travel plan for the user.

Follow these strict rules:

- Only use the provided information.
- Focus ONLY on the requested destination.
- Do not mention other cities or destinations.
- Do not create fake hotels.
- Do not create fake prices.
- Do not add unrelated attractions.
- Do not start with greetings.
- Do not mention AI agents.
- Do not add closing messages.
- Do not say "Happy travels".
- Keep the answer concise and professional.



Requested Destination:

{destination}



Retrieved Destination Knowledge (RAG):

{planner_data.get("travel_information")}



User Preferences:

{planner_data.get("preference_information")}



Budget Information:

{planner_data.get("budget_information")}



Transportation Options:

{planner_data.get("transport_information")}



Accommodation Options:

{planner_data.get("accommodation_information")}



Weather Information:

{planner_data.get("weather_information")}



Itinerary Information:

{planner_data.get("itinerary_information")}



Generate the response exactly using this format:



# {destination} Travel Plan


## Transportation

Recommended option:

Estimated cost:

Why it suits the traveller:


## Accommodation

Recommended place:

Price:

Location:


## Suggested Itinerary


Day 1:
- 


Day 2:
- 



## Food & Cultural Experiences

- 



## Estimated Budget

Transportation:

Accommodation:

Activities:

Approximate total:


## Travel Tips

- 



Do not add anything before or after this format.

"""



        response = openrouter_chat(prompt)



        return {


            "sender": self.name,


            "received_from": "Planner Agent",


            "destination": destination,


            "final_recommendation": response.strip()


        }





if __name__ == "__main__":


    agent = RecommendationAgent()


    result = agent.process_request(

        {

            "destination":"Ratnapura",

            "preference_information":{

                "travel_style":"Cultural",

                "interests":[

                    "Food",

                    "Culture"

                ]

            },


            "budget_information":{

                "available_budget":8000

            }

        }

    )


    print(result)