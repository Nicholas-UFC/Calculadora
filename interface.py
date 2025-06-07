import tkinter as tk
import logica

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Python")
        self.geometry("400x620") # Define o tamanho da janela

        # Display (Visor)
        self.display = tk.Entry(self, font=('Arial', 24), relief = "solid", justify='right') 
        self.display.pack(padx=10, pady=20, fill='x')

        # Frame para os botões
        botoes_frame = tk.Frame(self)
        botoes_frame.pack(expand=True, fill='both')

        # Lista de botões
        botoes = [
                'π', '√', 'xʸ', 'ln',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '3', '2', '1', '-',
                'C', '0', '=', '+'
                ]
        
        # Criação e posicionamento dos botões
        row, col = 0,0
        for texto_botoes in botoes:
            acao = lambda x=texto_botoes: self.ao_clicar(x)
            tk.Button(botoes_frame, text=texto_botoes, font=('Arial', 18), command=acao).grid(row=row, column=col, sticky='nsew',padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

            # Configura as colunas e linhas apra se expandirem igualmente
        for i in range(4):
            botoes_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            botoes_frame.grid_rowconfigure(i, weight=1)

    def ao_clicar(self, valor):
        texto_atual = self.display.get()

        if valor == 'C':
            self.display.delete(0, tk.END)  
                          
        elif valor == '=':
            try:
                resultado = logica.calcular_expressao(texto_atual)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'ERRO')

        elif valor == 'π':
            self.display.delete(0, tk.END)
            self.display.insert(0, logica.valor_de_pi())

        elif valor == '√':
                resultado = logica.raiz_quadrada(texto_atual)
                self.display.delete(0, tk.END)
                self.display.insert(0, resultado)

        elif valor == 'xʸ':
            self.display.insert(tk.END, '**')

        elif valor == 'ln':
            resultado = logica.logaritmo_natural(texto_atual)
            self.display.delete(0, tk.END)
            self.display.insert(0, resultado)

        else:
            self.display.insert(tk.END, valor)