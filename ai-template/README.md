# 🧠 Ollama AI Environment Variables Template

Use this template to set up the required environment variables for utilizing Ollama AI in your Python script.

## Variables

- `PROJECT_PLANNER_MODEL`: Specifies the model name for the project planner agent. Default value: `dolphin-mistral:latest`.
- `CODER_MODEL`: Specifies the model name for the coder agent. Default value: `codellama:7b`.
- `MARKDOWN_MAKER`: Specifies the model name for the markdown maker agent. Default value: `vicuna:13b-16k`.
- `TASKNAMER`: Specifies the model name for the tasknamer agent. Default value: `stablelm2:1.6b-zephyr-fp16`.

## Usage

1. Copy the template to a file named `.env`.
2. Replace the default values with the desired model names.
3. Save the file in the root directory of your project.
4. Ensure that your Python script reads the environment variables using a library like `dotenv`.

