from typing import TypedDict, List
from langgraph.graph import StateGraph
from math import prod

class AgentState(TypedDict):
  values: List[int]
  name: str
  operation: str
  result: str

def process_state(state: AgentState) -> AgentState:
  """Node to process the state"""

  if state['operation'] == "*":
    state['result'] = f"Hi {state['name']}, your answer is {prod(state['values'])}!"
  elif state['operation'] == "+":
    state['result'] = f"Hi {state['name']}, your answer is {sum(state['values'])}!"
  else:
    state['result'] = f"Hi {state['name']}, unacceptable operation provided!"

  return state

graph = StateGraph(AgentState)

graph.add_node("processor", process_state)
graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()

answer = app.invoke({"values": [1,2,3,4,5], "name": "Rex", "operation": "*"})
answer['result']
