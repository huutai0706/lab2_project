import streamlit as st
import pyrebase
import requests

# 1. CẤU HÌNH FIREBASE (Thay thế bằng config của bạn)
firebaseConfig = {
  "apiKey": "AIzaSyC-_UdI7P8iIpi7bYzwmUIFykmtzSTktt0",
  "authDomain": "lab2-noteapp-43f03.firebaseapp.com",
  "projectId": "lab2-noteapp-43f03",
  "storageBucket": "lab2-noteapp-43f03.firebasestorage.app",
  "messagingSenderId": "954769855143",
  "appId": "1:954769855143:web:358634cfd784ac2cf58182",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

BACKEND_URL = "http://127.0.0.1:8000"

# 2. KHỞI TẠO SESSION STATE
if "user" not in st.session_state:
    st.session_state.user = None

def login():
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        st.session_state.user = user
        st.success("Đăng nhập thành công!")
        st.rerun()
    except Exception as e:
        st.error("Đăng nhập thất bại. Vui lòng kiểm tra lại thông tin.")

def signup():
    try:
        user = auth.create_user_with_email_and_password(email, password)
        st.success("Tạo tài khoản thành công! Vui lòng đăng nhập.")
    except Exception as e:
        st.error("Tạo tài khoản thất bại.")

def logout():
    st.session_state.user = None
    st.rerun()

# 3. GIAO DIỆN CHÍNH
st.title("Ứng dụng Ghi chú (Note App)")

# KHU VỰC ĐĂNG NHẬP / ĐĂNG KÝ
if st.session_state.user is None:
    st.subheader("Đăng nhập / Đăng ký")
    email = st.text_input("Email")
    password = st.text_input("Mật khẩu", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Đăng nhập"):
            login()
    with col2:
        if st.button("Đăng ký"):
            signup()

# KHU VỰC TÍNH NĂNG CHÍNH (Sau khi đăng nhập)
else:
    user_email = st.session_state.user['email']
    st.write(f"Xin chào, **{user_email}**")
    if st.button("Đăng xuất"):
        logout()
        
    st.divider()
    
    # Thêm ghi chú mới
    st.subheader("Thêm ghi chú")
    new_note = st.text_area("Nội dung ghi chú:")
    if st.button("Lưu ghi chú"):
        if new_note:
            payload = {"user_email": user_email, "content": new_note}
            res = requests.post(f"{BACKEND_URL}/notes", json=payload)
            if res.status_code == 200:
                st.success("Đã lưu!")
            else:
                st.error("Lỗi khi lưu!")
        else:
            st.warning("Vui lòng nhập nội dung.")

    st.divider()

    # Hiển thị ghi chú đã lưu
    st.subheader("Danh sách ghi chú của bạn")
    res = requests.get(f"{BACKEND_URL}/notes", params={"user_email": user_email})
    if res.status_code == 200:
        notes = res.json()
        if len(notes) == 0:
            st.info("Chưa có ghi chú nào.")
        else:
            for n in notes:
                st.info(n['content'])