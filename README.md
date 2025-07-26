Dự án RAG Chatbot (Retrieval-Augmented Generation Chatbot)
Giới thiệu
Dự án này phát triển một Chatbot sử dụng kiến trúc Retrieval-Augmented Generation (RAG), cho phép người dùng tương tác và trích xuất thông tin từ các tệp PDF gốc được tải lên. Chatbot được thiết kế để cung cấp câu trả lời chính xác và có ngữ cảnh bằng cách truy vấn một cơ sở dữ liệu vector được tạo từ các tài liệu đã xử lý.

Tính năng chính
Quản lý dữ liệu PDF: Thêm, xóa và xem các tệp PDF gốc.

Xử lý Embedding: Chuyển đổi nội dung PDF thành các vector nhúng và lưu trữ vào cơ sở dữ liệu vector (FAISS hoặc tương tự).

Truy vấn thông minh: Sử dụng kỹ thuật Retrieval để tìm kiếm các đoạn văn bản liên quan nhất từ cơ sở dữ liệu vector dựa trên câu hỏi của người dùng.

Tạo phản hồi: Tích hợp với mô hình ngôn ngữ lớn (LLM) để tạo ra câu trả lời tự nhiên và chính xác, được tăng cường bởi thông tin đã truy xuất.

Giao diện người dùng thân thiện: Ứng dụng web được xây dựng bằng Streamlit giúp người dùng dễ dàng tương tác.

Ghi Log: Hệ thống ghi log chi tiết để theo dõi hoạt động và gỡ lỗi.

Cấu hình linh hoạt: Dễ dàng tùy chỉnh các thiết lập hệ thống thông qua tệp cấu hình.

Cấu trúc dự án
Dưới đây là cấu trúc thư mục của dự án:

rag_chatbot_project/
├── data/
│   ├── raw_pdfs/                 # File PDF gốc tải lên
│   └── processed_data/           # Dữ liệu xử lý (Vector Database)
├── src/
│   ├── __init__.py               # Gói Python
│   ├── data_manager.py           # Quản lý dữ liệu (thêm/xóa/xem PDF)
│   ├── embeddings_manager.py     # Xử lý embedding và lưu vector
│   ├── retrieval.py              # Xử lý truy vấn dữ liệu
│   ├── chatbot.py                # Khởi tạo và quản lý chatbot (RAG chain)
│   ├── logging_manager.py        # Ghi log và theo dõi hệ thống
│   └── config.py                 # Quản lý cấu hình hệ thống
├── web_app/
│   ├── app.py                    # Streamlit app
│   └── utils.py                  # Các hàm tiện ích UI
├── logs/                         # File log (Excel, text, ...)
├── images/                       # Assets (logo, hình ảnh...)
├── requirements.txt              # Quản lý thư viện, dependencies
└── README.md                     # File README của dự án

Cài đặt
Để thiết lập và chạy dự án này trên máy cục bộ của bạn, hãy làm theo các bước sau:

1. Clone Repository
Mở terminal hoặc command prompt và clone repository:

git clone <URL_CUA_REPOSITORY_CUA_BAN>
cd rag_chatbot_project

2. Tạo Môi trường ảo (khuyến nghị)
Tạo một môi trường ảo để quản lý các thư viện phụ thuộc:

python -m venv venv

Kích hoạt môi trường ảo:

Trên Windows:

.\venv\Scripts\activate

Trên macOS/Linux:

source venv/bin/activate

3. Cài đặt các thư viện phụ thuộc
Sau khi kích hoạt môi trường ảo, cài đặt tất cả các thư viện cần thiết từ requirements.txt:

pip install -r requirements.txt

4. Cấu hình API Key (nếu cần)
Nếu bạn sử dụng các dịch vụ LLM yêu cầu API Key (ví dụ: OpenAI, Google Gemini), hãy cập nhật tệp src/config.py với API Key của bạn. Bạn có thể cần thiết lập biến môi trường hoặc trực tiếp thêm vào tệp cấu hình (tùy thuộc vào cách bạn triển khai).

# src/config.py
# Ví dụ:
OPENAI_API_KEY = "your_openai_api_key_here"
# hoặc
GEMINI_API_KEY = "your_gemini_api_key_here"

Cách sử dụng
1. Chuẩn bị dữ liệu PDF
Đặt các tệp PDF gốc của bạn vào thư mục data/raw_pdfs/.

2. Chạy ứng dụng web Streamlit
Từ thư mục gốc của dự án (rag_chatbot_project/), chạy ứng dụng Streamlit:

streamlit run web_app/app.py

Lệnh này sẽ mở ứng dụng web trong trình duyệt mặc định của bạn (thường là http://localhost:8501).

3. Tương tác với Chatbot
Tải lên PDF: Sử dụng giao diện người dùng để tải lên các tệp PDF mới.

Xử lý dữ liệu: Ứng dụng sẽ tự động xử lý các tệp PDF đã tải lên, tạo embedding và lưu vào data/processed_data/.

Đặt câu hỏi: Nhập câu hỏi của bạn vào khung chat và nhận câu trả lời từ chatbot.

Cấu hình
Tệp src/config.py chứa các cài đặt quan trọng cho dự án, bao gồm:

Đường dẫn thư mục dữ liệu.

Cài đặt mô hình Embedding.

Cài đặt mô hình ngôn ngữ lớn (LLM).

Các tùy chọn ghi log.

Bạn có thể chỉnh sửa tệp này để tùy chỉnh hành vi của chatbot.

Ghi log
Tất cả các hoạt động quan trọng của hệ thống sẽ được ghi lại trong thư mục logs/. Bạn có thể kiểm tra các tệp log để theo dõi hiệu suất, gỡ lỗi hoặc phân tích các tương tác của người dùng.

Đóng góp
Đóng góp vào dự án này luôn được hoan nghênh! Nếu bạn muốn đóng góp, vui lòng làm theo các bước sau:

Fork repository này.

Tạo một nhánh mới cho tính năng của bạn (git checkout -b feature/AmazingFeature).

Thực hiện các thay đổi của bạn.

Commit các thay đổi của bạn (git commit -m 'Add some AmazingFeature').

Push lên nhánh của bạn (git push origin feature/AmazingFeature).

Mở một Pull Request.

Giấy phép
Dự án này được cấp phép dưới Giấy phép MIT. Xem tệp LICENSE (nếu có) để biết thêm chi tiết.

Lưu ý: Thay thế <URL_CUA_REPOSITORY_CUA_BAN> bằng URL thực tế của repository GitHub của bạn.
