from modules import input_handler, task_splitter, agent_fabricator, execution_core, synthesizer
import json

def run_system(topic: str):
    clean_topic = input_handler.get_cleaned_input(topic)
    subtasks = task_splitter.split_into_subtasks(clean_topic)
    agents = agent_fabricator.create_agents(subtasks)

    responses = []
    for agent in agents:
        prompt = agent["task"]
        response = execution_core.query_openai(prompt)
        responses.append(response)

    final_output = synthesizer.synthesize_results(responses)

    with open("session_output.json", "w") as f:
        json.dump({
            "topic": topic,
            "subtasks": subtasks,
            "responses": responses,
            "summary": final_output
        }, f, indent=2)

    return final_output
