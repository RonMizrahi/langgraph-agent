from langchain_openai import AzureChatOpenAI
from tools import syncronziedToolExample
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode

llm= AzureChatOpenAI(
    openai_api_key=azure_openai_api_key,
    azure_endpoint=azure_openai_endpoint,
    azure_deployment=azure_openai_deployment,
    azure_api_version=azure_openai_api_version,
    temperature=0
)

tools = [syncronziedToolExample]
llm_with_tools = llm.bind_tools(tools)

sys_message = SystemMessage(content="You are a helpful assistant that can answer questions about math and weather.")

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")

# Compile graph
graph = builder.compile()

def expose_graph():
    """Expose the graph for use in other modules."""
    return graph

# messages = [HumanMessage(content="Add 3 and 4. Multiply the output by 2. Divide the output by 5")]
# messages = graph.invoke({"messages": messages})
# for m in messages['messages']:
#     m.pretty_print()

