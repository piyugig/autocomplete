# autocomplete server
docker-compose build
docker-compose up

# polulate cities
python autocomplete.py

# env
for prod copy secret.prod.json to secret.json
for dev/local copy secret.dev.json to secret.json

# architecture & library used
redis-search
https://oss.redislabs.com/redisearch/index.html
benchmarking
https://redislabs.com/blog/search-benchmarking-redisearch-vs-elasticsearch/

flask web framework

#API
GET: http://localhost:3000/query?term=piy

POST: http://localhost:3000/add
{
	"location": "pi"
}

POST: http://localhost:3000/delete
{
	"location": "pi"
}




