from typing import TypedDict, Dict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
  message: str

def greetings(state: AgentState) -> AgentState:
  """Simple node that adds a greeting message to state"""

  state['message'] = state['message'] + ", you're doing an amazing job learning langgraph!"

  return state

graph = StateGraph(AgentState)

graph.add_node("greeter", greetings)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

result = app.invoke({"message": "Rex"})
result['message']
