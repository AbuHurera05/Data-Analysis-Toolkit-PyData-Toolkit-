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

    while True:
        print("\n==============================")
        print("        MAIN MENU")
        print("==============================")
        print("1. Data Summary")
        print("2. Select Columns")
        print("3. Filter High Scorers (marks > 85)")
        print("4. Sort by Marks (Descending)")
        print("5. Compute Statistics")
        print("6. Visualizations")
        print("0. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- DATA SUMMARY ---")
            data_summary(data)

        elif choice == "2":
            cols = input("Enter column names separated by comma (e.g. name,marks): ").split(",")
            selected = select_columns(data, [c.strip() for c in cols])
            print("\n[INFO] Sample of selected columns:")
            for row in selected[:5]:
                print(row)

        elif choice == "3":
            print("\n--- FILTERED DATA (marks > 85) ---")
            high_scorers = filter_rows(data, lambda row: float(row["marks"]) > 85)
            for row in high_scorers:
                print(row)

        elif choice == "4":
            sorted_data = sort_by(data, "marks", reverse=True)
            print("\n--- SORTED DATA BY MARKS (DESC) ---")
            for row in sorted_data:
                print(row)

        elif choice == "5":
            print("\n--- STATISTICS ---")
            mean(data, "marks")
            median(data, "marks")
            mode(data, "marks")
            variance(data, "marks")
            correlation(data, "age", "marks")

        elif choice == "6":
            print("\n--- VISUALIZATIONS ---")
            plot_histogram(data, "marks")
            plot_bar_chart(data, "city")

        elif choice == "0":
            print("\n[DONE] Exiting program. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice! Please try again.")
