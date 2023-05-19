#!/usr/bin/python3
import os, time, warnings, json, jsonpath, requests, traceback

warnings.filterwarnings('ignore')

env = 'fat'
keyword = '\"业务操作日志接收信息\"'
hour = 12  # 几小时
service = 'p*'

txt_path = 't01_1.txt'
if os.path.exists(txt_path):
    os.remove(txt_path)

if env == 'fat':
    host = 'http://'
    headers = {
        'content-type': 'application/x-ndjson',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'kbn-version': '6.8.23',
        'Authorization': 'Basic xxx'
    }

url = '/elasticsearch/_msearch?rest_total_hits_as_int=true&ignore_throttled=true'

nowTime = int(time.time() * 1000)
startTime = nowTime - 3600000 * hour
endTime = nowTime

args1 = {"index": service, "ignore_unavailable": True, "preference": nowTime}
args2 = {"version": True, "size": 500, "sort": [{"@timestamp": {"order": "desc", "unmapped_type": "boolean"}}],
         "_source": {"excludes": []}, "aggs": {"2": {
        "date_histogram": {"field": "@timestamp", "interval": "1m", "time_zone": "Asia/Shanghai",
                           "min_doc_count": 1}}}, "stored_fields": ["*"], "script_fields": {},
         "docvalue_fields": [{"field": "@timestamp", "format": "date_time"}], "query": {"bool": {
        "must": [{"query_string": {"query": keyword, "analyze_wildcard": True, "default_field": "*"}},
                 {"range": {"@timestamp": {"gte": startTime, "lte": endTime, "format": "epoch_millis"}}}],
        "filter": [],
        "should": [], "must_not": []}},
         "highlight": {"pre_tags": ["@kibana-highlighted-field@"], "post_tags": ["@/kibana-highlighted-field@"],
                       "fields": {"*": {}}, "fragment_size": 2147483647}, "timeout": "30000ms"}

data = json.dumps(args1) + '\n' + json.dumps(args2) + '\n'
try:
    resp = requests.post(host + url, data=data.encode('utf8'), headers=headers, verify=False)
    total = jsonpath.jsonpath(resp.json(), '$..responses..hits..total')[0]
    if int(total) != 0:
        result = []
        messages = jsonpath.jsonpath(resp.json(), '$..responses..hits..hits.._source..message')
        for item in messages:
            # print(item)
            orderNo = item[item.find('<ceb:orderNo>') + 13: item.find('<ceb:orderNo>') + 23]
            print(orderNo)
            # 获取字段
            with open(txt_path, mode='a+', encoding='utf8') as f:
                f.write(f'{orderNo}\n')
except Exception as e:
    traceback.print_exc()
