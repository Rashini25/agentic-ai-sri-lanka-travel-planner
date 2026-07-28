import streamlit as st
import time
import re

from agents.planner_agent import planner_agent



# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(

    page_title="Smart Sri Lankan Travel Planning Assistant",

    page_icon="",

    layout="centered",

    initial_sidebar_state="expanded"

)



# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown(

"""
<style>


/* Main Background */

.stApp {

background:

radial-gradient(
circle at 20% 15%,
rgba(14,165,233,0.12),
transparent 35%
),

radial-gradient(
circle at 80% 85%,
rgba(37,99,235,0.12),
transparent 35%
),

linear-gradient(
135deg,
#010409,
#041426,
#020617
);


color:white;

}




/* Hide Streamlit Default */

#MainMenu {

visibility:hidden;

}


footer {

visibility:hidden;

}


header {

visibility:hidden;

}




.main-title {

text-align:center !important;

font-size:52px !important;

font-weight:800 !important;

letter-spacing:1.5px !important;

line-height:1.2 !important;

color:#E0F2FE !important;

margin-top:15px !important;

margin-bottom:10px !important;

animation:titleGlow 3s infinite alternate;

}




@keyframes titleGlow {


from {


text-shadow:

0 0 8px #38BDF8;


}



to {


text-shadow:

0 0 25px #0284C7,
0 0 40px #0EA5E9;


}


}




.subtitle {


text-align:center;

font-size:16px;

color:#BAE6FD;

margin-bottom:35px;


}




/* Chat Message Box */


[data-testid="stChatMessage"] {


background:


linear-gradient(

135deg,

rgba(15,40,70,0.95),

rgba(8,47,73,0.95)

);



border:

1px solid rgba(56,189,248,0.35);



border-radius:20px;



padding:18px;



margin-bottom:15px;



transition:0.3s;


}




[data-testid="stChatMessage"]:hover {


transform:translateY(-3px);



border-color:#38BDF8;



box-shadow:

0 0 20px rgba(56,189,248,0.35);


}




/* Remove bottom black container */

[data-testid="stBottom"] {

    background: transparent !important;

}



[data-testid="stBottomBlockContainer"] {

    background: transparent !important;

    padding-bottom: 20px !important;

}



/* Chat Input */

[data-testid="stChatInput"] {

    background:

    linear-gradient(
        135deg,
        rgba(15,40,70,0.95),
        rgba(8,47,73,0.95)
    ) !important;


    border-radius:25px !important;


    border:

    1px solid rgba(56,189,248,0.5) !important;


    box-shadow:

    0 0 20px rgba(14,165,233,0.25);


    backdrop-filter:blur(15px);


}



[data-testid="stChatInput"]:hover {


    border-color:#38BDF8 !important;


    box-shadow:

    0 0 25px rgba(56,189,248,0.6);


}



/* Input Text */

[data-testid="stChatInput"] textarea {


    color:#E0F2FE !important;


}



/* Remove extra Streamlit bottom padding */

.block-container {


    padding-bottom:80px !important;


}







/* Text */

p,span,li {


color:#E0F2FE !important;


}




/* Sidebar */


section[data-testid="stSidebar"] {


background:


linear-gradient(

180deg,

#020617,

#082F49

);


}




/* Buttons */


button {


border-radius:12px !important;


}



/* Remove Streamlit floating bottom background */

div[data-testid="stBottom"] > div {

    background: transparent !important;

}


.stAppViewContainer {

    background: transparent !important;

}


.main {

    background: transparent !important;

}
/* -----------------------------
   AI Response Typography
------------------------------*/


/* Main response title */

.stMarkdown h1 {

font-size:28px !important;

font-weight:700 !important;

color:#E0F2FE !important;

margin-bottom:18px !important;

}



/* Section headings */

.stMarkdown h2 {

font-size:22px !important;

font-weight:650 !important;

color:#BAE6FD !important;

margin-top:20px !important;

margin-bottom:12px !important;

}



/* Sub headings */

.stMarkdown h3 {

font-size:18px !important;

font-weight:600 !important;

color:#7DD3FC !important;

margin-top:15px !important;

}



/* Normal response text */

.stMarkdown p,
.stMarkdown li {


font-size:15px !important;

line-height:1.7 !important;

color:#E5F3FF !important;


}
</style>

""",

