from agent.fitness_agent import agent

def test_agent_basic():
    response = agent.run("Create a workout plan for a beginner aiming to lose weight.")
    assert "Workout Plan" in response