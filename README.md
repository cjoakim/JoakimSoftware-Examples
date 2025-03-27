<p align="center">
  <img src="docs/img/joakimsoftware-logo.png" width="70%">
</p>

This repo contains examples of using primarily Azure PaaS service
databases such as the **Azure Cosmos DB NoSQL API**, 
**Azure Cosmos DB Mongo vCore API**, and **Azure PostgreSQL**
in multiple programming language ecosystems.

Also used are various Azure AI Services such as **Azure OpenAI**, 
**Azure AI Search**, Amazon S3 storage, and LLM orchestrators such as
**LangChain** and **Semantic Kernel**.

The examples are roughly functionally equivalent, as they use a
mainstream programming language (i.e. - C#, Java, Node.js/Typescript, and Python)
along with a web application framework typical of that language ecosystem
(i.e. - Blazor, SpringBoot, Express, and FastAPI, respectively).

These examples are both for my personal use, and for use on my
customer projects.  They are intended to be **starter projects**
rather than full-functionality business applications.

Note: This the subprojects in this repo are being developed
at this time (late March 2025).  They are expected to be completed
by May 2025.

---

## Contact Information

```
Chris Joakim
christopher.joakim@outlook.com
Davidson, NC, USA  28036
```

---

## Directory Structure - Top-Level Projects

```
├── LICENSE
├── README.md
├── az
├── data
├── docs
│   └── img
├── dotnet_blazor
├── java_gremlin_export
├── java_jena_graph
├── java_spring
├── nodejs_ts_express
├── python_data
├── python_fastapi
├── python_jupyter
├── scripts
└── sql
```

---

## Standard Environment Variables

For consistency, these variable names are used throughout the various
language-specific implementaion subprojects.

```
AZURE_COSMOSDB_NOSQL_ACCT
AZURE_COSMOSDB_NOSQL_URI
AZURE_COSMOSDB_NOSQL_KEY
AZURE_COSMOSDB_NOSQL_AUTHTYPE
AZURE_COSMOSDB_NOSQL_DEFAULT_DB
AZURE_COSMOSDB_NOSQL_DEFAULT_CONTAINER
LOG_LEVEL
MONGO_CONN_STR
REDIS_HOST
REDIS_PORT
```

