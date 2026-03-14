import tkinter as tk
from tkinter import messagebox
import time
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Master de Tipeo - Evolución de WPM")
        self.root.geometry("900x600")

        # Lista de frases aleatorias (puedes añadir de electrónica o código)
        self.phrases = [
            "El diseño de circuitos requiere una gran atencion al detalle.",
            "Python es un lenguaje versatil para la automatizacion de procesos.",
            "La arquitectura de software define la estructura de un sistema.",
            "El control PID es fundamental en la ingenieria electronica.",
            "Aprender a programar abre puertas a nuevas oportunidades laborales."
        ]
        
        self.history_wpm = []  # Para el gráfico
        self.start_time = None
        self.current_phrase = ""

        # UI: Frase y Entrada
        self.label_phrase = tk.Label(root, text="", font=("Courier", 14), wraplength=400, fg="#333")
        self.label_phrase.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12), width=50)
        self.entry.pack(pady=5)
        self.entry.bind("<KeyPress>", self.start_timer)
        self.entry.bind("<KeyRelease>", self.check_typing)

        self.result_label = tk.Label(root, text="WPM: 0", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=5)

        # Botón Reiniciar
        self.btn_restart = tk.Button(root, text="Reiniciar / Nueva Frase", command=self.reset_app, bg="#f0f0f0")
        self.btn_restart.pack(pady=5)

        # Configuración del Gráfico (Matplotlib)
        self.setup_chart()
        self.reset_app()

    def setup_chart(self):
        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=80)
        self.ax.set_title("Progreso de Velocidad")
        self.ax.set_xlabel("Sesión")
        self.ax.set_ylabel("WPM")
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(pady=10, fill=tk.BOTH, expand=True)

    def reset_app(self):
        self.current_phrase = random.choice(self.phrases)
        self.label_phrase.config(text=self.current_phrase)
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.config(fg="black")
        self.start_time = None
        self.result_label.config(text="WPM: 0")

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def check_typing(self, event):
        user_input = self.entry.get()
        
        # Feedback visual
        if self.current_phrase.startswith(user_input):
            self.entry.config(fg="black")
        else:
            self.entry.config(fg="red")

        # Finalización
        if user_input == self.current_phrase:
            total_time = (time.time() - self.start_time) / 60
            words = len(self.current_phrase.split())
            wpm = round(words / total_time)
            
            self.history_wpm.append(wpm)
            self.result_label.config(text=f"¡Excelente! WPM: {wpm}")
            self.entry.config(state="disabled")
            self.update_chart()

    def update_chart(self):
        self.ax.clear()
        self.ax.set_title("Progreso de Velocidad")
        self.ax.set_xlabel("Sesión")
        self.ax.set_ylabel("WPM")
        self.ax.plot(range(1, len(self.history_wpm) + 1), self.history_wpm, marker='o', color='b')
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    def on_closing():
        # Esto mata el proceso de raíz para que no quede colgado en VS Code
        root.quit()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    # ------------------------------

    root.mainloop()