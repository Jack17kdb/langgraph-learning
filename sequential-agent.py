from typing import TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
  name: str
  age: int
  skills: list[str]
  final: str

def first_node(state: AgentState) -> AgentState:
  """Personalizes name with greeting"""

  state['final'] = f"Hey {state['name']}, welcome to the system!"
  return state

def second_node(state: AgentState) -> AgentState:
  """Describes user's age"""

  state['final'] += f" You are {state['age']} years old!"
  return state

def third_node(state: AgentState) -> AgentState:
  """Lists users skills"""

  state['final'] += f" You have skills in: {', '.join(state['skills'])}"
  return state

graph = StateGraph(AgentState)

graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.add_node("third_node", third_node)

graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.add_edge("second_node", "third_node")
graph.set_finish_point("third_node")

app = graph.compile()

result = app.invoke({"name": "Rex", "age": 20, "skills": ["machine learning", "deep learning", "ethical hacking", "devops engineering"]})

print(result)
print(result['final'])
