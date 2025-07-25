import tkinter as tk
from tkinter import ttk

class TrafficLightApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🚦 Traffic Light Simulator")
        self.geometry("300x400")
        self.resizable(False, False)

        # Set main window background color
        self.configure(bg="#2E2E2E")  # Dark charcoal

        # Use ttk for modern styling
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#2E2E2E")
        style.configure("TLabel", background="#2E2E2E", foreground="yellow")
        style.configure("TButton", background="#4A90E2", foreground="yellow", padding=6)
        style.map("TButton", background=[("active", "#357ABD")])

        # Main frame container
        main_frame = ttk.Frame(self, padding=10)
        main_frame.pack(fill="both", expand=True)

        # Canvas for the traffic light
        self.canvas = tk.Canvas(main_frame, width=150, height=300,
                                bg="#2E2E2E", highlightthickness=0)
        self.canvas.pack(side="left", padx=10, pady=10)

        # Draw housing and lights
        self.canvas.create_rectangle(25, 20, 125, 280, fill="#111", outline="#333", width=2)
        self.red = self.canvas.create_oval(40, 30, 110, 100, fill="gray")
        self.yellow = self.canvas.create_oval(40, 110, 110, 180, fill="gray")
        self.green = self.canvas.create_oval(40, 190, 110, 260, fill="gray")

        # Control panel
        ctrl_frame = ttk.Frame(main_frame)
        ctrl_frame.pack(side="right", fill="y", padx=(10, 0))

        ttk.Label(ctrl_frame, text="State:", font=("Segoe UI", 14, "bold")).pack(pady=(0, 10))
        self.state_lbl = ttk.Label(ctrl_frame, text="Red", font=("Segoe UI", 16))
        self.state_lbl.pack(pady=(0, 20))

        btn_frame = ttk.Frame(ctrl_frame)
        btn_frame.pack(fill="x", pady=(0, 10))
        for (text, cmd) in [("🚦 Start", self.start), ("⏸️ Pause", self.pause), ("🔄 Reset", self.reset)]:
            ttk.Button(btn_frame, text=text, command=cmd).pack(side="left", expand=True, padx=5)

        # Initialize light state
        self.states = [("red", 3000), ("green", 3000), ("yellow", 1000)]
        self.current = 0
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self._cycle()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.current = 0
        self._update_lights("red")

    def _cycle(self):
        state, delay = self.states[self.current]
        self._update_lights(state)
        if self.running:
            self.current = (self.current + 1) % len(self.states)
            self.after(delay, self._cycle)

    def _update_lights(self, state):
        self.canvas.itemconfig(self.red, fill="red" if state=="red" else "gray")
        self.canvas.itemconfig(self.yellow, fill="yellow" if state=="yellow" else "gray")
        self.canvas.itemconfig(self.green, fill="green" if state=="green" else "gray")
        self.state_lbl.config(text=state.capitalize())

if __name__ == "__main__":
    TrafficLightApp().mainloop()
