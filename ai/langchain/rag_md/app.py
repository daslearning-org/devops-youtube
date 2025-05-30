from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from vector import md_rag
import os

ollama_url = os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")
model = OllamaLLM(model="llama3.2", base_url=ollama_url)

template = """
You are an exeprt in answering technical questions and you will get answers from the Markdown files.

Here are some relevant documents: {documents}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

md_files = "./markdown_files"
retriever = md_rag(source_directory=md_files, db_path="chroma_md_db", collection_name="law_files")
print("Retriever ready.")

while True:
    print("\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(f"AI: {result}")
