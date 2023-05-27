import math
class MyFractal:
    def __init__(self, numerator, denumerator):
        self.numerator=numerator
        self.denumerator=denumerator
    def __str__(self):
        return f"{self.numerator}/{self.denumerator}"
    
    def __add__(self,other):
        if isinstance(other,MyFractal):
            common_den=self.denumerator * other.denumerator
            second_mum=other.numerator * self.denumerator
            first_num=self.numerator * other.denumerator
            return MyFractal(first_num + second_mum,common_den)
        elif isinstance(other,int):
            second=MyFractal(other,1) # 3/1
            common_den=self.denumerator * second.denumerator
            second_mum=second.numerator * self.denumerator
            first_num=self.numerator * second.denumerator
            return MyFractal(first_num - second_mum,common_den)
    def simplity(self):
            common_den=math.gcd(self.numerator,self.denumerator)
            self.numerator //=common_den
            self.denumerator //=common_den
    def __mul__(self,other):
        if isinstance(other,MyFractal):
            result=MyFractal(self.numerator * other.numerator,self.denumerator * other.denumerator)
            result.simplity()
            return result
        elif isinstance(other,int):
            result=MyFractal(self.numerator * other,self.denumerator)
            result.simplity()

    def __truediv__(self,other):
        if isinstance(other,MyFractal):
            other_inverse = MyFractal(other.denumerator, other.numerator)

            result = self * other_inverse

            result.simplity()
            return result
        elif isinstance(other,int):
            other_inverse = MyFractal(1, other)

            result = self * other_inverse

            result.simplity()
            return result