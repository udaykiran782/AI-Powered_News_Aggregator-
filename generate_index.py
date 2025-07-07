import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


df = pd.read_json("data/News_Category_Dataset_v3.json", lines=True)
df = df[['headline', 'category']].dropna().drop_duplicates().head(1000)

docs = [
    Document(page_content=f"{row['headline']} [{row['category']}]", metadata={"category": row["category"]})
    for _, row in df.iterrows()
]

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embedding_model)
vectorstore.save_local("news_index")

print("✅ FAISS index created and saved to 'news_index'")