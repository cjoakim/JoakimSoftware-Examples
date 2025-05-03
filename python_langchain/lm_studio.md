# LMStudio

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

## CLI 

See https://lmstudio.ai/docs/cli

### Installation

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

## Embeddings

See https://lmstudio.ai/docs/python/embedding

```
lms get nomic-ai/nomic-embed-text-v1.5
```

```
import lmstudio as lms

model = lms.embedding_model("nomic-embed-text-v1.5")

embedding = model.embed("Hello, world!")
```
