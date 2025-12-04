from agent.tools.workout_planner import create_workout_plan

def test_workout_planner():
    result = create_workout_plan("weight loss")
    assert "HIIT" in result