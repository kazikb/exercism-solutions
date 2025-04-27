def largest_product(series, size):
    """Function to find largest series product in a sequence."""

    if len(series) < size:
        raise ValueError("span must be smaller than string length")

    if size < 0:
        raise ValueError("span must not be negative")

    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    result = 0

    for i in range(len(series)):
        end = i + size
        if end > len(series):
            break

        sequence = series[i:end]
        if "0" in sequence:
            continue

        product = 1
        for n in sequence:
            product *= int(n)
        result = max(result, product)

    return result
