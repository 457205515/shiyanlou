import requests, json
# from json import loads
from elasticsearch import Elasticsearch


HOST = '66.3.125.43'
port = '9200'
api_infor = '_cluster/stats?pretty'
url = 'http://' + HOST + ':' + port + '/' + api_infor
cluster_infor = requests.get(url)   #  get到的是response

# 将response对象转换为json
info_json = cluster_infor.json()

# get方法查询集群状态
es_healthy = json.loads(cluster_infor.text).get("status")
print(es_healthy)
