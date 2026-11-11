import streamlit as st
from src.scorer import get_risk

st.set_page_config(page_title="ScamShield", page_icon="🛡️")

st.title("🛡️ ScamShield: Fake Job Detector")
st.write("Paste a job message, email or offer letter. We will check if it looks like a scam.")

text = st.text_area("Paste the job message here", height=250)

if st.button("Check Now"):
    if not text.strip():
        st.warning("Please paste some text first.")
    else:
        result = get_risk(text)
        level = result["level"]
        title = f"Risk: {level} ({result['score']}/100)"

        if level == "High":
            st.error(title)
        elif level == "Medium":
            st.warning(title)
        else:
            st.success(title)

        st.progress(result["score"] / 100)

        if result["reasons"]:
            st.subheader("Red flags found")
            for reason in result["reasons"]:
                st.write("- " + reason)
        else:
            st.write("No red flags found by the rules.")

        st.write(f"ML model scam chance: **{result['ml_percent']}%**")

st.caption("This tool gives guidance only. Always verify the company on its official website.")