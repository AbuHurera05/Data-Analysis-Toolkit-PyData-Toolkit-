# toolkit/cleaner.py

import statistics

def drop_missing(data, column, value=None):
    """
    FR1: Data Cleaning (Enhanced)
    ----------------------------------
    Description:
        Handles missing or invalid data entries.
        - For numeric columns ('age', 'marks'): Replace missing with 0, then fill with column mean.
        - For 'city': Replace missing with 'Karachi'.
        - For 'name': Remove the entire row if missing.

    Input:
        data (list[dict]): Dataset loaded from CSV.
        column (str): Column name to check for missing values.
        value (optional): Custom replacement value.

    Output:
        list[dict]: Cleaned dataset.
    """

    if not data:
        print("[WARN] No data provided for cleaning.")
        return []

    # Step 1: Replace missing values with initial defaults
    cleaned_data = []
    replaced_count = 0
    removed_count = 0

    for row in data:
        cell = str(row.get(column, "")).strip()

        # Check for missing/invalid
        if cell == "" or cell.lower() in ["na", "null", "none", "nan"]:
            # Handle based on column type
            if column.lower() in ["marks", "age"]:
                row[column] = "0"
                replaced_count += 1
                cleaned_data.append(row)

            elif column.lower() == "city":
                row[column] = "Karachi"
                replaced_count += 1
                cleaned_data.append(row)

            elif column.lower() == "name":
                # Drop entire row if name missing
                removed_count += 1
                continue

            else:
                # For any other unknown column
                row[column] = "N/A"
                replaced_count += 1
                cleaned_data.append(row)
        else:
            cleaned_data.append(row)

    # Step 2: Replace numeric zeros with mean (for numeric columns only)
    if column.lower() in ["marks", "age"]:
        numeric_values = []
        for row in cleaned_data:
            try:
                val = float(row[column])
                if val != 0:
                    numeric_values.append(val)
            except ValueError:
                continue

        if numeric_values:
            mean_value = round(statistics.mean(numeric_values), 2)
            for row in cleaned_data:
                if float(row[column]) == 0:
                    row[column] = str(mean_value)
            print(f"[INFO] Replaced '0' with mean ({mean_value}) in '{column}' column.")
        else:
            print(f"[WARN] No valid numeric values found to compute mean for '{column}'.")

    print(f"[INFO] Cleaned '{column}' column:")
    print(f"       → Missing/invalid values replaced: {replaced_count}")
    print(f"       → Rows removed (name missing): {removed_count}")
    print(f"       → Total rows after cleaning: {len(cleaned_data)}")

    return cleaned_data
