from typing import Dict,TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    message : str

def greeting_node(state :AgentState)->AgentState:
    """
    Simple node to add greeting message to the state 
    """
    state['message'] = "hi "+state["message"]

    return state

graph=StateGraph(AgentState)
graph.add_node("greeter",action=greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")
app=graph.compile()

from IPython.display import Image,display
display(Image(app.get_graph().draw_mermaid_png()))

if __name__=="__main__":
    res=app.invoke({"message":"bon"})
    print(res['message'])
