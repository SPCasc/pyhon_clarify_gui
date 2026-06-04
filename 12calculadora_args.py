# Def é função. Dentro de uma Class (classe) se torna metódo 

# codepen.io

class Calculadora :
    def somar(self, *args) :
        return sum(args)
        
calc = Calculadora()

print(calc.somar(1, 5))
print(calc.somar(1, 2, 3, 7, 5))