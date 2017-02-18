from json import loads, dump

with open('main.json') as i:
  unsorted_pages = loads(i.read())

pages = sorted(unsorted_pages, key = lambda k: int(k['page_number']))

for p in pages:
  unsorted_results = p['results']
  results = sorted(unsorted_results, key = lambda k: int(k['id']))
  for r in results:
    # record = p['query'], p['page_number'], p['num_results'], r['rank'], r['id'], r['title'], r['domain'], r['snippet']
    record = p['query'], p['page_number'], p['num_results'], r['rank'], r['id'], r['domain']
    print(record)
