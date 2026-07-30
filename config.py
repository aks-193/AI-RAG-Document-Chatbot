import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "openai/gpt-oss-20b:free"

api_key = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")

if not api_key:
    st.error("❌ OpenRouter API key not found.")
    st.stop()

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)
