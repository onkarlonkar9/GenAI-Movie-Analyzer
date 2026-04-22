from dotenv import load_dotenv
import os
import streamlit as st
from pydantic import BaseModel
from typing import List

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

st.set_page_config(page_title="Movie Analyzer", layout="centered")

st.title("🎬Movie Analyzer")

movie_text = st.text_area("Movie Description", height=200)

llm = ChatMistralAI(
    model="mistral-small-2506",
    api_key=os.getenv("MISTRAL_API_KEY")
)

class Movie(BaseModel):
    movie_name: str
    cast: List[str]
    genre: str
    rating: str
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract movie details."),
    ("user", """
{format_instructions}

{input}
""")
])

if st.button("Analyze"):
    messages = prompt.format_messages(
        input=movie_text,
        format_instructions=parser.get_format_instructions()
    )

    response = llm.invoke(messages)
    data = parser.parse(response.content)

    st.json(data.model_dump())