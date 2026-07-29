# Smart Sri Lankan Travel Planning Assistant
### Agentic AI Powered Tourism Recommendation System using Multi-Agent Architecture and Retrieval-Augmented Generation (RAG)

---

## Module Information

**University:** Horizon Campus  
**Faculty:** Faculty of Information Technology  

**Module:** IT41043 – Intelligent Systems (Agentic AI)

---

# Project Overview

The **Smart Sri Lankan Travel Planning Assistant** is an intelligent AI-powered travel recommendation system designed to help both local and international travelers plan personalized trips across Sri Lanka.

Unlike traditional travel chatbots, this system utilizes an **Agentic AI architecture** consisting of multiple specialized AI agents that collaborate to understand user preferences, retrieve relevant tourism knowledge, generate optimized travel recommendations, and produce personalized travel itineraries.

The application combines:

- Multi-Agent Systems
- Agentic AI Design Patterns
- Retrieval-Augmented Generation (RAG)
- Large Language Models (Groq + OpenRouter)
- Streamlit Deployment

to provide accurate, context-aware and user-specific travel guidance.

---

# Problem Statement

Many travel planning platforms provide generic recommendations that fail to consider individual travel preferences, budget constraints, transportation options, accommodation choices, and current tourism information.

Tourists often need to search across multiple websites to gather information, making travel planning time-consuming and inefficient.

This project addresses this problem by integrating multiple intelligent AI agents capable of collaboratively generating personalized travel recommendations using domain-specific tourism knowledge.

---

# Objectives

## Main Objective

To develop an intelligent multi-agent travel planning assistant that provides personalized travel recommendations for destinations across Sri Lanka using Agentic AI and Retrieval-Augmented Generation.

## Specific Objectives

- Understand user travel preferences.
- Analyze available tourism knowledge.
- Recommend suitable destinations.
- Suggest transportation options.
- Recommend accommodations.
- Generate optimized travel itineraries.
- Produce personalized travel plans.
- Demonstrate Agentic AI collaboration.
- Integrate Retrieval-Augmented Generation.
- Deploy a publicly accessible AI application.

---

# Key Features

- Multi-Agent AI Architecture
- Personalized Travel Planning
- Budget-aware Recommendations
- Destination Recommendations
- Accommodation Suggestions
- Transportation Recommendations
- Travel Itinerary Generation
- RAG Knowledge Retrieval
- Beautiful Streamlit Interface
- Responsive Chat Experience
- Modular Agent Design
- Intelligent Prompt Routing

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | AI Workflow |
| ChromaDB | Vector Database |
| Sentence Transformers | Embedding Model |
| Groq API | Fast LLM Inference |
| OpenRouter API | Advanced Reasoning |
| FAISS / Chroma | Vector Search |
| Git & GitHub | Version Control |

---

# Agentic AI Architecture

The system follows a **Router → Specialized Agents → Recommendation Pipeline** architecture.

```
                    User

                      │

                      ▼

             Planner / Router Agent

                      │

 ┌──────────┬──────────┬──────────┬────────────┐

 ▼          ▼          ▼          ▼

Preference  Budget     RAG      Destination

 Agent       Agent    Agent       Agent

 └──────────┬──────────┬──────────┘

            ▼

 Transportation Agent

            ▼

 Accommodation Agent

            ▼

 Itinerary Agent

            ▼

 Recommendation Agent

            ▼

      Final Response

```

---

# Agent Communication Diagram

The project demonstrates structured communication between multiple AI agents.

```
User

↓

Planner Agent

↓

Preference Agent

↓

Budget Agent

↓

RAG Knowledge Agent

↓

Transportation Agent

↓

Accommodation Agent

↓

Itinerary Agent

↓

Recommendation Agent

↓

Streamlit UI

```

Each agent exchanges structured Python dictionaries containing:

- user preferences
- travel style
- destination information
- accommodation options
- transportation details
- itinerary information
- final recommendation

---

# Agentic AI Design Patterns Used

This project implements multiple Agentic AI design patterns.

## 1. Router Pattern

Used inside:

```
planner_agent.py
```

Purpose:

Routes user requests to specialized agents.

---

## 2. Planning / Task Decomposition

Used inside:

```
planner_agent.py
```

The Planner Agent breaks the travel planning task into smaller subtasks:

