# Python with LangChain

...and ollama, too, for localhost LLM/SLM app development.

---

## LM Studio

- [See lm_studio.md in this directory](docs/lm_studio.md)
- Run LLMs/SLMs locally

---

## ollama

- [See ollama.md in this directory](docs/ollama.md)
- Run LLMs/SLMs locally
- Integrates with LangChain

---

## chromadb

- [See chromadb.md in this directory](docs/chromadb.md)


---

## LangChain libraries for Python Virtual Environment

See the requirements.txt file in this directory, which includes:

```
$ pip list

...
ollama                   0.4.8
langchain                0.3.25
langchain-community      0.3.23
langchain-core           0.3.58
langchain-ollama         0.3.2
langchain-openai         0.3.16
langchain-text-splitters 0.3.8
langsmith                0.3.42
...
```

### LangChain with ollama links

- https://python.langchain.com/docs/integrations/llms/ollama/
- https://medium.com/@abonia/ollama-and-langchain-run-llms-locally-900931914a46
- https://medium.com/towards-agi/how-to-use-ollama-effectively-with-langchain-tutorial-546f5dbffb70
- https://python.langchain.com/docs/integrations/providers/ollama/
- https://dev.to/emmakodes_/how-to-run-llama-31-locally-in-python-using-ollama-langchain-k8k

### Example program

#### References

- https://pypi.org/project/langchain-ollama/
- https://python.langchain.com/docs/integrations/llms/ollama/
- https://python.langchain.com/api_reference/ollama/llms/langchain_ollama.llms.OllamaLLM.html
- Also see "ollama1.py" in this directory.

```
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step.
"""

model = "llama3.1"
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model=model)
chain = prompt | model
chain.invoke({"question": "What is LangChain?"})
```

Chat, see https://python.langchain.com/api_reference/ollama/chat_models/langchain_ollama.chat_models.ChatOllama.html

```
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3-groq-tool-use")
llm.invoke("Sing a ballad of LangChain.")
```

Embeddings, see https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.ollama.OllamaEmbeddings.html

```
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="llama3")
embeddings.embed_query("What is the meaning of life?")
```

---

## LangServe

See https://python.langchain.com/docs/langserve/

> [!WARNING] We recommend using LangGraph Platform rather than LangServe for new projects.

---

## LangGraph

References:
- https://www.langchain.com/langgraph 
- https://langchain-ai.github.io/langgraph/

> LangGraph — used by Replit, Uber, LinkedIn, GitLab and more — is a low-level
> orchestration framework for building controllable agents. While langchain provides 
> integrations and composable components to streamline LLM application development, 
> the LangGraph library enables agent orchestration — offering customizable architectures, 
> long-term memory, and human-in-the-loop to reliably handle complex tasks.

```
pip install -U langgraph
```
