from agents.llm_service import groq_chat


class RouterAgent:


    def process_request(self, user_message):

        prompt = f"""

You are a routing agent for a Sri Lanka travel planner.

Classify the user request.

Choose one task:

1. extract_information
2. generate_recommendation
3. answer_general_question


User message:

{user_message}


Return only the task name.

"""


        response = groq_chat(prompt)


        return {

            "sender": "Router Agent",

            "selected_task": response.strip()

        }