class TransportAgent:
    """
    Transport Agent responsible for finding
    suitable transportation options.
    """

    def __init__(self):
        self.name = "Transport Agent"

    def process_request(self, planner_message):
        """
        Receive structured message from Planner Agent
        and generate transport recommendations.
        """

        destination = planner_message["travel_details"]["destination"]
        budget = planner_message["travel_details"]["budget"]

        response = {
            "sender": self.name,
            "received_from": planner_message["sender"],

            "destination": destination,

            "transport_options": [
                {
                    "method": "Public Bus",
                    "estimated_cost": "Rs.500-800",
                    "speed": "Medium"
                },
                {
                    "method": "Train",
                    "estimated_cost": "Rs.300-600",
                    "speed": "Fast"
                },
                {
                    "method": "Taxi",
                    "estimated_cost": "Rs.4000-5000",
                    "speed": "Very Fast"
                }
            ],

            "budget_reference": budget
        }

        return response


# Test Transport Agent
if __name__ == "__main__":

    transport_agent = TransportAgent()

    planner_message = {
        "sender": "Planner Agent",

        "travel_details": {
            "destination": "Pallekele",
            "budget": 5000
        }
    }

    result = transport_agent.process_request(planner_message)

    print(result)