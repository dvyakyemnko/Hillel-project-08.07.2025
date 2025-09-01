class Fraction:
    a: int
    b: int

    def __init__(self, a: int, b: int) -> None:
        if b == 0:
            raise ValueError("Знаменник не може бути нулем")
        self.a = a
        self.b = b

    def __mul__(self, other: "Fraction") -> "Fraction":
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other: "Fraction") -> "Fraction":
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)

    def __sub__(self, other: "Fraction") -> "Fraction":
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b == self.b * other.a

    def __gt__(self, other: "Fraction") -> bool:
        return self.a * other.b > self.b * other.a

    def __lt__(self, other: "Fraction") -> bool:
        return self.a * other.b < self.b * other.a

    def __str__(self) -> str:
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c
assert f_d > f_e
assert f_a != f_b
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2
print('OK')
