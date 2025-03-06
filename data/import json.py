import json

with open('/Users/junhyungpark/Bokdolboksun/data/dataset.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        print(data['prompt'], "→", data["completion"])
