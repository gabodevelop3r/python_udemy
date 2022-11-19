class Aritmetica:
    """
        Clase artimetica para realizar las operaciones de sumar, restar , etc

    """


    def __init__(self, operandoA, operadoB):
        self.operandoA = operandoA
        self.operandoB = operadoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(10, 5)
print(f'suma: {aritmetica1.sumar()}')
print(f'restar: {aritmetica1.restar()}')
print(f'multiplicar: {aritmetica1.multiplicar()}')
print(f'division: {aritmetica1.dividir():.2f}')