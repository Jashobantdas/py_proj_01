from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

class ProcessVectors:
    def __init__(self):
        self.text_spliter = RecursiveCharacterTextSplitter( chunk_size=500, chunk_overlap=100 )
        self.embeddings = HuggingFaceEmbeddings( model_name="sentence-transformers/all-MiniLM-L6-v2" )
        self.vector_store = Chroma(collection_name= "documents", embedding_function= self.embeddings, persist_directory= "./chroma_db")

    def extract_pdf_pages(file_path: str, document_id: int, tenant_id: int, file_name: str, document_type: str) -> list[Document]:

        documents = []
        reader = PdfReader(file_path)

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""

            if not text.strip():
                continue

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "document_id": document_id,
                        "tenant_id": tenant_id,
                        "file_name": file_name,
                        "document_type": document_type,
                        "source": file_path,
                        "page_number": page_number
                    }
                )
            )

        return documents

    def chunk_each_page(self, documents: list[Document], chunk_size: int) -> list[list[Document]]:
        chunks = []
        for page_document in documents:
            chunk_spliter = self.text_spliter.split_documents(page_document)
            chunks.extend(chunk_spliter)

        return chunks

    # save chunks to vector db
    def save_chunks(self, chunks: list[list[Document]]):
        self.vector_store.add_documents(chunks)

    def search_vectors(self, qustions: str):
        results = self.vector_store.similarity_search(
            "What is the annual leave policy?",
            k=5,
            filter={
                "tenant_id": 1
            }
        )

        return results
