# [LAB 2] Application Programming Interface and Firebase Studio

**Môn học:** Tư duy tính toán  
**Sinh viên thực hiện:** Phạm Văn Hữu Tài (MSSV: 24120435)  
**Dự án:** Ứng dụng Ghi chú (Note App) tích hợp FastAPI, Streamlit và Firebase.

## 🔗 Link Video Demo
> **[CHÈN LINK VIDEO YOUTUBE HOẶC GOOGLE DRIVE CỦA BẠN VÀO ĐÂY]**

---

## 🛠 Hướng dẫn cài đặt môi trường (Environment Setup)

Dự án này sử dụng Python. Để đảm bảo ứng dụng chạy mượt mà không bị xung đột thư viện, vui lòng thiết lập môi trường ảo (`venv`) trước khi khởi chạy.

**1. Khởi tạo môi trường ảo (Tạo thư mục `.venv`)**
* Mở Terminal tại thư mục gốc của dự án (`lab2_project`) và chạy lệnh:
```bash
python -m venv .venv
```
**2. Kích hoạt môi trường ảo**
* Trên Windows (PowerShell/Command Prompt):
```bash
.\.venv\Scripts\activate
```
**3. Cài đặt các thư viện cần thiết**
Ứng dụng được chia thành hai phần độc lập là backend và frontend. Bạn cần cài đặt thư viện cho cả hai phần:
* Cài đặt thư viện Backend:
```bash
cd backend
pip install -r requirements.txt
```
* Cài đặt thư viện Frontend:
```bash
cd ../frontend
pip install -r requirements.txt
```
## 🚀 Hướng dẫn chạy ứng dụng
* Để ứng dụng hoạt động đầy đủ, bạn cần mở 2 cửa sổ Terminal hoạt động song song (một cho Backend và một cho Frontend) và đảm bảo cả 2 đều đã kích hoạt môi trường ảo (.venv).

**1. Khởi chạy Backend (FastAPI)**
* Backend đóng vai trò xử lý logic, giao tiếp với database SQLite và cung cấp các API endpoint.

* Mở Terminal 1, di chuyển vào thư mục backend và chạy lệnh:
```bash
cd backend
python -m uvicorn main:app --reload
```
- Dấu hiệu thành công: Terminal hiển thị Uvicorn running on http://127.0.0.1:8000. Hãy giữ nguyên Terminal này.
**2. Khởi chạy Frontend (Streamlit)**
* Frontend cung cấp giao diện người dùng và tích hợp Firebase Authentication để đăng nhập.

* Mở Terminal 2, di chuyển vào thư mục frontend và chạy lệnh:
```bash
cd frontend
python -m streamlit run app.py
```
Dấu hiệu thành công: Trình duyệt web sẽ tự động mở tab mới tại địa chỉ http://localhost:8501 hiển thị giao diện của Ứng dụng Ghi chú.

## ✨ Tính năng chính (Main Features)
* Xác thực người dùng: Đăng ký và đăng nhập sử dụng Firebase Authentication (Email/Password).

* Quản lý ghi chú: Người dùng có thể tạo ghi chú mới và xem lại toàn bộ danh sách ghi chú của cá nhân mình. Dữ liệu được lưu trữ thông qua API của FastAPI xuống database SQLite.