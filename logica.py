import math
from decimal import Decimal

# Função para calcular uma expressão matemática
def calcular_expressao(expressao) -> str:
    try:
        return str(eval(expressao))
    except Exception:
        return "ERRO"

# Função para adicionar dois números
def adicionar(a, b) -> Decimal:
    return a + b

# Função para subtrair dois números
def subtrair(a,b) -> Decimal:
    return a - b

# Função para multiplicar dois números
def multiplicar(a,b) -> Decimal:
    return a * b

# Função para dividir dois números
def dividir(a,b) -> Decimal:
    if b == 0:
        raise ZeroDivisionError("Erro! Não pode dividir um numero por zero")
    return a / b
       
# Função para calcular a raiz quadrada de um número
def raiz_quadrada(a) -> Decimal:
    return Decimal(math.sqrt(Decimal(a)))

# Função para calcular a potência de um número
def potencial(a,b) -> Decimal:
    return Decimal(a) ** Decimal(b) 

# Função para calcular o logaritmo natural de um número
def logaritmo_natural(a) -> Decimal:
    try:
        return Decimal(math.log(Decimal(a)))
    except (ValueError, TypeError):
        return Decimal('NaN')
    
# Função para calcular o logaritmo 10 de um número
def logaritmo_10(a) -> Decimal:
    try:
        return Decimal(math.log(Decimal(a), 10))
    except (ValueError, TypeError):
        return Decimal('NaN')

# Função para retornar o valor de Euler (e)
def euler() -> Decimal:
    return Decimal(math.e)

# Função para retornar o valor de pi
def valor_de_pi() -> Decimal:
    return Decimal(math.pi)