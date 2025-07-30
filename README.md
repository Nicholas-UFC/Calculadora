# 🔢 Calculadora Científica em Python

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Uma calculadora de desktop com interface gráfica, desenvolvida em Python usando a biblioteca Tkinter. Este projeto implementa funcionalidades científicas e foi estruturado com base nos princípios da Programação Orientada a Objetos (OOP) para garantir um código limpo, modular e de fácil manutenção.

O foco do projeto foi criar uma aplicação robusta, com uma interface de usuário responsiva e uma arquitetura de software que separa claramente as responsabilidades da lógica de negócio e da apresentação.

---

### ✨ Funcionalidades

* **Operações Básicas:** Adição, subtração, multiplicação e divisão.
* **Funções Científicas:** Raiz quadrada (`√`), potenciação (`xʸ`), logaritmo natural (`ln`) e logaritmo na base 10 (`log`).
* **Constantes Matemáticas:** Acesso rápido aos valores de Pi (`π`) e o número de Euler (`e`).
* **Memória de Resposta:** Botão "Ant" para reutilizar o último resultado em novos cálculos.
* **Interface Responsiva:** O cálculo principal é executado em uma *thread* separada, garantindo que a interface do usuário não congele durante operações complexas.
* **Entrada Flexível:** Suporte para o uso de parênteses `()` para controlar a ordem das operações.

---

### 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface Gráfica:** Tkinter
* **Princípios de Arquitetura:**
    * Programação Orientada a Objetos (OOP)
    * Separação de Responsabilidades (Interface vs. Lógica)
    * Multithreading para responsividade da UI

---

### 🚀 Como Executar a Partir do Código-Fonte

Para executar o projeto, você precisará ter o Python 3 instalado.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)](https://github.com/Nicholas-UFC/Calculadora.git)
    ```
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd seu-repositorio
    ```
3.  **Execute o script principal:**
    ```bash
    python main.py
    ```

---

### 📦 Como Gerar o Executável (`.exe`)

É possível empacotar a aplicação em um único arquivo executável para Windows.

1.  **Instale a biblioteca PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Execute o comando de compilação:**
    Na raiz do projeto, execute o seguinte comando no terminal:
    ```bash
    python -m PyInstaller --onefile --windowed --name="calculadora" main.py
    ```
3.  O executável final, `calculadora.exe`, estará localizado na pasta `dist/`.

---

### 🏗️ Estrutura do Projeto

O código é dividido em três módulos principais para garantir a organização e a manutenibilidade:

* **`main.py`**: Ponto de entrada da aplicação. Responsável apenas por instanciar e iniciar a interface gráfica.
* **`interface.py`**: Contém a classe `Calculadora`, que gerencia toda a construção da janela, widgets e a interação com o usuário.
* **`logica.py`**: Módulo que contém todas as funções matemáticas puras, sem qualquer dependência da interface gráfica.

---

### 📄 Licença

Distribuído sob a licença MIT.
