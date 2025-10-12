from toolkit import *

# ==========================
#  MAIN PROGRAM START
# ==========================

if __name__ == "__main__":
    print("=== PYDATA TOOLKIT: STUDENT DATA ANALYSIS ===\n")

    # Step 1: Load dataset
    data = read_csv("data/sample.csv")

    # Step 2: Clean missing data
    data = drop_missing(data, "name")
    data = drop_missing(data, "age")
    data = drop_missing(data, "marks")
    data = drop_missing(data, "city")

    # Step 3: Show data summary
    print("\n--- DATA SUMMARY ---")
    data_summary(data)

    # Step 4: Select specific columns
    selected = select_columns(data, ["name", "marks"])
    print("\n[INFO] Sample of selected columns:")
    for row in selected[:3]:
        print(row)

    # Step 5: Filter rows (students with marks > 85)
    print("\n--- FILTERED DATA (marks > 85) ---")
    high_scorers = filter_rows(data, lambda row: float(row["marks"]) > 85)
    for row in high_scorers:
        print(row)

    # Step 6: Sort by marks (descending)
    sorted_data = sort_by(data, "marks", reverse=True)
    print("\n--- SORTED DATA BY MARKS (DESC) ---")
    for row in sorted_data:
        print(row)

    # Step 7: Compute statistics
    print("\n--- STATISTICS ---")
    mean(data, "marks")
    median(data, "marks")
    mode(data, "marks")
    variance(data, "marks")
    correlation(data, "age", "marks")

    # Step 8: Visualizations
    print("\n--- VISUALIZATIONS ---")
    plot_histogram(data, "marks")
    plot_bar_chart(data, "city")

    print("\n[DONE] Data Analysis Complete.")
