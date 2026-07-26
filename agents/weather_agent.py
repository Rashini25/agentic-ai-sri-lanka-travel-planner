class WeatherAgent:
    """
    Weather Agent responsible for providing
    weather-based travel recommendations.
    """

    def __init__(self):
        self.name = "Weather Agent"


    def process_request(self, planner_message):
        """
        Receive destination details from Planner Agent
        and generate weather recommendations.
        """

        destination = planner_message["travel_details"]["destination"]


        weather_database = {

            "Kitulgala": {
                "condition": "Warm and humid",
                "temperature": "25°C - 30°C",
                "recommendation": "Suitable for rainforest activities and rafting. Carry rain protection."
            },

            "Kandy": {
                "condition": "Cool and pleasant",
                "temperature": "20°C - 28°C",
                "recommendation": "Good for sightseeing and cultural activities."
            },

            "Ella": {
                "condition": "Cool mountain climate",
                "temperature": "18°C - 25°C",
                "recommendation": "Ideal for hiking and outdoor exploration."
            }
        }


        weather_info = weather_database.get(
            destination,
            {
                "condition": "Tropical climate",
                "temperature": "25°C - 32°C",
                "recommendation": "Check local weather conditions before travelling."
            }
        )


        return {

            "sender": self.name,

            "received_from": planner_message["sender"],

            "destination": destination,

            "weather_information": weather_info
        }



if __name__ == "__main__":

    weather_agent = WeatherAgent()


    planner_message = {

        "sender": "Planner Agent",

        "travel_details": {

            "destination": "Kitulgala"

        }
    }


    result = weather_agent.process_request(
        planner_message
    )


    print(result)