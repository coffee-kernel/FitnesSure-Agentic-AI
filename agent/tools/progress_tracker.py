_user_progress = {}

def update_progress(user_id: str, entry: dict):
    if user_id not in _user_progress:
        _user_progress[user_id] = []
    _user_progress[user_id].append(entry)
    return "Progress updated successfully."

def get_progress(user_id: str):
    return _user_progress.get(user_id, [])