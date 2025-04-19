def split_into_subtasks(topic: str) -> list[str]:
    return [f"{topic} - aspect {i+1}" for i in range(3)]
