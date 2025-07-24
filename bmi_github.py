# This program calculates the Body Mass Index (BMI) and classifies it.

def calculate_bmi(weight_kg, height_m):
    """
    Calculates the Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: The calculated BMI value.
    """
    if height_m <= 0:
        raise ValueError("Height cannot be zero or negative.")
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi):
    """
    Classifies the BMI value into categories.

    Args:
        bmi (float): The BMI value to classify.

    Returns:
        str: The classification of the BMI.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    elif 30 <= bmi <= 34.9:
        return "Obesity (Class I)"
    elif 35 <= bmi <= 39.9:
        return "Obesity (Class II)"
    else: # bmi > 40
        return "Obesity (Class III) -> Severe or morbid obesity"

def main():
    """
    Main function to get user input, calculate BMI, and display results.
    """
    print("--- BMI Calculator ---")
    while True:
        try:
            weight_str = input("Enter your weight in kilograms (e.g., 70.5): ")
            weight = float(weight_str)
            if weight <= 0:
                print("Weight must be a positive number. Please try again.")
                continue

            height_str = input("Enter your height in meters (e.g., 1.75): ")
            height = float(height_str)
            if height <= 0:
                print("Height must be a positive number. Please try again.")
                continue

            # Calculate BMI
            bmi_value = calculate_bmi(weight, height)
            # Classify BMI
            bmi_classification = classify_bmi(bmi_value)

            print(f"\nYour BMI is: {bmi_value:.2f}") # Format to 2 decimal places
            print(f"Classification: {bmi_classification}")
            break # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter numeric values for weight and height.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
