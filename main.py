import tkinter as tk
from datetime import datetime, timedelta

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Таймер")
        
        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")
        
        self.label = tk.Label(self.master, textvariable=self.time_var, font=("Helvetica", 48))
        self.label.pack(padx=20, pady=20)
        
        self.start_button = tk.Button(self.master, text="Старт", command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.master, text="Стоп", command=self.stop_timer)
        self.stop_button.pack(pady=10)
        
        self.reset_button = tk.Button(self.master, text="Сброс", command=self.reset_timer)
        self.reset_button.pack(pady=10)
        
        self.is_running = False
        self.start_time = None
        self.update()
        
    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now()
            self.update()
        
    def stop_timer(self):
        if self.is_running:
            self.is_running = False
        
    def reset_timer(self):
        self.is_running = False
        self.start_time = None
        self.time_var.set("00:00:00")
        
    def update(self):
        if self.is_running:
            elapsed_time = datetime.now() - self.start_time
            time_str = str(elapsed_time).split(".")[0]
            self.time_var.set(time_str)
            self.master.after(1000, self.update)  # Обновление каждую секунду
        else:
            self.master.after(100, self.update)

if __name__ == "__main__":
    input("""
    =======================================================
    ==  Это таймер на питоне с графическим отображением  ==
    ==  Разрабатывался в качестве развелечения, можете   ==
    ==  Использовать как хотите.                         ==
    =======================================================
    ==================   Автор: @misha023    ==============
    =======================================================
          

Для продолжения нажмите Enter...""")
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()