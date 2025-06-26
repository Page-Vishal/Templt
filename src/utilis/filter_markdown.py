import regex as re

def remove_backticks_and_json(text):
    """
    Removes backticks (`) and the word "json" (case-insensitive) from a string.
    """
    try:
        pattern = r"[`]|json"
        return re.sub(pattern, "", text, flags=re.IGNORECASE)
    except Exception as e:
        print("Error on Formatting")