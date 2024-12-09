import time
import importlib

def display_menu(options):
    for key, value in options.items():
        print(f"{key}: {value}")

def get_choice(prompt, options):
    try:
        choice = int(input(prompt))
        if choice in options:
            return choice
        else:
            print("Invalid choice. Try again.")
            return get_choice(prompt, options)
    except ValueError:
        print("Please enter a valid number.")
        return get_choice(prompt, options)

# Menu options
organism_menu = {1: "Algae", 2: "Plant"}
algae_parameters = {
    1: "Carbohydrate",
    2: "Protein",
    3: "Lipids",
    4: "Chlorophyll a",
    5: "Chlorophyll b",
    6: "Carotenoids",
}

def handle_parameter(organism, param_name):
    try:
        # Dynamically import the corresponding module
        module = importlib.import_module(f"parameters.{param_name.lower()}")
        # Call the main function of the parameter module
        module.run()
    except ModuleNotFoundError:
        print(f"Module for {param_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    time.sleep(1)
    print("Please select appropriate organism type")
    display_menu(organism_menu)
    species = get_choice("Please select the specific type: ", organism_menu)

    if species == 1:  # Algae
        print("Welcome to Algae Parameters Calculator")
        display_menu(algae_parameters)
        param_choice = get_choice("Please select a parameter: ", algae_parameters)
        param_name = algae_parameters[param_choice]
        handle_parameter("algae", param_name)
    elif species == 2:
        print("Plant module is under development!")

if __name__ == "__main__":
    main()
