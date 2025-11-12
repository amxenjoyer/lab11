
class Account:
    def __init__(self):
        self._balance = 0
        print("Account created.")

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Invalid withdraw amount or insufficient funds.")


class Calculator:
    def __init__(self):
        print("Calculator ready.")

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y


class Fraction:
    def __init__(self, num, den):
        self._numerator = num
        self._denominator = den
        print(f"Base Fraction {num}/{den} created.")

    def get_numerator(self):
        return self._numerator

    def get_denominator(self):
        return self._denominator

    def add(self, other):
        new_num = (self._numerator * other._denominator) + (other._numerator * self._denominator)
        new_den = self._denominator * other._denominator
        return Fraction(new_num, new_den)  # Returns a base Fraction

    def multiply(self, other):
        # A simple multiply for demo
        new_num = self._numerator * other._numerator
        new_den = self._denominator * other._denominator
        return Fraction(new_num, new_den)  # Returns a base Fraction

    def __str__(self):
        return f"Base {self._numerator}/{self._denominator}"



class SecureAccount(Account):
    def __init__(self, password):
        super().__init__()
        self.password = password

    def get_balance(self, password):
        if self.password == password:
            # Use return to give the value back
            return super().get_balance()
        else:
            print("Incorrect password")
            return None  # Good practice to return something

    def deposit(self, amount, password):
        if self.password == password:
            super().deposit(amount)
        else:
            print("Incorrect password")

    def withdraw(self, amount, password):
        if self.password == password:
            super().withdraw(amount)
        else:
            print("Incorrect password")


class MemoryCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.memory = 0

    def add(self, x, y):
        if x == "RESULT":
            x = self.memory

        if y == "RESULT":
            y = self.memory

        self.memory = super().add(x, y)
        return self.memory

    def sub(self, x, y):
        if x == "RESULT":
            x = self.memory

        if y == "RESULT":
            y = self.memory

        self.memory = super().sub(x, y)
        return self.memory


# --- Fractions ---
class ImprovedFraction(Fraction):

    def __init__(self, num, den):
        super().__init__(num, den)

    def add(self, other):
        if type(other) == int:
            other = ImprovedFraction(other, 1)
        return super().add(other)

    def multiply(self, other):
        if type(other) == int:
            other = ImprovedFraction(other, 1)
        return super().multiply(other)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self):
        return f"{self.get_numerator()}/{self.get_denominator()}"