import json
import csv

def extract_data(region_data):
    rows = []
    for audio_name, segments in region_data.items():
        for segment_id, annotations in segments.items():
            # Initialize values for each segment
            start = end = gender = age = text = ""
            for annotation in annotations:
                if annotation['type'] == 'choices':
                    if 'gender' in annotation:
                        gender = annotation['gender']
                    elif 'age' in annotation:
                        age = annotation['age']
                elif annotation['type'] == 'textarea':
                    text = " ".join(annotation['text']) if annotation['text'] else ""
                elif annotation['type'] == 'labels':
                    start = annotation['start']
                    end = annotation['end']
            rows.append([audio_name, segment_id, start, end, text, gender, age])
    return rows

def convert_json_to_csv(json_path, csv_path):
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    rows = extract_data(data)

    # Write to CSV
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['نام فایل صوتی', 'شناسه بخش', 'شروع', 'پایان', 'متن', 'جنسیت', 'سن'])
        writer.writerows(rows)

# Example usage:
convert_json_to_csv('regions.json', 'output.csv')