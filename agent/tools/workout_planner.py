def create_workout_plan(goal: str, experience: str = "beginner"):
    goal = goal.lower()
    experience = experience.lower()
    
    if goal == "weight loss":
        return "Workout Plan: 30 minutes HIIT (5 days/week) + 10k steps/day."
    
    if goal == "muscle gain":
         return "Workout Plan: Push/Pull/Legs split, 6-12 reps, 4-5 days/week."
     
    return "Workout Plan: Mixed Cardio + Strength Training, 3-4 days/week."