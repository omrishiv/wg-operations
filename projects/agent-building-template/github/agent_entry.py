from agent import MyAgent
from api_manager import endpoint
from pydantic import BaseModel

agent = MyAgent()


class Request(BaseModel):
    request: str


@endpoint(method="post")
def request(request: Request):
    return agent.run(request.request)
