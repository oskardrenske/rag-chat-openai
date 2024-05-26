from src import settings
from src import messages
from src import chat_history_writer


class ChatHistory:
    """
    This class handles the query history
    The last n queries (defined by environment variable CHAT_HISTORY_MAX_LENGTH in settings.py) are saved.
    FIFO, when queue length is exceeded, the oldest is removed
    """

    def __init__(self):
        self.history = []
        self.chat_log_writer = chat_history_writer.WriteChatToFile()

    def add_to_history(self, word):
        """
        Add the latest query to the history
        If the length set by CHAT_HISTORY_MAX_LENGTH is exceeded, the oldest is removed
        :param word:
        :return:
        """
        if len(self.history) >= settings.CHAT_HISTORY_MAX_LENGTH:
            self.history.pop(0)
        self.history.append(word)

    def history_as_string(self) -> str:
        """
        Formats the list of query history as a string
        :return:
        """
        return " ".join(self.history)

    def add_history_to_query(self, query) -> str:
        """
        Adds query history as a string of queries to the current query
        :param query: str
        :return: A string built from the latest query with query history appended
        """
        query_with_history = query + " " + self.history_as_string()
        return query_with_history

    def clear_history(self) -> None:
        """
        Empties the history to avoid sending old queries when the subject changes
        A message is written to the chat log file to assist troubleshooting
        :return: None
        """
        self.history = []
        self.chat_log_writer.write_message(messages.query_history_deleted)

    def write_history(self, query: str, answer: str, elapsed_time: int) -> None:
        """
        Writes the query, answer and how loong it took to execute (seconds) to the chat log file
        :param query: str
        :param answer: str
        :param elapsed_time: int
        :return: None
        """
        self.chat_log_writer.write_query_answer_to_file(query, answer, elapsed_time)
