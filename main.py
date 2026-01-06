
from crew import stock_crew




def run(stock: str):
    result = stock_crew.kickoff(inputs={"stock": stock})
    return result


