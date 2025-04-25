import streamlit as st
import re

st.set_page_config(page_title= "Password Strength Meter", page_icon="🔑")

st.title("🔐 Password Strength Meter")

st.markdown("""
## Welcome to the ultimate password strength checker!👋  
This tool will help you keep your passwords strong and secure. Just enter your password and we'll give
            you a score based on its strength and helpful suggestions to make your password stronger. The higher the score, the stronger your password! 💪""")

password = st.text_input("Enter your password",type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("⚠️Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) :
        score += 1
    else :
        feedback.append("⚠️Password should have at least one uppercase and one lowercase letter.")

    if re.search(r'\d', password) :
        score += 1
    else :
        feedback.append("⚠️Password should have at least one digit.")

    if re.search(r'[!£$&#@/]', password) :
        score += 1
    else :
        feedback.append("⚠️Password should have at least one special character (!£$&#@/).")

    if score == 4 :
        feedback.append("✅ 🟢Your password is strong! 💪🏻🙌")
    elif score == 3 :
        feedback.append("⚠️ 🟡Your password is good, but can be stronger. Try to add a special character or a digit.")
    else :
        feedback.append("⚠️ 🔴Your password is weak!, please make it stronger by adding a special character and a digit")
        
    if feedback :
        st.markdown("## Improvement Suggestions")  
        for tip in feedback :
            st.write(tip)
            
else :
    st.write("🥺Please enter a password to check its strength.")





