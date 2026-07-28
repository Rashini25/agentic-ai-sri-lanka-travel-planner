from agents.preference_agent import PreferenceAgent
from agents.budget_agent import BudgetAgent
from agents.rag_agent import rag_agent
from agents.transport_agent import TransportAgent
from agents.accommodation_agent import AccommodationAgent
from agents.itinerary_agent import ItineraryAgent
from agents.weather_agent import WeatherAgent
from agents.recommendation_agent import RecommendationAgent
from agents.router_agent import RouterAgent

import re



# -----------------------------
# Initialize Agents
# -----------------------------


transport_agent = TransportAgent()

accommodation_agent = AccommodationAgent()

itinerary_agent = ItineraryAgent()

preference_agent = PreferenceAgent()

budget_agent = BudgetAgent()

weather_agent = WeatherAgent()

recommendation_agent = RecommendationAgent()

router_agent = RouterAgent()



# -----------------------------
# Destination Extraction
# -----------------------------


def extract_destination(message):


    locations = [

        "Kandy",
        "Ella",
        "Mirissa",
        "Galle",
        "Colombo",
        "Ratnapura",
        "Kitulgala",
        "Nuwara Eliya",
        "Sigiriya",
        "Anuradhapura",
        "Polonnaruwa",
        "Jaffna",
        "Trincomalee",
        "Bentota",
        "Arugam Bay"

    ]


    for place in locations:

        if place.lower() in message.lower():

            return place



    return "Sri Lanka"




# -----------------------------
# Main Planner Agent
# -----------------------------


def planner_agent(destination, budget, preferences, user_message):



    # Extract destination if UI sends empty value

    if not destination:

        destination = extract_destination(
            user_message
        )



    # Router

    routing_information = router_agent.process_request(

        user_message

    )



    # RAG Retrieval

    travel_info = rag_agent(

        destination

    )



    # Shared message

    planner_message = {


        "sender":"Planner Agent",


        "travel_details":{


            "destination":destination,


            "budget":budget


        }

    }




    # Preference

    preference_info = preference_agent.process_request(

        preferences

    )



    # Budget

    budget_info = budget_agent.process_request(

        planner_message

    )



    # Weather

    weather_info = weather_agent.process_request(

        planner_message

    )



    # Transport

    transport_info = transport_agent.process_request(

        planner_message

    )



    # Accommodation

    accommodation_info = accommodation_agent.process_request(

        planner_message

    )



    # Itinerary

    itinerary_info = itinerary_agent.process_request(

        planner_message

    )




    # Data for Recommendation Agent


    recommendation_input = {


        "sender":"Planner Agent",


        "destination":destination,


        "travel_information":travel_info,


        "preference_information":preference_info,


        "budget_information":budget_info,


        "weather_information":weather_info,


        "transport_information":transport_info,


        "accommodation_information":accommodation_info,


        "itinerary_information":itinerary_info


    }




    # Final answer

    recommendation_info = recommendation_agent.process_request(

        recommendation_input

    )




    return {


        "sender":"Planner Agent",


        "destination":destination,


        "routing_information":routing_information,


        "preference_information":preference_info,


        "budget_information":budget_info,


        "weather_information":weather_info,


        "travel_information":travel_info,


        "transport_information":transport_info,


        "accommodation_information":accommodation_info,


        "itinerary_information":itinerary_info,


        "recommendation_information":recommendation_info


    }





# -----------------------------
# Testing
# -----------------------------


if __name__=="__main__":


    result = planner_agent(


        "",


        8000,


        {


            "budget_type":"Medium",


            "travel_style":"Cultural",


            "interests":[

                "Food",

                "Culture"

            ]

        },


        """

        I want to visit Ratnapura next week.

        My budget is Rs.8000.

        I love cultural places and local food.

        Suggest transport, hotels and activities.

        """

    )



    print(

        result["recommendation_information"]["final_recommendation"]

    )