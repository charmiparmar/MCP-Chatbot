def create_agents(subtasks: list[str]) -> list[dict]:
    return [{"id": i, "task": task} for i, task in enumerate(subtasks)]
