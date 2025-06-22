from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import asyncio
from langchain_core.messages import HumanMessage
from langchain.tools import tool

# https://github.com/langchain-ai/langchain-mcp-adapters
async def agent_with_mcp_tools(messages:list) -> str:
    """This function creates a React agent with MCP tools and invokes it with the provided messages.
    Args:
        messages (list): A list of messages to be processed by the agent.
        Returns: str: The response from the agent.
    """

    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": ["/path/to/math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                # make sure you start your weather server on port 8000
                "url": "http://localhost:8000/mcp/",
                "transport": "streamable_http",
            }
        }
    )
    
    tools = await client.get_tools()
    agent = create_react_agent(model=llm, tools=tools)
    result = await agent.ainvoke({"messages": messages})
    return result["messages"][-1].content
    
    
    
@tool
def syncronziedToolExample(pormpt: str) -> str:
    message = [HumanMessage(content=pormpt)]
    return asyncio.run(agent_with_mcp_tools(message)) # This will return a synchronous result from the agent
    