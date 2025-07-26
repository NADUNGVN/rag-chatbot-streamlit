<<<<<<< HEAD
# 🤖 RAG Chatbot Hành Chính Công (Tiếng Việt)

Hệ thống trợ lý AI trả lời tự động về **thủ tục hành chính công** bằng cách sử dụng các văn bản hướng dẫn có sẵn (PDF). Dựa trên mô hình RAG (Retrieval-Augmented Generation) với HuggingFace + LangChain + Groq API.

---

## 🗂️ Cấu trúc thư mục

rag_chatbot_project/

├── data/
│   ├── raw_pdfs/                 # File PDF gốc tải lên
│   └── processed_data/           # Dữ liệu xử lý (Vector Database)
├── src/
│   ├── __init__.py 
│   ├── data_manager.py           # Quản lý dữ liệu (thêm/xóa/xem PDF)
│   ├── embeddings_manager.py     # Xử lý embedding và lưu vector
│   ├── retrieval.py              # Xử lý truy vấn dữ liệu
│   ├── chatbot.py                # Khởi tạo và quản lý chatbot (RAG chain)
│   ├── logging_manager.py        # Ghi log và theo dõi hệ thống
│   └── config.py                 # Quản lý cấu hình hệ thống
├── web_app/
│   ├── app.py                    # Streamlit app
│   └── utils.py                  # Các hàm tiện ích UI
├── logs/                         # File log (Excel, text, ...)
├── images/                       # Assets (logo, hình ảnh...)
├── requirements.txt              # Quản lý thư viện, dependencies
└── README.md


---

## ✅ Yêu cầu hệ thống

- Python 3.9+
- API Key từ [Groq](https://console.groq.com/)
- Cài đặt thư viện:

```bash
pip install -r requirements.txt
=======
# rag-chatbot-streamlit
>>>>>>> d4c18af520f77bceccc92fa70af1a74585ea62f9
