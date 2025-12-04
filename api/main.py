from fastapi import FastAPI
from agent.fitness_agent import agent

app = FastAPI()

@app.post("/fitness-agent")
async def ask_agent(query: str):
    response = agent.run(query)
    return {"response": response}