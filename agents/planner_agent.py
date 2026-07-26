from agents.preference_agent import PreferenceAgent
from agents.budget_agent import BudgetAgent
from agents.rag_agent import rag_agent
from agents.transport_agent import TransportAgent
from agents.accommodation_agent import AccommodationAgent
from agents.itinerary_agent import ItineraryAgent


# Initialize agents
transport_agent = TransportAgent()
accommodation_agent = AccommodationAgent()
itinerary_agent = ItineraryAgent()
preference_agent = PreferenceAgent()
budget_agent = BudgetAgent()



def planner_agent(destination, budget, preferences):

    # Get travel information from RAG Agent
    travel_info = rag_agent(destination)


    # Structured message for other agents
    planner_message = {
        "sender": "Planner Agent",

        "travel_details": {
            "destination": destination,
            "budget": budget
        }
    }


    # Analyze user preferences
    preference_info = preference_agent.process_request(
        preferences
    )


    # Analyze budget
    budget_info = budget_agent.process_request(
        planner_message
    )


    # Get transport recommendations
    transport_info = transport_agent.process_request(
        planner_message
    )


    # Get accommodation recommendations
    accommodation_info = accommodation_agent.process_request(
        planner_message
    )


    # Get itinerary recommendations
    itinerary_info = itinerary_agent.process_request(
        planner_message
    )


    return {

        "sender": "Planner Agent",

        "destination": destination,

        "preference_information": preference_info,

        "budget_information": budget_info,

        "travel_information": travel_info,

        "transport_information": transport_info,

        "accommodation_information": accommodation_info,

        "itinerary_information": itinerary_info
    }



if __name__ == "__main__":

    result = planner_agent(

        "Kitulgala",

        5000,

        {
            "budget_type": "Low",

            "travel_style": "Adventure",

            "interests": [
                "Adventure",
                "Nature"
            ]
        }
    )


    print(result)