"""
Simple Calculator Module
Demonstrates basic arithmetic operations for Jenkins CI/CD testing
"""

class Calculator:
    """A simple calculator class with basic operations"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def power(self, base, exponent):
        """Calculate base raised to exponent"""
        return base ** exponent
    
    def modulo(self, a, b):
        """Return remainder of a divided by b"""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero!")
        return a % b

def main():
    """Demo function"""
    calc = Calculator()
    print("Calculator Demo")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(f"2 ^ 3 = {calc.power(2, 3)}")

if __name__ == "__main__":
    main()
