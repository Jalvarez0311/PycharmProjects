import tkinter as tk
import requests
import time

class SystemMonitor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("System Monitor")
        self.geometry("300x150")

        self.cpu_label = tk.Label(self, text="CPU Usage: ")
        self.cpu_label.pack()

        self.disk_label = tk.Label(self, text="Disk Usage: ")
        self.disk_label.pack()

        self.memory_label = tk.Label(self, text="Memory Usage: ")
        self.memory_label.pack()

        self.update_values()

    def update_values(self):
        try:
            cpu_usage = self.get_api_data("/remote/cpu")
            disk_usage = self.get_api_data("/remote/disk")
            memory_usage = self.get_api_data("/remote/mem")

            self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
            self.disk_label.config(text=f"Disk Usage: {disk_usage}%")
            self.memory_label.config(text=f"Memory Usage: {memory_usage}%")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")

        self.after(5000, self.update_values)  # Update every 5 seconds

    def get_api_data(self, endpoint):
        response = requests.get(f"http://127.0.0.1:8000{endpoint}")
        data = response.json()
        return data[f"{endpoint.split('/')[-1]}_usage"]

if __name__ == "__main__":
    app = SystemMonitor()
    app.mainloop()