unsafe_allow_html=True

)




# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown(

"""
<h1 class="main-title">

Smart Sri Lankan Travel Planning Assistant

</h1>

<div class="subtitle">

Plan your Sri Lankan journey with intelligent AI-powered recommendations.
Our multi-agent travel assistant analyzes your preferences, budget, destination,
and interests using Agentic AI and Retrieval Augmented Generation (RAG)
to provide personalized transportation, accommodation, activities, and travel insights.

</div>

""",

unsafe_allow_html=True

)





# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:


    st.markdown(

        "## 🌏 Travel Assistant"

    )


    if st.button("➕ New Chat"):


        st.session_state.messages=[]

        st.rerun()



    st.divider()



    st.markdown(

"""
### AI Architecture


Router Agent

RAG Knowledge Agent

Preference Agent

Budget Agent

Transport Agent

Accommodation Agent

Itinerary Agent

Recommendation Agent

"""

    )





# -------------------------------------------------
# SESSION MEMORY
# -------------------------------------------------

if "messages" not in st.session_state:


    st.session_state.messages=[]





# -------------------------------------------------
# DISPLAY CHAT HISTORY
# -------------------------------------------------

for message in st.session_state.messages:


    with st.chat_message(message["role"]):


        st.markdown(

            message["content"]

        )





# -------------------------------------------------
# CLEAN AI RESPONSE
# -------------------------------------------------

def clean_response(text):


    emojis = [

        "🚆",

        "🏨",

        "📅",

        "🍛",

        "💰",

        "🌦",

        "🧠",

        "✈️",

        "🌏"

    ]



    for emoji in emojis:


        text=text.replace(

            emoji,

            ""

        )


    return text.strip()




# -------------------------------------------------
# EXTRACT USER INFORMATION
# -------------------------------------------------

def extract_user_information(text):


    budget=5000


    travel_style="General"


    interests=[]



    budget_match=re.search(

        r'(\d{3,6})\s*(?:rupees|rs|Rs|/=)?',

        text

    )



    if budget_match:


        budget=int(

            budget_match.group(1)

        )



    keywords=[


        "beach",

        "nature",

        "food",

        "photography",

        "culture",

        "cultural",

        "history",

        "adventure",

        "wildlife"

    ]



    for word in keywords:


        if word.lower() in text.lower():


            interests.append(word)



    if "culture" in text.lower() or "cultural" in text.lower():


        travel_style="Cultural"



    elif "beach" in text.lower():


        travel_style="Relaxation"



    elif "adventure" in text.lower():


        travel_style="Adventure"



    elif "nature" in text.lower():


        travel_style="Nature"



    return budget, travel_style, interests
# -------------------------------------------------
# CHAT INPUT
# -------------------------------------------------

user_prompt = st.chat_input(

    "Ask me about any Sri Lankan destination..."

)



if user_prompt:



    # Save user message

    st.session_state.messages.append(

        {

            "role":"user",

            "content":user_prompt

        }

    )



    # Display user message

    with st.chat_message("user"):


        st.markdown(user_prompt)





    # Assistant Response

    with st.chat_message("assistant"):



        thinking = st.empty()



        dots = ""



        for i in range(3):


            dots += "."


            thinking.markdown(

                f"AI Agents are preparing your travel plan{dots}"

            )


            time.sleep(0.5)



        thinking.empty()




        try:



            # Extract requirements

            budget, travel_style, interests = extract_user_information(

                user_prompt

            )





            # Call Agent System

            result = planner_agent(


                destination="",


                budget=budget,


                preferences={


                    "budget_type":


                    "Low" if budget <=5000 else "Medium",



                    "travel_style":

                    travel_style,



                    "interests":

                    interests


                },



                user_message=user_prompt


            )





            # Get Recommendation

            recommendation = result[

                "recommendation_information"

            ][

                "final_recommendation"

            ]





            # Remove unwanted emojis

            recommendation = clean_response(

                recommendation

            )





            # Display final answer

            st.markdown(

                recommendation

            )






        except Exception as e:



            recommendation = (

                "Sorry, I could not generate your travel plan."

            )


            st.error(e)





    # Save assistant message


    st.session_state.messages.append(

        {


            "role":"assistant",


            "content":recommendation


        }

    )