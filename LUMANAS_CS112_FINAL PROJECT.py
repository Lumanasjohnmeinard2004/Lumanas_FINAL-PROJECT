class HealthAssistant:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.weight = 0.0
        self.height = 0.0
        self.target_weight = 0.0
        self.activity_level = ""
        self.calorie_intakes = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderate": 1.55,
            "heavy": 1.725
        }
        self.bmi = 0.0
        self.category = ""
        self.advice = ""
        self.suggested_calories = 0.0
        self.weight_difference = 0.0

    def get_user_input(self):
        self.name = input("Enter your Name: ")

        while any(char.isdigit() for char in self.name):
            print("Invalid input. Please enter a name without numbers. \n")
            self.name = input("Enter your Name: ")

        self.age = int(input("Enter your age: "))
        self.weight = self.get_valid_input("weight")
        self.height = self.get_valid_input("height")
        self.target_weight = self.get_valid_input("target weight")

    def get_valid_input(self, prompt, unit):
        while True:
            user_input = input(f"Enter your {prompt} {unit}: ")

            # Validating numeric input greater than 0
            if not user_input.replace(".", "", 1).isdigit() or float(user_input) <= 0:
                print(f"Invalid input. Please enter a valid number higher than 0 for {prompt}.\n")
            else:
                return float(user_input)

    def get_user_input(self):
        self.name = input("Enter your Name: ")

        while any(char.isdigit() for char in self.name):
            print("Invalid input. Please enter a name without numbers. \n")
            self.name = input("Enter your Name: ")

        self.age = int(input("Enter your age: "))
        self.weight = self.get_valid_input("weight", "in kilograms")
        self.height = self.get_valid_input("height", "in meters")
        self.target_weight = self.get_valid_input("target weight", "in kilograms")

    def get_activity_level(self):
        while True:
            print("\n-----------------------\nSedentary = low amount of physical activity\n"
                  "Light = low-intensity activity\n"
                  "Moderate = more substantial level of physical exertion\n"
                  "Heavy = involves high levels of physical effort\n-----------------------\n")

            self.activity_level = input("Enter your daily activity level (sedentary/light/moderate/heavy): ").lower()

            if self.activity_level in ["sedentary", "light", "moderate", "heavy"]:
                break
            else:
                print("Invalid input. Please enter one of the specified activity levels.")

    def calculate_bmi(self):
        self.bmi = self.weight / (self.height ** 2)

    def determine_category_and_advice(self):
        if self.bmi < 18.5:
            self.category = "Underweight"
            self.advice = "It's important to ensure you're getting enough nutrients. Consider consulting with a nutritionist."
        elif 18.5 <= self.bmi < 24.9:
            self.category = "Normal Weight"
            self.advice = "Congratulations! You're in a healthy weight range. Keep up the good work with a balanced diet and regular exercise."
        elif 25.0 <= self.bmi < 29.9:
            self.category = "Overweight"
            self.advice = "Consider incorporating more physical activity and adopting a healthier diet to reduce the risk of associated health issues."
        elif 30.0 <= self.bmi < 39.9:
            self.category = "Obese"
            self.advice = "It's recommended to consult with a healthcare professional to create a personalized plan for weight management."
        else:
            self.category = "Extremely Obese"
            self.advice = "Immediate consultation with a healthcare professional is strongly advised. Obesity in this range poses serious health risks."

    def calculate_suggested_calories(self):
        if self.activity_level in self.calorie_intakes:
            self.suggested_calories = self.weight * 24 * self.calorie_intakes[self.activity_level]
        else:
            self.suggested_calories = 0

    def calculate_weight_difference(self):
        self.weight_difference = self.target_weight - self.weight

    def display_results(self):
        print(f"\nHello, {self.name}!")
        print(f"\nAt the age of {self.age}, your BMI is: {self.bmi:.2f}")
        print(f"You are categorized as: {self.category}")
        print(f"Health advice: {self.advice}")
        print(f"\nTo reach your target weight of {self.target_weight} kg, you need to gain/lose {abs(self.weight_difference):.2f} kg.")
        print(f"Suggested daily calorie intake is approximately {self.suggested_calories:.2f} calories based on a {self.activity_level} activity level.")


def main():
    # Welcome message
    print("\nWelcome to the Health and Fitness Assistant!\nA BMI checker, Activity planner, and Body Fat Calculator all in one go where we help you with your health needs!\n")

    # Create an instance of HealthAssistant
    assistant = HealthAssistant()

    # Get user input
    assistant.get_user_input()

    # Get activity level
    assistant.get_activity_level()

    # Calculate BMI and related values
    assistant.calculate_bmi()
    assistant.determine_category_and_advice()
    assistant.calculate_suggested_calories()
    assistant.calculate_weight_difference()

    # Display the results
    assistant.display_results()

if __name__ == "__main__":
    main()
