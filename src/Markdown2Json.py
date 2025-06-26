from src.config.config_openai import client
from src.config.load_prompt import load_prompt

sys_prompt = load_prompt()

def make_template(content: str):
    """
    Generates JSON template from Markdown content

    Args:
        content: Markdown text content
        
    Returns:
        str: Generated JSON template
    """
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user"  , "content": f"{content}"}
            ]
        )

        template = response.choices[0].message.content
        return template
    except Exception as e:
        return f"Error on making template"