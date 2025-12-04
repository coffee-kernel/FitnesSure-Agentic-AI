def generate_meal_plan(preference: str = "balanced"):
    preference = preference.lower()
    
    if preference == "keto":
        return "Meal Plan: High fat, low carb; eggs, avocado, salmon, leafy greens."
    
    if preference == "vegan":
        return "Meapl Plan: Lentils, Tofus, quinoa, vegetables, nuts."
    
    return "Meal Plan: Balanced diet with lean proteins, whole grains, fruits, and vegetables."