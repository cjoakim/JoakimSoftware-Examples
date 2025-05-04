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

These examples are both for my personal use, and for use on my
customer projects.  They are intended to be **starter projects**
rather than full-functionality business applications.

---

## Contact Information

```
Chris Joakim
christopher.joakim@outlook.com
Davidson, NC, USA  28036
```

---

## Directory Structure - Top-Level Projects

| Directory           | State         | Description                              |
| ------------------- |-------------- | ---------------------------------------- |
| az                  | Planned       | Azure CLI (az) deployment scripts        |
| data                | Implemented   | Common datasets used in these projects   |
| java_gremlin_export | External      | Export CosmosDB Gremlin API data         |  
| java_jena_graph     | External Repo | Apache Jena RDF in-memory graph          |  
| python_aws_finops   | Partial Impl  | FinOps with AWS CUR data                 |
| python_data         | Implemented   | Data wrangling with Python, duckdb, etc  |
| python_fastapi      | Implemented   | FastAPI Python webservice                |
| python_langchain    | WIP           | AI witg Python, LangChain, Ollama, etc   |
| python_libraries    | WIP           | Python library graph dataset creation    |

---

## Standard Environment Variables

For consistency, these variable names are used throughout the various
language-specific implementaion subprojects.

```
AWS_ACCESS_KEY_ID
AWS_DEFAULT_REGION
AWS_SECRET_ACCESS_KEY
AWS_BILLING_BUCKET
AWS_BILLING_ITEM_PREFIX

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
