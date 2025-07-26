import os
import shutil
from typing import List
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from src.config import PDF_RAW_DIR, VECTOR_DB_DIR, EMBEDDING_MODEL_NAME, EMBEDDING_MODEL_KWARGS

# 1. Tải tất cả tài liệu PDF
def load_pdf_documents() -> List:
    loader = DirectoryLoader(
        path=PDF_RAW_DIR,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True
    )
    return loader.load()

# 2. Chia nhỏ nội dung thành từng đoạn
def split_documents(documents: List) -> List:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    return text_splitter.split_documents(documents)

# 3. Tạo và lưu Vector Database
def create_vector_database(chunks: List) -> Chroma:
    # Xoá database cũ nếu có
    if os.path.exists(VECTOR_DB_DIR):
        shutil.rmtree(VECTOR_DB_DIR)
    os.makedirs(VECTOR_DB_DIR, exist_ok=True)

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs=EMBEDDING_MODEL_KWARGS
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_DIR
    )
    vectordb.persist()
    print(f"✅ Vector DB đã tạo từ {len(chunks)} đoạn văn bản.")
    return vectordb

# 4. Tải lại Vector Database nếu đã có
def load_vector_database() -> Chroma:
    if not os.path.exists(VECTOR_DB_DIR):
        raise FileNotFoundError("Vector DB chưa được tạo.")
    
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs=EMBEDDING_MODEL_KWARGS
    )

    return Chroma(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embeddings
    )

# 5. Pipeline toàn diện (gọi khi tạo mới DB)
def rebuild_vector_db():
    print("🔄 Đang xử lý lại toàn bộ cơ sở dữ liệu văn bản...")
    docs = load_pdf_documents()
    chunks = split_documents(docs)
    return create_vector_database(chunks)
