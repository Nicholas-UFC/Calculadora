import math

def obter_pi() -> str:
    """Retorna o valor da constante Pi como uma string."""
    return str(math.pi)

def obter_euler() -> str:
    """Retorna o valor da constante de Euler (e) como uma string."""
    return str(math.e)

def calcular_raiz_quadrada(numero_str: str) -> str:
    """
    Calcula a raiz quadrada de um número.
    Recebe o número como uma string (vindo do visor) e retorna o resultado como string.
    """
    try:
        return str(math.sqrt(float(numero_str)))
    except (ValueError, TypeError):
        return "Erro"

def calcular_ln(numero_str: str) -> str:
    """
    Calcula o logaritmo natural (base e) de um número.
    """
    try:
        # Converte a string para float e calcula o logaritmo natural.
        return str(math.log(float(numero_str)))
    except (ValueError, TypeError):
        # Captura erros se a entrada não for um número válido ou for <= 0.
        return "Erro"

def calcular_log10(numero_str: str) -> str:
    """
    Calcula o logaritmo na base 10 de um número.
    """
    try:
        # A função 'math.log' aceita um segundo argumento para a base.
        # Aqui, especificamos a base 10.
        return str(math.log(float(numero_str), 10))
    except (ValueError, TypeError):
        # Captura erros se a entrada não for um número válido ou for <= 0.
        return "Erro"

def calcular_expressao(expressao: str) -> str:
    """
    Calcula o resultado de uma expressão matemática completa (ex: "5*2+10").
    Esta é a função principal chamada quando o botão '=' é pressionado.
    """
    # Verificação inicial: se a expressão estiver vazia, retorna "Erro"
    if not expressao:
        return "Erro"
    
    try:
        return str(eval(expressao))
    except Exception:
        return "Erro"