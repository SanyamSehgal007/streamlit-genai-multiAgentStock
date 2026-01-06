from crewai import Task
from agents.trader_agent import trader_agent

trade_decision = Task(
    description=(
        "Use live market data and stock performance indicators for {stock} to make a strategic trading decision. "
        "Assess key factors such as current price, daily change percentage, volume trends, and recent momentum. "
        "Based on your analysis, recommend whether to **Buy**, **Sell**, or **Hold** the stock."
    ),
    expected_output=(
    "Provide a FINAL trading decision in BULLET POINTS.\n\n"
    "Rules:\n"
    "- Maximum 4 bullet points\n"
    "- First bullet MUST be: Buy / Sell / Hold\n"
    "- Each bullet point must be short (1 line)\n"
    "- No reasoning paragraphs\n\n"
    "Bullet points should include:\n"
    "- Recommendation (Buy/Sell/Hold)\n"
    "- Key price signal\n"
    "- Risk consideration\n"
    "- Short justification"
)
,
    agent=trader_agent
)