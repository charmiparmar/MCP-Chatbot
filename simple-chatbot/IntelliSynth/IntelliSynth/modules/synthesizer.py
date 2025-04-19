def synthesize_results(responses: list[str]) -> str:
    return "\n\n".join(f"🔹 {resp}" for resp in responses)
