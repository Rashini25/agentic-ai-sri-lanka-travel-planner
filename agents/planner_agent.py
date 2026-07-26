from agents.rag_agent import rag_agent


def planner_agent(destination):

    travel_info = rag_agent(destination)

    return {
        "sender": "Planner Agent",
        "destination": destination,
        "travel_info": travel_info
    }


if __name__ == "__main__":

    result = planner_agent("Kitulgala")

    print(result)