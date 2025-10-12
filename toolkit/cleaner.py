# toolkit/cleaner.py

def drop_missing(data, column, value=None):

    if not data:
        print("[WARN] No data provided for cleaning.")
        return []

    cleaned_data = []
    replaced_count = 0
    removed_count = 0

    for row in data:
        cell = str(row.get(column, "")).strip()

        # Detect missing / invalid values
        if cell == "" or cell.lower() in ["na", "null", "none", "nan"]:
            # Assign default replacement if user didn't specify one
            if value is None:
                if column.lower() in ["marks", "age"]:
                    row[column] = "0"
                elif column.lower() in ["name", "city"]:
                    row[column] = "Unknown"
                else:
                    row[column] = "N/A"
            else:
                row[column] = str(value)

            replaced_count += 1
            cleaned_data.append(row)
        else:
            cleaned_data.append(row)

    print(f"[INFO] Cleaned '{column}' column:")
    print(f"       → Missing/invalid values replaced: {replaced_count}")
    print(f"       → Total rows after cleaning: {len(cleaned_data)}")

    return cleaned_data
