def select_columns(data, columns):
  
    if not data:
        print("[WARN] No data to select columns from.")
        return []

    selected_data = []
    for row in data:
        selected_row = {col: row.get(col, "") for col in columns}
        selected_data.append(selected_row)

    print(f"[INFO] Selected columns: {columns}")
    print(f"[INFO] Resulting dataset size: {len(selected_data)} rows")
    return selected_data


def filter_rows(data, condition_func):

    if not data:
        print("[WARN] No data to filter.")
        return []

    filtered_data = []
    for row in data:
        try:
            if condition_func(row):
                filtered_data.append(row)
        except Exception:
            continue

    print(f"[INFO] Filtered dataset size: {len(filtered_data)} rows")
    return filtered_data


def sort_by(data, column="marks", reverse=False):

    if not data:
        print("[WARN] No data to sort.")
        return []

    try:
        sorted_data = sorted(
            data,
            key=lambda row: (
                float(row[column])
                if str(row[column]).replace('.', '', 1).isdigit()
                else str(row[column]).lower()
            ),
            reverse=reverse
        )
        order = "descending" if reverse else "ascending"
        print(f"[INFO] Data sorted by '{column}' in {order} order.")
        return sorted_data

    except KeyError:
        print(f"[ERROR] Column '{column}' not found in dataset.")
        return data
    except Exception as e:
        print(f"[ERROR] Sorting failed: {e}")
        return data
