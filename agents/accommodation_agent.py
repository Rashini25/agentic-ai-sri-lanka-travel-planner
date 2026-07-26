class AccommodationAgent:
    """
    Accommodation Agent responsible for finding
    suitable accommodation options based on
    destination and budget.
    """

    def __init__(self):
        self.name = "Accommodation Agent"

    def process_request(self, planner_message):
        """
        Receive structured message from Planner Agent
        and generate accommodation recommendations.
        """

        destination = planner_message["travel_details"]["destination"]
        budget = planner_message["travel_details"]["budget"]

        response = {
            "sender": self.name,
            "received_from": planner_message["sender"],

            "destination": destination,

            "accommodation_options": [
                {
                    "name": "Budget Guest House",
                    "price_per_night": 2500,
                    "location": f"Near {destination}",
                    "rating": "4.2/5"
                },
                {
                    "name": "City Budget Hotel",
                    "price_per_night": 3500,
                    "location": f"Within {destination} area",
                    "rating": "4.5/5"
                },
                {
                    "name": "Affordable Homestay",
                    "price_per_night": 2000,
                    "location": f"Nearby {destination}",
                    "rating": "4.0/5"
                }
            ],

            "budget_reference": budget
        }

        return response


# Test Accommodation Agent
if __name__ == "__main__":

    accommodation_agent = AccommodationAgent()

    planner_message = {
        "sender": "Planner Agent",

        "travel_details": {
            "destination": "Pallekele",
            "budget": 5000
        }
    }

    result = accommodation_agent.process_request(planner_message)

    print(result)