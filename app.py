import streamlit as st
from main import run

st.set_page_config(page_title="AI Stock Analyst", page_icon="📈")

st.title("📈 Multi-Agent AI Stock Analysis")
st.markdown(
    "Powered by **CrewAI + Groq LLaMA-3.3-70B**\n\n"
    "Enter a stock ticker (e.g. `AAPL`, `TSLA`, `MSFT`) to get:\n"
    "- Live stock analysis\n"
    "- Trading recommendation (Buy / Sell / Hold)"
)

# Input
stock_symbol = st.text_input(
    "Enter stock ticker",
    placeholder="TSLA"
).strip().upper()

# Button
if st.button("Analyze Stock 🚀"):
    if not stock_symbol:
        st.warning("Please enter a stock symbol.")
    else:
        with st.spinner("Running multi-agent analysis..."):
            result = run(stock_symbol)

        st.success("Analysis complete!")

        # Final Output
        st.markdown("## 📊 Final Recommendation")
        st.markdown(result)

        # Optional: verbose logs
        with st.expander("🔍 Agent Reasoning & Logs"):
            st.text(result)
