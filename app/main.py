from fastapi import FastAPI
from app.models import AgentRequest, AgentResponse
from app.agent import AutonomousAgent

app = FastAPI(
    title="Autonomous AI Agent V2",
    version="2.0"
)

agent = AutonomousAgent()


@app.get("/")
def home():
    return {
        "status": "Running",
        "version": "2.0"
    }


@app.post(
        "/agent",
        response_model=AgentResponse
        )
def execute(request: AgentRequest):

    return agent.process_request(
        request.request
    )