from app.agents.manager_agent import (
    ManagerAgent
)


def analyze_dataframe(df):

    manager = ManagerAgent()

    return manager.run(df)