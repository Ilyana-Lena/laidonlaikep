import streamlit as st

# Tạo 2 cột: Cột 1 chứa ảnh (tỉ lệ 1), Cột 2 chứa tiêu đề (tỉ lệ 5)
col1, col2 = st.columns([1, 5])

with col1:
    # Đảm bảo file 'Logo.png' nằm cùng thư mục với file code (app.py)
    # Nếu file nằm trong thư mục khác, ví dụ 'images/Logo.png', hãy sửa lại đường dẫn
    st.image("Logo.png", width=100)

with col2:
    # Căn chỉnh tiêu đề cho hài hòa với vị trí ảnh
    st.markdown("<br>", unsafe_allow_html=True) # Tạo khoảng trống phía trên
    st.title("Ứng dụng tính tiền gửi tiết kiệm")   

# Nhập dữ liệu
C = st.number_input(
    "Nhập số tiền khách hàng gửi tiết kiệm (triệu đồng)",
    min_value=0.0,
    value=100.0
)

i = st.number_input(
    "Nhập lãi suất gửi tiết kiệm theo năm (%)",
    min_value=0.0,
    value=6.0
)

n = st.number_input(
    "Nhập số tháng khách hàng gửi tiết kiệm",
    min_value=1,
    value=12
)

# Đổi lãi suất từ % sang số thập phân
i = i / 100

# Nút tính toán
if st.button("Tính toán"):
    
    # Lãi đơn
    An = C * (1 + (i / 12) * n)

    # Lãi kép
    Bn = C * (1 + i / 12) ** n

    st.success("Kết quả tính toán")

    st.write(
        f"📌 Số tiền khách hàng nhận được theo lãi đơn: **{An:,.2f} triệu đồng**"
    )

    st.write(
        f"📌 Số tiền khách hàng nhận được theo lãi kép: **{Bn:,.2f} triệu đồng**"
    )
