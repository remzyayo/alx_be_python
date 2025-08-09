# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to return the sum of two numbers.
        This method does not access class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to return the product of two numbers.
        Accesses the class attribute 'calculation_type' via cls.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
