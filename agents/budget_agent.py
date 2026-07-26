class BudgetAgent:
    """
    Budget Agent responsible for analyzing
    travel costs and providing budget recommendations.
    """

    def __init__(self):
        self.name = "Budget Agent"


    def process_request(self, planner_message):

        destination = planner_message["travel_details"]["destination"]
        budget = planner_message["travel_details"]["budget"]


        # Estimated cost calculation
        transport_cost = 500
        accommodation_cost = 2500
        activity_cost = 2000

        total_cost = (
            transport_cost +
            accommodation_cost +
            activity_cost
        )


        if total_cost <= budget:
            recommendation = (
                "The planned trip is within the user's budget."
            )

        else:
            recommendation = (
                "Reduce costs by selecting cheaper transport "
                "or accommodation options."
            )


        response = {

            "sender": self.name,

            "received_from": planner_message["sender"],

            "destination": destination,

            "budget_analysis": {

                "available_budget": budget,

                "estimated_cost": total_cost,

                "cost_breakdown": {

                    "transport": transport_cost,

                    "accommodation": accommodation_cost,

                    "activities": activity_cost
                },

                "recommendation": recommendation
            }
        }


        return response



if __name__ == "__main__":

    budget_agent = BudgetAgent()


    planner_message = {

        "sender": "Planner Agent",

        "travel_details": {

            "destination": "Kitulgala",

            "budget": 5000
        }
    }


    result = budget_agent.process_request(
        planner_message
    )


    print(result)