def input_formatter(user_input: str) -> str:
    if len(user_input) > 7 or len(user_input.split()) < 1:
        # not a command
        return user_input

    user_input = user_input.lower()
    # Remove quotes
    user_input = user_input.replace('"', "").replace("'", "")
    user_input = user_input.strip()
    return user_input
