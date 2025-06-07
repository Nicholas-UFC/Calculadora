import math

def calcular_expressao(expressao):
    try:
        # Tenta calcular a expressão passada como string.
        return str(eval(expressao))
    except Exception:
        # Retorna "ERRO" se a expressão for inválida (ex: divisão por zero, sintaxe errada).
        return "ERRO"

def adicionar(a, b):
    # Adiciona dois numeros e retorna o resultado
    return a + b

def subtrair(a,b):
    # Subtrai o segundo numero do primeiro e retorna o resultado
    return a - b

def multiplicar(a,b):
    # Multiplica dois numeros e retorna o resultado
    return a*b

def dividir(a,b):
    # Divide o primeiro numero pelo segundo e retorn o resultado
    if b == 0:
        return "Erro! Não pode dividir um numero por zero"
    return a / b

def raiz_quadrada(a):
    # Calcula a raiz quadrada de um numero e retorn o resultado
    return str(math.sqrt(float(a)))
def potencial(a,b):
    # Calcula um numero "a" elevado a "b" potencia
    return a**b

def valor_de_pi():
    return str(math.pi)

def logaritmo_natural(a):
    try:
        # Tenta converter para numero e calcular o log
        return str(math.log(float(a)))
    except (ValueError, TypeError):
        return "Erro"