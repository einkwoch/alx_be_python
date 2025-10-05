def safe_divide(numerator, denominator):
    try:
        # Try to convert both values to float
        num = float(numerator)
        den = float(denominator)

        # Try the division
        result = num / den
        return f"The result of the division is {result:.2f}"

    except ValueError:
        # Raised when conversion to float fails
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Raised when denominator is zero
        return "Error: Cannot divide by zero."