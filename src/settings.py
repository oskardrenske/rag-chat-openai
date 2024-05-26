import os
import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent.resolve()

DB_DIRECTORY = os.path.join(ROOT_DIR, str(ROOT_DIR / "db"))

default_chat_logs_dir = str(ROOT_DIR / "chat_logs")
CHAT_LOGS_DIRECTORY = os.environ.get("CHAT_LOGS_DIRECTORY", default_chat_logs_dir)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)
LLM_TEMP = os.environ.get("LLM_TEMP", 0.1)
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4-turbo")
DOC_COUNT = os.environ.get("DOC_COUNT", 10)

default_result_file = str(ROOT_DIR / "chat_logs" / "questions-answers.txt")
RESULT_FILE = os.environ.get("RESULT_FILE", default_result_file)

CHAT_HISTORY_MAX_LENGTH = os.environ.get("CHAT_HISTORY_MAX_LENGTH", 3)


os.environ["LOGURU_LEVEL"] = "INFO"
