import streamlit as st

from agents.planner_agent import planner_agent


st.set_page_config(
    page_title="Sri Lanka AI Travel Assistant",
    page_icon="🇱🇰",
    layout="centered"
)


# Header

st.title("🇱🇰 Sri Lanka AI Travel Assistant")

st.caption(
    "Your personal AI travel planner powered by multiple AI agents and RAG"
)


# Chat history

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])



# User input

user_prompt = st.chat_input(
    "Ask me about any Sri Lankan destination..."
)



if user_prompt:


    # Show user message

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_prompt
        }
    )


    with st.chat_message("user"):

        st.markdown(user_prompt)



    # AI response

    with st.chat_message("assistant"):


        with st.spinner(
            "AI agents are planning your trip..."
        ):


            result = planner_agent(

                destination="",

                budget=5000,

                preferences={
                    "budget_type":"Low",
                    "travel_style":"Adventure",
                    "interests":["Nature"]
                },

                user_message=user_prompt

            )


            recommendation = result[
                "recommendation_information"
            ][
                "final_recommendation"
            ]


            st.markdown(
                recommendation
            )


    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":recommendation
        }
    )