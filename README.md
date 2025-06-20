
# LangGraph Agent Project

This project is an end-to-end agent framework built using [LangGraph](https://github.com/langchain-ai/langgraph). It is designed to demonstrate how to construct, configure, and run a powerful AI agent pipeline, including Retrieval-Augmented Generation (RAG) as a major component.

## Major Sections

### 1. Retrieval-Augmented Generation (RAG)
RAG is a core part of this agent, enabling the agent to retrieve relevant information from a vector database (OpenSearch) and use it to enhance responses. The RAG pipeline uses OpenSearch as a vector store and Azure OpenAI for embeddings.

#### Features
* Store and retrieve vector embeddings in OpenSearch
* Use Azure OpenAI for text embedding
* Simple Python interface for querying relevant documents

#### Requirements
* Python 3.8+
* Docker (for running OpenSearch and OpenSearch Dashboards)

#### Setup for RAG

1. **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd langgraph-agent
    ```
2. **Install Python dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure Environment Variables**
    Copy `.env.example` to `.env` and fill in your Azure OpenAI and OpenSearch details:
    ```bash
    cp .env.example .env
    ```
    Edit `.env` and set:
    - `AZURE_OPENAI_API_KEY`
    - `AZURE_OPENAI_ENDPOINT`
    - `OPENSEARCH_URL`
4. **Start OpenSearch and Dashboards (UI)**
    ```bash
    docker-compose up -d
    ```
    - OpenSearch: [https://localhost:9200](https://localhost:9200)
    - Dashboards UI: [http://localhost:5601](http://localhost:5601)
      - Default username: `admin`, password: `admin`
5. **Run the RAG Example**
    ```bash
    python rag-opensearch.py
    ```
    Enter your query when prompted. The script will print the most relevant documents from OpenSearch.

#### File Overview (RAG)
* `rag-opensearch.py`: Main script for RAG retrieval
* `requirements.txt`: Python dependencies
* `docker-compose.yml`: OpenSearch and Dashboards setup
* `.env.example`: Example environment variables
* `my-index.json`: Example OpenSearch index mapping for vector search

#### Index Mapping
The file `my-index.json` provides a minimal example of an OpenSearch index mapping suitable for vector search with LangChain. It defines:
- `vector_field`: type `knn_vector`, dimension 1536 (this is the default field name that the LangChain API expects for vector search)
- `text`: type `text`, analyzer `standard`

If you use a different field name for your vector, you must specify it explicitly in your code. By default, LangChain looks for a field named `vector_field`.

---

## Other Sections

This project is designed to be modular. Additional agent capabilities, tools, and workflows can be added as new sections. See future updates for more features and agent logic.

## Notes
- This setup disables OpenSearch security for local development. Do not use in production as-is.
- For production, enable security and use secure credentials.

## References
- [OpenSearch Documentation](https://opensearch.org/docs/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://github.com/langchain-ai/langgraph)
- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)


