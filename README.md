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

Some of these subprojects are Implemented, others are Pending.

```
    Subproject                   State
    -------------------          ----------
├── LICENSE
├── README.md
├── aws                          Pending
├── az                           Pending
├── data                         Implemented
├── docs                         Pending
├── dotnet_blazor                Pending
├── java_gremlin_export          Implemented, external repo
├── java_jena_graph              Implemented, external repo
├── java_spring                  Pending
├── nodejs_ts_express            Pending, planned impl for April 2025
├── python_aws_finops            In progress
├── python_data                  Implemented
├── python_fastapi               Implemented
├── python_jupyter               Pending
├── sql
└── ts_aws                       In progress
```

| Directory          | State        | Description                              |
| ------------------ |---- -------- | ---------------------------------------- |
| az                 | Planned      | Azure CLI (az) deployment scripts        |
| data               | Implemented  | Common datasets used in these projects   |
| python_aws_finops  | Partial Impl | FinOps with AWS CUR data                 |

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
