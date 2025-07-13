import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

# Load .env file
load_dotenv("C:/Users/SWAPN/OneDrive/Desktop/Data_science/GenAI/.env")
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Setup Hugging Face LLM via LangChain
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",  # or try "conversational" if "text-generation" fails
    huggingfacehub_api_token=api_key,
)

model = ChatHuggingFace(llm=llm)

# Invoke with a simple question
result = model.invoke("What is the capital of India? Reply in one sentence.")

# Output the answer
print("\n🟢 Answer:")
print(result.content.strip())
