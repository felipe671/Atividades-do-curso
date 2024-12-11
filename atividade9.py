import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def abrir_imc():
    def calcular_imc():
        try:
            peso = float(entry_peso.get())
            altura = float(entry_altura.get())
            imc = peso / (altura ** 2)
            messagebox.showinfo("Resultado IMC", f"Seu IMC é: {imc:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    janela_imc = tk.Toplevel()
    janela_imc.title("Cálculo IMC")

    label_peso = ttk.Label(janela_imc, text="Peso (kg):")
    label_peso.grid(row=0, column=0, padx=10, pady=5)

    entry_peso = ttk.Entry(janela_imc)
    entry_peso.grid(row=0, column=1, padx=10, pady=5)

    label_altura = ttk.Label(janela_imc, text="Altura (m):")
    label_altura.grid(row=1, column=0, padx=10, pady=5)

    entry_altura = ttk.Entry(janela_imc)
    entry_altura.grid(row=1, column=1, padx=10, pady=5)

    btn_calcular_imc = ttk.Button(janela_imc, text="Calcular IMC", command=calcular_imc)
    btn_calcular_imc.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


def abrir_calculadora():
    def pressionar(botao):
        entrada = entry_calculadora.get()
        entrada += str(botao)
        entry_calculadora.delete(0, tk.END)
        entry_calculadora.insert(0, entrada)

    def calcular():
        try:
            resultado = eval(entry_calculadora.get())
            entry_calculadora.delete(0, tk.END)
            entry_calculadora.insert(0, resultado)
        except:
            entry_calculadora.delete(0, tk.END)
            entry_calculadora.insert(0, "Erro")

    def limpar():
        entry_calculadora.delete(0, tk.END)

    janela_calculadora = tk.Toplevel()
    janela_calculadora.title("Calculadora")

    entry_calculadora = ttk.Entry(janela_calculadora, font=("Arial", 18), justify='right')
    entry_calculadora.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    
    botoes = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
    ]

    for (texto, linha, coluna) in botoes:
        if texto == "=":
            ttk.Button(janela_calculadora, text=texto, width=5, command=calcular).grid(row=linha, column=coluna, padx=5, pady=5)
        else:
            ttk.Button(janela_calculadora, text=texto, width=5, command=lambda t=texto: pressionar(t)).grid(row=linha, column=coluna, padx=5, pady=5)

    btn_limpar = ttk.Button(janela_calculadora, text="C", width=5, command=limpar)
    btn_limpar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


def abrir_regra_3():
    def calcular_regra_3():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            resultado = (b * c) / a
            messagebox.showinfo("Resultado", f"O resultado da regra de 3 é: {resultado:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    janela_regra_3 = tk.Toplevel()
    janela_regra_3.title("Regra de 3")

    label_a = ttk.Label(janela_regra_3, text="A:")
    label_a.grid(row=0, column=0, padx=10, pady=5)

    entry_a = ttk.Entry(janela_regra_3)
    entry_a.grid(row=0, column=1, padx=10, pady=5)

    label_b = ttk.Label(janela_regra_3, text="B:")
    label_b.grid(row=1, column=0, padx=10, pady=5)

    entry_b = ttk.Entry(janela_regra_3)
    entry_b.grid(row=1, column=1, padx=10, pady=5)

    label_c = ttk.Label(janela_regra_3, text="C:")
    label_c.grid(row=2, column=0, padx=10, pady=5)

    entry_c = ttk.Entry(janela_regra_3)
    entry_c.grid(row=2, column=1, padx=10, pady=5)

    btn_calcular = ttk.Button(janela_regra_3, text="Calcular", command=calcular_regra_3)
    btn_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


root = tk.Tk()
root.title("Menu Principal")

btn_imc = ttk.Button(root, text="Cálculo IMC", command=abrir_imc)
btn_imc.grid(row=0, column=0, padx=20, pady=20)

btn_calculadora = ttk.Button(root, text="Calculadora", command=abrir_calculadora)
btn_calculadora.grid(row=1, column=0, padx=20, pady=20)

btn_regra_3 = ttk.Button(root, text="Regra de 3", command=abrir_regra_3)
btn_regra_3.grid(row=2, column=0, padx=20, pady=20)

root.mainloop()