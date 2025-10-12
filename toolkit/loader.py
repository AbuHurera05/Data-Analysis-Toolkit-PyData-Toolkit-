import csv

def read_csv(filepath):
 
    data = []  # List to store rows as dictionaries
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(dict(row))  # Convert OrderedDict to regular dict
        print(f"[INFO] Successfully loaded {len(data)} rows from '{filepath}'")
        return data

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return []

    except Exception as e:
        print(f"[ERROR] Failed to load file: {e}")
        return []
