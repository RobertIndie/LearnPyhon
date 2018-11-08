class Progression:
    def __init__(self,start=0):
        self._currentValue = start;

    def _advance(self):
        self._currentValue+=1

    def __next__(self):
        if self._currentValue is None:
            raise StopIteration()
        else:
            answer = self._currentValue
            self._advance()
            return answer
    
    def __iter__(self):
        return self

    def print_progression(self,n):
        for i in range(n):
            print(str(next(self)))

class ArithmeticProgression(Progression):
    def __init__(self,increment=1,start=0):
        self._increment = increment
        super().__init__(start)

    def _advance(self):
        self._currentValue += self._increment

class GeometricProgression(Progression):
    def __init__(self,base=2,start=2):
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        self._currentValue *= self._base

print("Print base progression:")
Progression().print_progression(100)
print('='*20)

print("Print arithmetic progression:")
ArithmeticProgression(4).print_progression(100)
print('='*20)

print("Print geometric progression:")
GeometricProgression(2,1).print_progression(100)
print('='*20)
