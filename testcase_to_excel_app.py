import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Testcase to Excel", layout="centered")

st.title("🧪 Chuyển Testcase (từ Claude) thành File Excel")

st.markdown("""
### 📋 Bước 1: Dán nội dung testcase
Nội dung nên theo định dạng như sau (từ Claude):

