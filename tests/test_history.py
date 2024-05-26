import unittest

from src.chat_history import ChatHistory


class TestChatHistory(unittest.TestCase):
    def test_add_to_history(self):
        ch = ChatHistory()
        for word in ["italien", "platsbiljett", "supplemento", "gelato"]:
            ch.add_to_history(word)
        assert ch.history_as_string() == "platsbiljett supplemento gelato"

    def test_rewrite(self):
        ch = ChatHistory()
        ch.add_to_history("cabelho")
        query = "hur reser jag till portugal?"
        result = ch.add_history_to_query(query)
        assert result == "hur reser jag till portugal? cabelho"

    def test_clear_history(self):
        ch = ChatHistory()
        ch.add_to_history("cabelho")
        ch.clear_history()
        assert ch.history_as_string() == ""


if __name__ == "__main__":
    unittest.main()
