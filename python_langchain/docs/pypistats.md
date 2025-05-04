# PyPi Stats

## Referencs

- https://pypistats.org
- https://pypistats.org/api/
- https://pypistats.org/packages/m26

> PyPI Stats provides a simple JSON API for retrieving aggregate download stats
> and time series for packages. The following are the valid endpoints using host: 
> https://pypistats.org/

Also see  Google BigQuery pypi downloads tables.

```
$ pypistats recent langchain -f json | jq
{
  "data": {
    "last_day": 2195328,
    "last_month": 72132900,
    "last_week": 17271934
  },
  "package": "langchain",
  "type": "recent_downloads"
}
```

## Other Solutions

pipdeptree

curl https://registry.npmjs.org/m26-js | jq

