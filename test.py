import langchain
print(langchain.__version__)
print("Hello from test.py!")



# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task = "text-generation",
# )

# model = ChatHuggingFace(llm=llm)

# result = model.invoke('what is the capital of India?')

# print(result.content)
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv("C:/Users/SWAPN/OneDrive/Desktop/Data_science/GenAI/.env")

client = InferenceClient(
    provider="featherless-ai",
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")  # or "HF_TOKEN"
)

completion = client.chat.completions.create(
    model="HuggingFaceH4/zephyr-7b-beta",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
)


# DEBUG: print raw completion
print("Raw completion response:", completion)

# Safely extract result
if completion and completion.choices:
    print(completion.choices[0].message.content)
else:
    print("❌ No response or choices returned. Check token, model name, or provider.")

