def safe_divide(numerator, denominator):
    try:
        # Attempt to convert to float and perform division
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is {result}"  # Return formatted string
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
