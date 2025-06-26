import yaml

with open("src/config/prompts.yaml", "r") as f:
    prompt_config = yaml.safe_load(f)

def load_prompt():
    sys_prompt = prompt_config["sys_prompt_pdf"]

    return sys_prompt