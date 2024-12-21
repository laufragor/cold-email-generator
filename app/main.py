import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Email Generator")
    url_input = st.text_input("Enter a URL:", value="https://jobs.apple.com/en-us/details/200579396/aiml-sr-full-stack-engineer-data-and-ml-innovation")
    submit_btn = st.button("Submit")

    if submit_btn:
        with st.spinner("Processing your request! Please wait."):
            try:
                loader = WebBaseLoader(url_input)
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)

                for job in jobs:
                    skills = job.get("skills", [])
                    links = portfolio.query_links(skills)
                    email = llm.write_email(job, links)
                    st.text(email)

            except Exception as e:
                st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)