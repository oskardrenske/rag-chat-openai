import time
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferMemory

from loguru import logger

from src.templates import template
from src import settings


class OpenAIClient:
    def __init__(self):
        logger.info("start")
        self.check()

        self.vector_db = Chroma(
            persist_directory=settings.DB_DIRECTORY,
            embedding_function=OpenAIEmbeddings(),
        )
        self.llm = ChatOpenAI(
            model_name=settings.LLM_MODEL, temperature=settings.LLM_TEMP
        )
        self.prompt = PromptTemplate.from_template(template)
        self.memory = ConversationBufferMemory()

    def check(self):
        if settings.OPENAI_API_KEY is None:
            raise ValueError("OPENAI_API_KEY environment variable is not set")

    def send_query(self, query: str) -> dict:
        qa_chain = (
            {
                "context": self.vector_db.as_retriever(
                    search_kwargs={"k": settings.DOC_COUNT}
                ),
                "question": RunnablePassthrough(),
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

        logger.debug(f"Query: {query}")
        start_time = time.time()
        answer = qa_chain.invoke(query)
        end_time = time.time()
        elapsed_time = int(end_time - start_time)
        logger.debug(elapsed_time)
        logger.debug(f"Answer: {answer}")
        return {"answer": answer, "elapsed_time": elapsed_time}
