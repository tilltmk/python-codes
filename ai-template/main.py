import json
import os
import sys
import traceback
import ollama
import dotenv

dotenv.load_dotenv()  # Load environment variables
PROJECT_PLANNER_MODEL = os.getenv("PROJECT_PLANNER_MODEL", "dolphin-mistral:latest")
CODER_MODEL = os.getenv("CODER_MODEL", "codellama:7b")
MARKDOWN_MAKER = os.getenv("CODER_MODEL", "vicuna:13b-16k")
TASKNAMER = os.getenv("TASKNAMER", "stablelm2:1.6b-zephyr-fp16")

def generate_answers(agent, prompt):
    model_name = ""
    if agent == 'project_planner':
        model_name = PROJECT_PLANNER_MODEL
    elif agent == 'coder':
        model_name = CODER_MODEL
    elif agent == 'markdown':
        model_name = MARKDOWN_MAKER
    elif agent == 'taskname':
        model_name = TASKNAMER
    if not model_name:
        raise ValueError("Model name is not specified in the environment variables or defaults are missing.")
    messages = [
        {
            'role': 'user',
            'content': prompt,
        },
    ]
    try:
        response = ollama.chat(model=model_name, messages=messages)
        return response['message']['content']
    except Exception as e:
        print(f"There was an error communicating with the Ollama model: {e}")
        return None
