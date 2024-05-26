import datetime
import pathlib

from src import settings


class WriteChatToFile:
    """
    This class handles the writing of chat history to a file.
    Use environment variable CHAT_HISTORY_MAX_LENGTH to set the maximum length of chat history.
    See settings.py for more related environment variables.
    A new file will be created when the program starts
    """

    def __init__(self):
        self.current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.log_file_name = (
            f"{settings.CHAT_LOGS_DIRECTORY}/chat_logs{self.current_time}.txt"
        )
        self.prepare_directory()

    def prepare_directory(self) -> None:
        """
        Creates the directory if it doesn't exist.
        Directory name is controlled by an environment variable. See settings.py for more related environment variables.'
        :return: None
        """
        p = pathlib.Path(settings.CHAT_LOGS_DIRECTORY)
        p.mkdir(parents=True, exist_ok=True)

    def _write_to_file(self, message: str) -> None:
        """
        Appendes the message to the chat history file
        :param message: A message to be appended to the chat history file, terminated by a line break.
        :return:  None
        """
        with open(self.log_file_name, "a", encoding="utf-8") as f:
            f.write(message)

    def write_query_answer_to_file(
        self, query: str, answer: str, elapsed_time: int
    ) -> None:
        """
        Formats the message to be written to the chat history file and a
        Information about elapsed time, LLM temperature and which model was used is also written along with the message
        """
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        diagnostics = f"{current_time} | {settings.LLM_MODEL} | {settings.LLM_TEMP} |{settings.DOC_COUNT} |  {elapsed_time}\n"
        self._write_to_file(diagnostics)
        self._write_to_file(f"Fråga: {query}\nSvar:  {answer}\n\n")

    def write_message(self, message: str) -> None:
        """
        Formats the message to be written to the chat history file.
        Leading and trailing white space characters are first stripped and a single line break is added to the end of the message before writing it to the chat history file.
        :param message: string
        :return: None
        """
        self._write_to_file(f"{message.strip()}\n")
