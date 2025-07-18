import tkinter as tk
import logica

class Calculadora(tk.Tk):
    def __init__(self) -> None:
        """Inicializa a janela da calculadora."""
        super().__init__()
        self.title("Calculadora Python")
        self.geometry("500x620") # Define o tamanho da janela

        # Display (Visor)
        self.display = tk.Entry(self, font=('Arial', 24), relief = "solid", justify='right')
        self.display.pack(padx=10, pady=20, fill='x')

        # Frame para os botões
        botoes_frame = tk.Frame(self)
        botoes_frame.pack(expand=True, fill='both')

        # Lista de botões
        botoes = [
            '?', '√', 'xʸ', 'ln', 'log',
            'π', '7', '8', '9', '/',
            'e', '4', '5', '6', '*',
            '?', '1', '2', '3', '-',
            'Ant', 'C', '0', '=', '+'
        ]
        
        # Criação e posicionamento dos botões
        row, col = 0,0
        for texto_botoes in botoes:
            acao = lambda x=texto_botoes: self.ao_clicar(x)
            tk.Button(botoes_frame, text=texto_botoes, font=('Arial', 18), command=acao).grid(row=row, column=col, sticky='nsew',padx=5, pady=5)

            col += 1
            if col > 4:
                col = 0
                row += 1

            # Configura as colunas e linhas apra se expandirem igualmente
        for i in range(5):
            botoes_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            botoes_frame.grid_rowconfigure(i, weight=1)

    def ao_clicar(self, valor):
        texto_atual = self.display.get()

        # Botão '?' não faz nada.
        if valor == '?':
            pass
        
        # Botão 'C' limpa o visor.
        elif valor == 'C':
            self.display.delete(0, tk.END)  
                          
        elif valor == '=':
            try:
                resultado = logica.calcular_expressao(texto_atual)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'ERRO')

        # Botão 'π' insere o valor de pi.
        elif valor == 'π':
            self.display.delete(0, tk.END)
            self.display.insert(0, str(logica.valor_de_pi()))

        # Botão '√' calcula a raiz quadrada do número atual.
        elif valor == '√':
                resultado = logica.raiz_quadrada(texto_atual)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))

        # Botão 'xʸ' calcula a potência de um número.
        elif valor == 'xʸ':
            self.display.insert(tk.END, '**')

        # Botão 'ln' calcula o logaritmo natural do número atual.
        elif valor == 'ln':
            resultado = logica.logaritmo_natural(texto_atual)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(resultado))

        # Botão 'log' calcula o logaritmo natural do número atual.
        elif valor == 'log':
            resultado = logica.logaritmo_10(texto_atual)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(resultado))

        # Botão 'e' insere o valor de Euler.
        elif valor == 'e':
            self.display.delete(0, tk.END)
            self.display.insert(0, str(logica.euler()))

        else:
            self.display.insert(tk.END, valor)