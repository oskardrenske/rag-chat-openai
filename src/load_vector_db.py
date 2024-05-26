import sys
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from loguru import logger
import settings


class VectorDBLoader:
    def __init__(self):
        self.filename = sys.argv[1]
        self.docs = None
        logger.info(f"Loading {self.filename}")

    def prepare_data_from_text_file(self):
        # Load the document, split it into chunks, embed each chunk and load it into the vector store.
        raw_documents = TextLoader(self.filename, encoding="utf8").load()
        text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=0)
        self.docs = text_splitter.split_documents(raw_documents)
        logger.info(f"Prepared {len(self.docs)} documents")

    def load_data_into_database(self):
        logger.info(f"Loading {len(self.docs)} documents into database")
        Chroma.from_documents(
            self.docs, OpenAIEmbeddings(), persist_directory=settings.DB_DIRECTORY
        )
        logger.info(f"Loaded {len(self.docs)} documents")


if __name__ == "__main__":
    vectordb_loader = VectorDBLoader()
    vectordb_loader.prepare_data_from_text_file()
    vectordb_loader.load_data_into_database()
