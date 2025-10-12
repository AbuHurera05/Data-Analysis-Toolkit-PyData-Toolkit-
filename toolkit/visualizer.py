import matplotlib.pyplot as plt
from collections import Counter

def _get_numeric_values(data, column):

    values = []
    for row in data:
        try:
            val = float(row[column])
            if not (val is None or row[column].strip() == ""):
                values.append(val)
        except (ValueError, KeyError, TypeError):
            continue
    return values


def plot_histogram(data, column="marks"):

    values = _get_numeric_values(data, column)

    if not values:
        print(f"[WARN] No valid numeric values found in '{column}' for histogram.")
        return

    plt.figure(figsize=(7, 4))
    plt.hist(values, bins=5, color='cornflowerblue', edgecolor='black')
    plt.title(f"📊 Histogram of {column.capitalize()}")
    plt.xlabel(column.capitalize())
    plt.ylabel("Frequency")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
    print(f"[INFO] Histogram displayed for column '{column}'.")


def plot_bar_chart(data, column="city"):

    try:
        # Filter out empty or missing values
        values = [row[column].strip() for row in data if row.get(column) and row[column].strip() != ""]
        if not values:
            print(f"[WARN] No valid data found in '{column}' for bar chart.")
            return

        counter = Counter(values)
        labels, counts = list(counter.keys()), list(counter.values())

        plt.figure(figsize=(7, 4))
        plt.bar(labels, counts, color='lightgreen', edgecolor='black')
        plt.title(f"🏙️ Bar Chart of {column.capitalize()}")
        plt.xlabel(column.capitalize())
        plt.ylabel("Count")
        plt.xticks(rotation=20, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()
        print(f"[INFO] Bar chart displayed for column '{column}'.")

    except KeyError:
        print(f"[ERROR] Column '{column}' not found in dataset.")
    except Exception as e:
        print(f"[ERROR] Failed to plot bar chart: {e}")
