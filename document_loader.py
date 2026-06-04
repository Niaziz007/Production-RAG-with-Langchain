import os
import tempfile
from pathlib import Path
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

def load_text_file_documents(file_path, encoding="utf-8"):
    """Load a text file into a list of Documents.

    Replaces the deprecated langchain_community TextLoader, which has no
    standalone successor package (langchain-community was sunset; see
    https://github.com/langchain-ai/langchain-community/issues/674).
    """
    text = Path(file_path).read_text(encoding=encoding) 
    return [Document(page_content=text, metadata={"source": str(file_path)})]

def load_text_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"This is a sample text file for testing.")
        temp_file_path = temp_file.name

    try:
        documents = load_text_file_documents(temp_file_path)
        print(f"Loaded document content: {documents[0].page_content}")
        
        for doc in documents:
            print("Document Content:")
            print(doc)
            print(f"Document content: {doc.page_content}")
    finally:
        os.remove(temp_file_path)


if __name__ == "__main__":
    load_text_file()