# Manticore Python client

 WARNING: this is a development version of the client. The latest release's readme is https://github.com/manticoresoftware/manticoresearch-python-asyncio/tree/1.0.0

## Requirements.

Minimum Manticore Search version is >= 6.2.0 with HTTP protocol enabled.

| **manticoresearch-python-asyncio*  | **Manticore Search**                | **Python**     | **Compatibility**       |
| -----------------------------------| ----------------------------------- | -------------- | ------------------------|
| `manticoresearch-devel`            | `dev` (latest development version)  | 3.4 or newer   | ✅ Fully Compatible     |
| 1.0.0 or newer                     | 9.2.14 or newer                     | 3.4 or newer   | ✅ Fully Compatible     |
| 1.0.0 or newer                     | 6.2.0 to 9.2.14                     | 3.4 or newer   | ⚠️ Partially Compatible |
| 1.0.0 or newer                     | 2.5.1 to 6.2.0                      | 3.4 or newer   | ❗ Incompatible         |

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m manticoresearch
```

and open your browser to here:

```
http://localhost:/ui/
```

Your OpenAPI definition lives here:

```
http://localhost:/openapi.json
```

To launch the integration tests, use pytest:
```
sudo pip install -r test-requirements.txt
pytest
```

## Prevent file overriding

After first generation, add edited files to _.openapi-generator-ignore_ to prevent generator from overwriting them. Typically:
```
server/controllers/*
test/*
*.txt
```

## Getting Started

Please follow the installation procedure and then run the following example:

```python
import manticoresearch
from manticoresearch.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
async with manticoresearch.ApiClient(configuration) as api_client:
    # Create instances of API classes
    indexApi = manticoresearch.IndexApi(api_client)
    searchApi = manticoresearch.SearchApi(api_client)
    utilsApi = manticoresearch.UtilsApi(api_client)

    try:
        # Perform insert and search operations    
        newDoc = {"title" : "Crossbody Bag with Tassel", "price": 19.85}
        insert_request = InsertDocumentRequest(index="products", doc=newDoc)
        await indexApi.insert(insert_request)
        
        # Check out the structure of the autocreated 'products' table
        sql_response = await utilsApi.sql('DESC products');
        print("The response of UtilsApi->sql:\n")
        pprint(sql_response) 

        newDoc = {"title" : "Pet Hair Remover Glove", "price": 7.99}
        insert_request = InsertDocumentRequest(index="products", doc=newDoc)
        await indexApi.insert(insert_request)
        
        query_highlight = Highlight()
        query_highlight.fields = {"title":{}}
        search_query = SearchQuery(query_string="@title bag")
        search_request = SearchRequest(index="products", query=search_query, highlight=query_highlight)
        search_response = await searchApi.search(search_request)    
        print("The response of SearchApi->search:\n")
        pprint(search_response)

        # Alternatively, you can pass all request arguments as a complex JSON object        
        await indexApi.insert({"index": "products", "doc" : {"title" : "Crossbody Bag with Tassel", "price" : 19.85}})
        await indexApi.insert({"index": "products", "doc" : {"title" : "Pet Hair Remover Glove", "price" : 7.99}})
        search_response = await searchApi.search({"index": "products", "query": {"query_string": "@title bag"}, "highlight":{"fields":{"title":{}}}})
        print("The response of SearchApi->search:\n")
        pprint(search_response)
    except ApiException as e:
        print("Exception when calling Api method: %s\n" % e)
```
