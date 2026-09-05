from langchain_ollama import ChatOllama
llm = ChatOllama(
    model="qwen3:8b",
    temperature=0.7,
)
response=llm.invoke(
    "give me 3 content idea for fictional ai fashion creator"
)
print(response.content)