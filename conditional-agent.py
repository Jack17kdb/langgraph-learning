from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
  number1: int
  number2: int
  operation1: str
  finalNumber1: int
  number3: int
  number4: int
  operation2: str
  finalNumber2: int

def adder1(state: AgentState) -> AgentState:
  """Function to add 2 numbers"""

  state['finalNumber1'] = state['number1'] + state['number2']
  return state

def substractor1(state: AgentState) -> AgentState:
  """Function to minus 2 numbers"""

  state['finalNumber1'] = state['number1'] - state['number2']
  return state

def adder2(state: AgentState) -> AgentState:
  """Function to add 2 numbers"""

  state['finalNumber2'] = state['number3'] + state['number4']
  return state

def substractor2(state: AgentState) -> AgentState:
  """Function to minus 2 numbers"""

  state['finalNumber2'] = state['number3'] - state['number4']
  return state

def first_operation(state: AgentState) -> AgentState:
  """Decide which node to go to"""

  if state['operation1'] == "+":
    return "addition_operation"
  elif state['operation1'] == "-":
    return "minus_operation"

def second_operation(state: AgentState) -> AgentState:
  """Decide which node to go to"""

  if state['operation2'] == "+":
    return "addition_operation1"
  elif state['operation2'] == "-":
    return "minus_operation1"

graph = StateGraph(AgentState)

graph.add_node("adder1", adder1)
graph.add_node("substractor1", substractor1)
graph.add_node("adder2", adder2)
graph.add_node("substractor2", substractor2)
graph.add_node("router1", lambda state:state)
graph.add_node("router2", lambda state:state)

graph.add_edge(START, "router1")

graph.add_conditional_edges(
    "router1",
    first_operation,
    {
        "addition_operation": "adder1",
        "minus_operation": "substractor1"
    }
)

graph.add_edge("adder1", "router2")
graph.add_edge("substractor1", "router2")

graph.add_conditional_edges(
    "router2",
    second_operation,
    {
        "addition_operation1": "adder2",
        "minus_operation1": "substractor2"
    }
)

graph.add_edge("adder2", END)
graph.add_edge("substractor2", END)

app = graph.compile()

result = app.invoke({
    "number1": 10,
    "number2": 20,
    "operation1": "+",
    "finalNumber1": 0,
    "number3": 40,
    "number4": 28,
    "operation2": "-",
    "finalNumber2": 0
})

print("Result:", result)
print(f"Operation 1: {result['operation1']}")
print(f"Final Number 1: {result['finalNumber1']}")
print(f"Operation 2: {result['operation2']}")
print(f"Final Number 2: {result['finalNumber2']}")
