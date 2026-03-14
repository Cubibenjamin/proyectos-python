import tkinter as tk
import time

class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Velocidad de Tipeo")
        self.root.geometry("600x400")

        self.text_to_type = "El diseño electronico requiere precision y paciencia."
        self.start_time = None

        # Interfaz
        self.label_text = tk.Label(root, text=self.text_to_type, font=("Courier", 14), wraplength=500)
        self.label_text.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 12), width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)
        self.entry.bind("<KeyRelease>", self.check_typing)

        self.result_label = tk.Label(root, text="WPM: 0 | Precisión: 100%", font=("Arial", 12))
        self.result_label.pack(pady=20)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def check_typing(self, event):
        user_input = self.entry.get()
        
        # Cambiar color si hay error
        if self.text_to_type.startswith(user_input):
            self.entry.config(fg="black")
        else:
            self.entry.config(fg="red")

        # Calcular métricas al terminar
        if user_input == self.text_to_type:
            end_time = time.time()
            total_time = (end_time - self.start_time) / 60  # en minutos
            words = len(self.text_to_type.split())
            wpm = round(words / total_time)
            
            self.result_label.config(text=f"¡Completado! WPM: {wpm}")
            self.entry.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()