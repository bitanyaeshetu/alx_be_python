# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers, referencing a class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

def main():
    # Demonstrating the static method
    sum_result = Calculator.add(5, 3)
    print(f"The sum is: {sum_result}")  # Expected: The sum is: 8

    # Demonstrating the class method
    product_result = Calculator.multiply(4, 2)
    print(f"The product is: {product_result}")  # Expected: The product is: 8

if __name__ == "__main__":
    main()
