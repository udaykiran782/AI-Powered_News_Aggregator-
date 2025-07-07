import os
from flask import Flask, render_template, request
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import warnings

app = Flask(__name__)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Load FAISS index
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("news_index", embedding_model, allow_dangerous_deserialization=True)

# QA model pipeline
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", max_length=512)
llm = HuggingFacePipeline(pipeline=qa_pipeline)

# Prompt template
prompt_template = """
Use the following news headlines to answer the question.
If the answer is not clear, say "Sorry, I don't know."

Headlines:
{context}

Question: {question}
Answer:
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt}
)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    question = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = qa_chain.run(question)
    return render_template("index.html", question=question, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)