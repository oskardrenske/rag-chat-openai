from src import settings


query_history_deleted = "Query history deleted"

CHAT_MESSAGE = "Your question ('help' to see available commands): "
CHAT_HELP = "Available commands:\n'quit' to exit the program\n'clear' to delete query history\n'help' to display this help message"

CHAT_START_MESSAGE = f"""Write your question about the subject in the provided data.\n
Query history includes the last {settings.CHAT_HISTORY_MAX_LENGTH} questions\n 
{CHAT_HELP} 
 """
