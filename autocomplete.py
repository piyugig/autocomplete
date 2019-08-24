from redisearch import Client, TextField, NumericField, Query
# Creating a client with a given index name
client = Client('myIndex', 'redis-search')

# Creating the index definition and schema
client.create_index((TextField('title', weight=5.0), TextField('body')))

# Indexing a document
client.add_document('doc1', title = 'RediSearch', body = 'Redisearch impements a search engine on top of redis')

# Simple search
res = client.search("search engine")

# Searching with snippets
#res = client.search("search engine", snippet_sizes = {'body': 50})

# Searching with complext parameters:
#q = Query("search engine").verbatim().no_content().paging(0,5)
#res = client.search(q)


# the result has the total number of results, and a list of documents
print(res.total)
print(res.docs[0].title)
