
# LangGraph Agent Project

This project demonstrates two main capabilities:

## 1. Retrieval-Augmented Generation (RAG)
- Uses OpenSearch as a vector store for document indexing and retrieval.
- Employs Azure OpenAI for generating embeddings of your documents.
- Retrieves relevant documents directly from OpenSearch to ground and enhance agent responses (no other vector store is used).
- Example workflow: You provide a query, the system fetches semantically similar documents from OpenSearch, and the agent uses these to generate a more informed answer.

## 2. React Agent with MCP Tools
- Implements a React-style agent using LangGraph and LangChain frameworks.
- Integrates MCP tools (e.g., math, weather) as callable tools, allowing the agent to perform actions or answer questions using external APIs or logic.
- The agent can reason step-by-step, calling tools as needed to solve complex queries.

## Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure environment variables in `.env` (see `.env.example`).
   - You will need your Azure OpenAI credentials and OpenSearch connection details.
3. Start OpenSearch (for RAG):
   ```bash
   docker-compose up -d
   ```
4. Run the RAG example:
   ```bash
   python rag-opensearch.py
   ```
   - This will index documents (if not already indexed) and allow you to query using retrieval-augmented generation.

## How RAG Works
- Documents are embedded using Azure OpenAI and stored in OpenSearch.
- When you ask a question, the system retrieves the most relevant documents from OpenSearch using vector similarity.
- The agent uses these documents to generate a grounded, context-aware response.

## How the React Agent Works
- The agent uses LangGraph to manage reasoning steps and tool calls.
- MCP tools are integrated as callable functions, so the agent can perform calculations, fetch weather, or other tasks as needed.

## File Overview
- `rag-opensearch.py`: RAG retrieval example
- `agent/agent.py`: React agent with MCP tools
- `agent/tools.py`: MCP tool integration
- `requirements.txt`: Dependencies

---
For more, see code comments and each module's docstrings.


