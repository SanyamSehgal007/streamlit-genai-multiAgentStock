from crewai import Task
from agents.analyst_agent import analyst_agent


get_stock_analysis = Task(
    description=(
        "Analyze the recent performance of the stock: {stock}. Use the live stock information tool to retrieve "
        "current price, percentage change, trading volume, and other market data. Provide a summary of how the stock "
        "is performing today and highlight any key observations from the data."
    ),
    expected_output=(
    "Provide ONLY the most important insights in BULLET POINTS.\n\n"
    "Rules:\n"
    "- Maximum 5 bullet points\n"
    "- Each bullet point must be 1 line only\n"
    "- No explanations, no paragraphs\n"
    "- Focus only on actionable or meaningful insights\n\n"
    "Bullet points should include:\n"
    "- Current stock price\n"
    "- Daily % change\n"
    "- Key trend or signal\n"
    "- Any unusual movement (if any)"
),
    agent=analyst_agent
)