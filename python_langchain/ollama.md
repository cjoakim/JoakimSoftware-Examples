# ollama

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

---

## Run and Serve

In one terminal, run a model:

```
$ ollama run --verbose phi3
```

In another terminal, run the server:

```
$ ollama serve
$ ollama serve --help
```

---

## ollama python lib

- https://pypi.org/project/ollama/
- https://github.com/ollama/ollama-python



