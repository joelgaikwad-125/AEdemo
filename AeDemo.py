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
class Find_even_odd:
    def check_even_odd(number):
    """Checks if a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Example usage
if __name__ == "__main__":
    add_obj = Addition()
    sub_obj = Subtraction()
    mul_obj = Multiplication()
    div_obj = Division()

    a, b = 10, 5
    print("Addition:", add_obj.add(a, b))
    print("Subtraction:", sub_obj.subtract(a, b))
    print("Multiplication:", mul_obj.multiply(a, b))
    print("Division:", div_obj.divide(a, b))
