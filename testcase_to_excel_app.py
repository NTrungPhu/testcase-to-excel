import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Testcase to Excel", layout="centered")

st.title("🧪 Chuyển Testcase (từ Claude) thành File Excel")

st.markdown("""
### 📋 Bước 1: Dán nội dung testcase
Nội dung nên theo định dạng như sau (từ Claude):
""")

testcase_text = st.text_area("📥 Dán nội dung testcase tại đây", height=300)

def parse_table_to_df(text):
    lines = [line.strip() for line in text.strip().split("\n") if "|" in line]
    if len(lines) < 2:
        return None
    header = [h.strip() for h in lines[0].split("|")[1:-1]]
    rows = []
    for line in lines[2:]:
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) == len(header):
            rows.append(cols)
    df = pd.DataFrame(rows, columns=header)
    return df

if st.button("📤 Tạo file Excel"):
    df = parse_table_to_df(testcase_text)
    if df is not None:
        output = io.BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        st.success("✅ File Excel đã sẵn sàng!")
        st.download_button(
            label="⬇️ Tải file Excel",
            data=output.getvalue(),
            file_name="testcases.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.error("❌ Không thể đọc được dữ liệu từ bảng bạn dán. Vui lòng kiểm tra định dạng.")
