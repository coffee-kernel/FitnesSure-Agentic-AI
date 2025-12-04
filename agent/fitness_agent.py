from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from .tools.workout_planner import create_workout_plan
from .tools.nutrition_tool import generate_meal_plan
from .tools.progress_tracker import update_progress, get_progress

llm = ChatOpenAI(model="gpt-4o-mini")

tools = [
    Tool(
        name="WorkoutPlanner",
        func=create_workout_plan,
        description="Create a personalized workout plan based on fitness goals and experience level."
    ),
    Tool(
        name="MealPlanner",
        func=generate_meal_plan,
        description="Generate a meal plan based on dietary preferences."
    ),
    Tool(
        name="UpdateProgress",
        func=lambda x: update_progress("user1", x),
        description="Update the user's fitness progress with new data."
    ),
    Tool(
        name="GetProgress",
        func=lambda _: get_progress("user1"),
        description="Retrieve the user's fitness progress data."
    ),
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)