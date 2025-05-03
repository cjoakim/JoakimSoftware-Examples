# Python with LangChain

...and ollama, too, for localhost LLM/SLM app development.

## Running SLMs locally

See YouTube video here: https://www.youtube.com/watch?v=e5iaYkSNrhY (Jeremy Morgan)

Manning Book by Jeremy Morgan: https://www.manning.com/books/coding-with-ai

---

## LMStudio

Runs on Mac, Linux, or Windows.

- https://lmstudio.ai 
  - Download and run Llama, DeepSeek, Mistral, Phi on your computer.
  - https://lmstudio.ai/docs/app/api/tools
  - https://lmstudio.ai/docs/cli
  - https://lmstudio.ai/docs/python
  - https://lmstudio.ai/docs/python/embedding


```
http://localhost:1234/v1/models

{
  "data": [
    {
      "id": "meta-llama-3.1-8b-instruct",
      "object": "model",
      "owned_by": "organization_owner"
    },
    {
      "id": "text-embedding-nomic-embed-text-v1.5",
      "object": "model",
      "owned_by": "organization_owner"
    }
  ],
  "object": "list"
}
```

---

### CLI 

See https://lmstudio.ai/docs/cli

#### Installation

```
$ ~/.lmstudio/bin/lms bootstrap

$ cat .bash_profile

# Added by LM Studio CLI (lms)
export PATH="$PATH:/Users/cjoakim/.lmstudio/bin"
# End of LM Studio CLI section


cat .bash_profile | grep lms
# Added by LM Studio CLI (lms)
export PATH="$PATH:/Users/cjoakim/.lmstudio/bin"
```

```
$ lms server status
The server is running on port 1234.

$ lms --help
lms <subcommand>

where <subcommand> can be one of:

- status - Prints the status of LM Studio
- server - Commands for managing the local server
- ls - List all downloaded models
- ps - List all loaded models
- get - Searching and downloading a model from online.
- load - Load a model
- unload - Unload a model
- create - Create a new project with scaffolding
- log - Log operations. Currently only supports streaming logs from LM Studio via `lms log stream`
- import - Import a model file into LM Studio
- flags - Set or get experiment flags
- bootstrap - Bootstrap the CLI
- version - Prints the version of the CLI
```

---

### Embeddings

See https://lmstudio.ai/docs/python/embedding

```
lms get nomic-ai/nomic-embed-text-v1.5
```

```
import lmstudio as lms

model = lms.embedding_model("nomic-embed-text-v1.5")

embedding = model.embed("Hello, world!")
```

---

## ollama

- https://ollama.com
- https://ollama.com/library (see and download models)
- https://ollama.com/library/phi3
- https://github.com/ollama/ollama 
- https://pypi.org/project/ollama/
- https://github.com/ollama/ollama-python
- https://python.langchain.com/docs/integrations/llms/ollama/


Runs on Mac, Linux, or Windows.

ollama is a Terminal/CLI-oriented program.

```
$ ollama list
NAME    ID    SIZE    MODIFIED

```

```
$ ollama run phi3
/bye
```

```
$ ollama run --verbose phi3
/bye
```

```
$ ollama list
NAME           ID              SIZE      MODIFIED
phi3:latest    4f2222927938    2.2 GB    36 seconds ago
```

```
$ ollama help
Large language model runner

Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command
```


#### Run and Serve

In one terminal, run a model:

```
$ ollama run --verbose phi3
```

In another terminal, run the server:

```
$ ollama serve
$ ollama serve --help
```

#### ollama python lib

- https://pypi.org/project/ollama/
- https://github.com/ollama/ollama-python



