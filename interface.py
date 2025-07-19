from typing import Dict, Callable
import tkinter as tk
import threading
import logica

class Calculadora(tk.Tk):
    """Cria a interface gráfica e gerencia as interações da calculadora."""

    def __init__(self) -> None:
        """Inicializa a janela da calculadora, mapeia operações e cria os widgets."""
        super().__init__()
        self.title("Calculadora Python")
        self.geometry("400x550") # Ajustei o tamanho para um layout 5x5 mais compacto

        # Atributo para guardar o último resultado (para o botão 'Ant')
        self.ultimo_resultado: str = ""
        
        # Mapeia os botões às suas funções lógicas para um código mais limpo
        self._mapear_operacoes()
        
        # Cria todos os elementos visuais da calculadora
        self._criar_widgets()

    def _mapear_operacoes(self) -> None:
        """
        Cria dicionários que mapeiam o texto de um botão à sua função correspondente.
        Esta é a principal melhoria para eliminar a cadeia 'if/elif/else'.
        """
        # Mapeia operações que usam o número atual no visor (ex: √, ln)
        self.operacoes_unarias: Dict[str, Callable[[str], str]] = {
            '√': logica.calcular_raiz_quadrada,
            'ln': logica.calcular_ln,
            'log': logica.calcular_log10,
        }
        # Mapeia botões que representam constantes (ex: π, e)
        self.constantes: Dict[str, Callable[[], str]] = {
            'π': logica.obter_pi,
            'e': logica.obter_euler,
        }

    def _criar_widgets(self) -> None:
        """Cria e posiciona todos os widgets da interface."""
        # Configura o visor da calculadora
        self.display = tk.Entry(self, font=('Arial', 24), relief="solid", justify='right')
        self.display.pack(padx=10, pady=20, fill='x', expand=True)

        # Cria um container para os botões
        botoes_frame = tk.Frame(self)
        botoes_frame.pack(expand=True, fill='both', padx=5, pady=5)

        # Define o layout dos botões em uma grade 5x5
        botoes = [
            '√', 'xʸ', 'ln', 'log', 'C',
            'π', '7', '8', '9', '/',
            'e', '4', '5', '6', '*',
            'Ant', '1', '2', '3', '-',
            '(', ')', '0', '=', '+'
        ]
        
        # Cria os botões dinamicamente a partir da lista
        row, col = 0, 0
        for texto_botao in botoes:
            acao = lambda x=texto_botao: self.ao_clicar(x)
            tk.Button(botoes_frame, text=texto_botao, font=('Arial', 18), command=acao, relief='groove').grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Configura as linhas e colunas da grade para se expandirem igualmente
        for i in range(5):
            botoes_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            botoes_frame.grid_rowconfigure(i, weight=1)

    def ao_clicar(self, valor: str) -> None:
        """
        Lida com todos os cliques de botão de forma organizada, usando os dicionários de mapeamento.
        Este método agora é muito mais curto e legível.
        """
        texto_atual = self.display.get()

        if valor == 'C':
            self.display.delete(0, tk.END)
        elif valor == '=':
            self.iniciar_calculo(texto_atual)
        elif valor == 'Ant':
            self.display.insert(tk.END, self.ultimo_resultado)
        elif valor in self.operacoes_unarias:
            # Se o botão é uma operação como '√', busca a função no dicionário e a executa
            funcao = self.operacoes_unarias[valor]
            resultado = funcao(texto_atual)
            self.display.delete(0, tk.END)
            self.display.insert(0, resultado)
        elif valor in self.constantes:
            # Se o botão é uma constante como 'π', busca a função e a executa
            funcao = self.constantes[valor]
            self.display.delete(0, tk.END)
            self.display.insert(0, funcao())
        elif valor == 'xʸ':
            self.display.insert(tk.END, '**')
        else: # Para números, parênteses e operadores básicos (+, -, *, /)
            self.display.insert(tk.END, valor)

    def iniciar_calculo(self, expressao: str) -> None:
        """Dispara o cálculo da expressão em uma thread separada para não travar a UI."""
        # Idealmente, aqui também teríamos uma barra de progresso como no outro projeto.
        # Por enquanto, apenas rodamos em uma thread para garantir a responsividade.
        thread = threading.Thread(target=self._thread_calcular, args=(expressao,))
        thread.start()

    def _thread_calcular(self, expressao: str) -> None:
        """Roda em segundo plano para executar o cálculo pesado com 'eval'."""
        resultado = logica.calcular_expressao(expressao)
        # Agenda a atualização da interface de volta na thread principal
        self.after(0, self._calculo_concluido, resultado)

    def _calculo_concluido(self, resultado: str) -> None:
        """Atualiza a UI com o resultado do cálculo quando a thread termina."""
        self.display.delete(0, tk.END)
        self.display.insert(0, resultado)
        # Se o cálculo foi bem-sucedido, guarda o resultado para o botão 'Ant'
        if resultado != "Erro":
            self.ultimo_resultado = resultado