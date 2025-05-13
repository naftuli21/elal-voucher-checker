import streamlit as st
from datetime import datetime

# Import your voucher checker function here
# from elal_voucher_checker import check_voucher

def fake_check_voucher(first_name, last_name, voucher):
    # Replace this with your real Selenium script call
    return {
        "amount_remaining": "$256.75",
        "expiry_year": 2025,
        "status": "active",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# UI
st.set_page_config(page_title="El Al Voucher Checker")
st.title("🛫 El Al Voucher Checker")

with st.form("voucher_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    voucher = st.text_input("Last 6 digits of Voucher")
    submitted = st.form_submit_button("Check Voucher")

if submitted:
    if not (first_name and last_name and voucher):
        st.warning("Please fill out all fields.")
    else:
        with st.spinner("Checking voucher..."):
            result = fake_check_voucher(first_name, last_name, voucher)

        st.success(f"Voucher Balance: {result['amount_remaining']}")
        st.info(f"Last Checked: {result['timestamp']}")
        if result["expiry_year"] == 2025:
            st.warning("⚠️ This voucher expires in 2025. Use it soon!")
