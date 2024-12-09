def get_float_input(prompt):
    """
    Prompt the user for a float input, with error handling.
    """
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_float_input(prompt)
