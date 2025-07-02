# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex: 
    def __init__(self, r, i):
        self.r = r  # Real part
        self.i = i  # Imaginary part

    def __add__(self, c2):
        # Addition: (a + bi) + (c + di) = (a + c) + (b + d)i
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        # Multiplication: (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)
    
    def __str__(self):
        sign = '+' if self.i >= 0 else '-'
        return f"{self.r} {sign} {abs(self.i)}i"
    
# Test
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print("Addition:", c1 + c2)     # Expected: 4 + 6i
print("Multiplication:", c1 * c2)  # Expected: (1×3 - 2×4) + (1×4 + 2×3)i = -5 + 10i
