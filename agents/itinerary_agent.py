class ItineraryAgent:
    """
    Itinerary Agent responsible for creating
    a simple travel itinerary.
    """

    def __init__(self):
        self.name = "Itinerary Agent"

    def process_request(self, planner_message):

        destination = planner_message["travel_details"]["destination"]

        response = {
            "sender": self.name,
            "received_from": planner_message["sender"],
            "destination": destination,

            "itinerary": [
                {
                    "day": 1,
                    "activities": [
                        "Arrive at destination",
                        "Check in to accommodation",
                        "Visit nearby attractions"
                    ]
                },
                {
                    "day": 2,
                    "activities": [
                        "Explore major tourist attractions",
                        "Enjoy local food",
                        "Shopping and leisure"
                    ]
                }
            ]
        }

        return response


if __name__ == "__main__":

    itinerary_agent = ItineraryAgent()

    planner_message = {
        "sender": "Planner Agent",
        "travel_details": {
            "destination": "Kitulgala"
        }
    }

    result = itinerary_agent.process_request(planner_message)

    print(result)