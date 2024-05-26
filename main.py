from src.chat_history import ChatHistory
from src.openai_client import OpenAIClient
from src import messages

llm_client = OpenAIClient()

chat_history = ChatHistory()


def format_user_input(user_input):
    if len(user_input) > 7:
        # not a command
        return user_input
    user_input = user_input.lower()

    # Remove quotes
    user_input = user_input.replace('"', "").replace("'", "")
    user_input = user_input.strip()
    return user_input


print(messages.CHAT_START_MESSAGE)
while True:
    user_input = input(messages.CHAT_MESSAGE)
    if user_input.lower() in ["quit", "'quit'"]:
        break

    if user_input.lower() in ["help", "'help'"]:
        print(messages.CHAT_HELP)
        continue

    if user_input.lower() in ["clear", "'clear'"]:
        chat_history.clear_history()
        print(messages.query_history_deleted)
        continue

    query_with_history = chat_history.add_history_to_query(user_input)

    response = llm_client.send_query(query_with_history)
    print("Svar: \n\n" + response["answer"])
    chat_history.add_to_history(user_input)
    chat_history.write_history(
        query=user_input,
        answer=response["answer"],
        elapsed_time=response["elapsed_time"],
    )
