class Addition:
    def add(self, a, b):
        return a + b

class Subtraction:
    def subtract(self, a, b):
        return a - b

class Multiplication:
    def multiply(self, a, b):
        return a * b

class Division:
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

class FindEvenOdd:
    def check_even_odd(self, number):
        """Checks if a number is even or odd."""
        if number % 2 == 0:
            return f"{number} is Even"
        else:
            return f"{number} is Odd"

class CalculatePercentage:
    def calculate_percentage(self, obtained_marks, total_marks):
        """Calculates the percentage based on obtained and total marks."""
        if total_marks == 0:
            return "Total marks cannot be zero."
        percentage = (obtained_marks / total_marks) * 100
        return f"Percentage: {percentage:.2f}%"

# Example usage
if __name__ == "__main__":
    add_obj = Addition()
    sub_obj = Subtraction()
    mul_obj = Multiplication()
    div_obj = Division()
    even_odd_obj = FindEvenOdd()
    percentage_obj = CalculatePercentage()

    a, b = 10, 5
    print("Addition:", add_obj.add(a, b))
    print("Subtraction:", sub_obj.subtract(a, b))
    print("Multiplication:", mul_obj.multiply(a, b))
    print("Division:", div_obj.divide(a, b))
    print(even_odd_obj.check_even_odd(a))
    print(percentage_obj.calculate_percentage(85, 100))
