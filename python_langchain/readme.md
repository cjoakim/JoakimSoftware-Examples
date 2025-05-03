# Python with LangChain

...and ollama, too, for localhost LLM/SLM app development.

---

## LM Studio

- [See lm_studio.md in this directory](lm_studio.md)
- Run LLMs/SLMs locally

---

## ollama

- [See ollama.md in this directory](ollama.md)
- Run LLMs/SLMs locally
- Integrates with LangChain

---

## LangChain libraries for Python Virtual Environment

See the requirements.txt file in this directory, which includes:

```
$ pip list | grep lang

langchain                0.3.25
langchain-community      0.3.23
langchain-core           0.3.58
langchain-ollama         0.3.2
langchain-openai         0.3.16
langchain-text-splitters 0.3.8
langsmith                0.3.42
```

### LangChain with ollama links

- https://python.langchain.com/docs/integrations/llms/ollama/
- https://medium.com/@abonia/ollama-and-langchain-run-llms-locally-900931914a46
- https://medium.com/towards-agi/how-to-use-ollama-effectively-with-langchain-tutorial-546f5dbffb70
- https://python.langchain.com/docs/integrations/providers/ollama/
- https://dev.to/emmakodes_/how-to-run-llama-31-locally-in-python-using-ollama-langchain-k8k

### Example program

See https://python.langchain.com/docs/integrations/llms/ollama/

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
