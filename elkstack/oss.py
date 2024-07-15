import requests
from elasticsearch import Elasticsearch


# Initialize Elasticsearch client
es = Elasticsearch([{'host': 'localhost', 'port': 9200,'scheme':'http'}])

def fetch_data_from_api(url):
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code)
        return None

def ingest_data_into_es(index_name, data):
    for doc in data['data']['rows']:
        es.index(index=index_name, body=doc)

# Trending Repos
trending_repos_data = fetch_data_from_api("https://api.ossinsight.io/v1/trends/repos/")
if trending_repos_data:
    ingest_data_into_es("trending_repos", trending_repos_data)

# List of Collections
collections_data = fetch_data_from_api("https://api.ossinsight.io/v1/collections/")
if collections_data:
    ingest_data_into_es("collections_list", collections_data)

# List of Hot Collections
hot_collections_data = fetch_data_from_api("https://api.ossinsight.io/v1/collections/hot/")
if hot_collections_data:
    ingest_data_into_es("hot_collections", hot_collections_data)

# Issue Creators

issue_creators_data = fetch_data_from_api("https://api.ossinsight.io/v1/repos/pingcap/tidb/issue_creators/")
if issue_creators_data:
    ingest_data_into_es("issue_creators", issue_creators_data)

# Countries/Regions of Issue Creators
countries_data = fetch_data_from_api("https://api.ossinsight.io/v1/repos/pingcap/tidb/issue_creators/countries/")
if countries_data:
    ingest_data_into_es("issue_creators_countries", countries_data)

# Organizations of Star Gazers
orgs_data = fetch_data_from_api("https://api.ossinsight.io/v1/repos/pingcap/tidb/issue_creators/organizations/")
if orgs_data:
    ingest_data_into_es("star_gazers_orgs", orgs_data)
