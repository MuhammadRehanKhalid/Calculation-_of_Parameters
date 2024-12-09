from utils.input_handler import get_float_input

def run():
    """
    Main entry point for the Carbohydrate Calculator.
    """
    print("Welcome to the Carbohydrate Parameter Calculator")
    # Prompt for inputs
    od_value = get_float_input("Enter OD value: ")
    solution_concentration = get_float_input("Enter solution concentration (mg/L): ")
    # Perform calculation
    result = calculate_carbohydrate(od_value, solution_concentration)
    # Display result
    print(f"Calculated Carbohydrate: {result:.2f} mg/L")

def calculate_carbohydrate(od, concentration):
    """
    Formula to calculate carbohydrate concentration.
    Adjust this function based on your specific formula.
    """
    return od * concentration * 0.42  # Example formula