- preference analysis
- budget analysis
- destination search
- accommodation planning
- transportation planning
- itinerary generation
- recommendation generation

---

## 3. Tool Use Pattern

Used inside:

```
rag_agent.py
```

External retrieval tools are used to query the vector database.

---

## 4. Retrieval-Augmented Generation (RAG)

The Recommendation Agent combines retrieved tourism knowledge with LLM reasoning before generating the final response.

---

# Model Selection Strategy

The project deliberately uses two different LLM providers.

| Sub Task | Model Provider | Reason |
|-----------|---------------|--------|
| Fast planning and routing | Groq | Very low latency, fast inference, cost-effective |
| Final recommendation generation | OpenRouter | Better reasoning quality and richer travel recommendations |

### Why Multiple Models?

Using Groq for routing minimizes response time while OpenRouter provides stronger reasoning capabilities for generating high-quality personalized travel plans.

This improves overall system performance while balancing latency and response quality.

---

# Retrieval-Augmented Generation (RAG)

The system integrates Retrieval-Augmented Generation using a tourism knowledge base.

## Knowledge Base

The vector database contains tourism-related documents covering:

- Sri Lankan destinations
- Attractions
- Historical places
- Beaches
- Wildlife
- Transportation
- Hotels
- Cultural information
- Local travel tips

More than **20 domain-specific documents** are embedded into the vector database.

---

## Embedding Model

```
Sentence Transformers
```

---

## Vector Store

```
ChromaDB
```

---

## Chunking Strategy

Documents are divided into smaller overlapping chunks before embedding.

Benefits include:

- Improved semantic search
- Better retrieval accuracy
- Reduced hallucination
- Context preservation

---

# Retrieval Evaluation

Five sample queries were tested.

| Query | Retrieved Relevant? |
|--------|--------------------|
| Best beaches in Sri Lanka | Yes |
| Budget trip to Ella | Yes |
| Wildlife destinations | Yes |
| Cultural attractions | Yes |
| Adventure travel recommendations | Yes |

The retrieved documents were relevant and successfully supported the final generated responses.

---

# Folder Structure

```
agentic-ai-sri-lanka-travel-planner/

│

├── agents/

│   ├── planner_agent.py

│   ├── recommendation_agent.py

│   ├── preference_agent.py

│   ├── budget_agent.py

│   ├── itinerary_agent.py

│   ├── transport_agent.py

│   ├── accommodation_agent.py

│   └── rag_agent.py

│

├── data/

├── vector_db/

├── app.py

├── requirements.txt

├── README.md

└── .streamlit/

```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Rashini25/agentic-ai-sri-lanka-travel-planner.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure API keys

Create a `.streamlit/secrets.toml` file:

```toml
GROQ_API_KEY="your_key"

OPENROUTER_API_KEY="your_key"
```

Run the application

```bash
streamlit run app.py
```

---

# Deployment

The application is deployed using **Streamlit Community Cloud**.

**Live Application**

https://agentic-ai-sri-lanka-travel-planner-olf2bv5blhmv3mxf6yt4jy.streamlit.app/

---

# GitHub Repository

Repository:

https://github.com/Rashini25/agentic-ai-sri-lanka-travel-planner

---

# Known Limitations

- Depends on internet connectivity.
- Limited to the current tourism knowledge base.
- Real-time hotel pricing is not integrated.
- Weather information is not yet included.
- Does not currently support multi-day optimization using live APIs.

---

# Future Improvements

- Google Maps integration
- Live weather forecasts
- Hotel booking APIs
- Public transport APIs
- Voice interaction
- Image recommendations
- Multi-language support
- Real-time event recommendations
- User account personalization

---

# Conclusion

The Smart Sri Lankan Travel Planning Assistant successfully demonstrates the practical implementation of Agentic AI using a collaborative multi-agent architecture, Retrieval-Augmented Generation (RAG), and multiple large language models. The system provides personalized, context-aware travel recommendations while showcasing modern AI engineering practices including modular agent communication, deliberate model selection, vector-based knowledge retrieval, and a user-friendly Streamlit interface.

---

# Author

**Rashini Prabodha**

BSc (Hons) Information Technology

Horizon Campus

IT41043 – Intelligent Systems (Agentic AI)

2026
