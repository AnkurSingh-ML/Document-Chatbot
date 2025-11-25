from pydantic import BaseModel

class MCPMessage(BaseModel):
    sender: str
    receiver: str
    type: str
    trace_id: str
    payload: dict