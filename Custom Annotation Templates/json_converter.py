import json
from collections import defaultdict


def extract_regions(data):
    regions = defaultdict(lambda: defaultdict(list))
    for item in data:
        task_id = item['id']
        audio_name = item.get('file_upload')
        audio_path = item.get('data', {}).get('audio')

        for annotation in item.get('annotations', []):
            for result in annotation.get('result', []):
                region_data = {
                    "task_id": task_id,
                    "audio_name": audio_name,
                    "audio_path": audio_path,
                    "type": result['type'],
                    "start": result['value'].get('start'),
                    "end": result['value'].get('end'),
                    "labels": result['value'].get('labels'),
                    "text": result['value'].get('text'),
                    "choices": result['value'].get('choices'),
                    "from_name": result.get('from_name'),
                    "to_name": result.get('to_name'),
                    "channel": result['value'].get('channel')
                }

                # Collect gender and age separately to avoid overwriting
                if result['type'] == 'choices':
                    if result.get('from_name') == 'gender':
                        region_data['gender'] = result['value'].get('choices')[0]
                    elif result.get('from_name') == 'age':
                        region_data['age'] = result['value'].get('choices')[0]

                # Group by audio_name and region_id
                region_id = result['id']
                regions[audio_name][region_id].append(region_data)

    return regions


# Read the JSON file
with open('export.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

regions = extract_regions(data)

# Save the grouped regions to a new JSON file
with open('regions.json', 'w', encoding='utf-8') as file:
    json.dump(regions, file, ensure_ascii=False, indent=4)

print("Extracted regions saved to regions.json")