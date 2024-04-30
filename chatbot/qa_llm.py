from langchain.chains.openai_functions.openapi import get_openapi_chain

chain = get_openapi_chain(
    "https://data.worldbank.org/indicator/SI.POV.DDAY?end=2022&locations=1W-BR&start=1981"
)
chain("What was the poverty headcount ratio a day in Brazil in 2017?")