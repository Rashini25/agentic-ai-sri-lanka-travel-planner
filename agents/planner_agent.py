from agents.rag_agent import rag_agent
from agents.transport_agent import TransportAgent
from agents.accommodation_agent import AccommodationAgent
from agents.itinerary_agent import ItineraryAgent


transport_agent = TransportAgent()
accommodation_agent = AccommodationAgent()
itinerary_agent = ItineraryAgent()


def planner_agent(destination, budget):

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

        "travel_information": travel_info,

        "transport_information": transport_info,

        "accommodation_information": accommodation_info,

        "itinerary_information": itinerary_info
    }


if __name__ == "__main__":

    result = planner_agent(
        "Kitulgala",
        5000
    )

    print(result)