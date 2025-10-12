def data_summary(data):
    if not data:
        print("[WARN] No data available for summary.")
        return

    # Total number of rows
    total_rows = len(data)
    columns = list(data[0].keys())

    print("\n=== DATA SUMMARY REPORT ===")
    print(f"Total Rows: {total_rows}\n")

    for col in columns:
        non_empty = sum(1 for row in data if row[col].strip() != "")
        empty = total_rows - non_empty
        completeness = (non_empty / total_rows) * 100

        print(f"Column: {col}")
        print(f"  Non-empty values : {non_empty}")
        print(f"  Empty values     : {empty}")
        print(f"  Completeness     : {completeness:.2f}%")
        print("-" * 40)

    print("[INFO] Summary report generated successfully.")
