#https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, 
                                  Query(
    min_length=3, max_length=50, pattern="^fixedquery$",
    title="Query string",
    description="Query string for the items to search in the database that have a good match",
    alias='item-query',
    #deprecated=True,
    #include_in_schema=False
    )] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#http://localhost:8000/items/?q=foo&q=bar
@app.get("/items_list/")
async def read_items(q: Annotated[list[str] | None, Query()] = None): # you can use  ["foo", "bar"] instead of None
    query_items = {"q": q}
    return query_items