import statistics

def _get_numeric_values(data, column):
   
    values = []
    for row in data:
        try:
            val = float(row[column])
            if not (row[column] == "" or row[column] is None):
                values.append(val)
        except (ValueError, KeyError, TypeError):
            continue
    return values


def mean(data, column="marks"):
    """
    Compute the mean (average) of a numeric column like 'marks' or 'age'.
    """
    values = _get_numeric_values(data, column)
    if not values:
        print(f"[WARN] No valid numeric values found in '{column}'.")
        return None
    result = statistics.mean(values)
    print(f"[INFO] Mean of '{column}': {result:.2f}")
    return result


def median(data, column="marks"):
    """
    Compute the median (middle value) of a numeric column.
    """
    values = _get_numeric_values(data, column)
    if not values:
        print(f"[WARN] No valid numeric values found in '{column}'.")
        return None
    result = statistics.median(values)
    print(f"[INFO] Median of '{column}': {result:.2f}")
    return result


def mode(data, column="marks"):
    """
    Compute the mode (most frequent value) of a numeric column.
    """
    values = _get_numeric_values(data, column)
    if not values:
        print(f"[WARN] No valid numeric values found in '{column}'.")
        return None
    try:
        result = statistics.mode(values)
        print(f"[INFO] Mode of '{column}': {result:.2f}")
        return result
    except statistics.StatisticsError:
        print(f"[WARN] No unique mode found in '{column}'.")
        return None


def variance(data, column="marks"):
    """
    Compute the variance (spread) of a numeric column.
    """
    values = _get_numeric_values(data, column)
    if len(values) < 2:
        print(f"[WARN] Not enough data to compute variance for '{column}'.")
        return None
    result = statistics.variance(values)
    print(f"[INFO] Variance of '{column}': {result:.2f}")
    return result


def correlation(data, col1="age", col2="marks"):
    """
    Compute the correlation coefficient between two numeric columns
    (e.g., between age and marks).
    """
    x_vals = _get_numeric_values(data, col1)
    y_vals = _get_numeric_values(data, col2)

    if len(x_vals) != len(y_vals) or len(x_vals) < 2:
        print(f"[WARN] Not enough matching data to compute correlation between '{col1}' and '{col2}'.")
        return None

    mean_x = statistics.mean(x_vals)
    mean_y = statistics.mean(y_vals)

    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_vals, y_vals))
    denominator_x = sum((x - mean_x) ** 2 for x in x_vals)
    denominator_y = sum((y - mean_y) ** 2 for y in y_vals)

    try:
        corr = numerator / ((denominator_x * denominator_y) ** 0.5)
        print(f"[INFO] Correlation between '{col1}' and '{col2}': {corr:.2f}")
        return corr
    except ZeroDivisionError:
        print(f"[WARN] Division by zero while computing correlation between '{col1}' and '{col2}'.")
        return None
