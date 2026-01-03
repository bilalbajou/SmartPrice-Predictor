import tkinter as tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class ProfitChart(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.figure.patch.set_facecolor('#2b2b2b') # Dark background match
        self.ax.set_facecolor('#2b2b2b')
        
        # Initial empty plot
        self.ax.set_title("Profit vs Prix", color='white')
        self.ax.set_xlabel("Prix ($)", color='white')
        self.ax.set_ylabel("Profit ($)", color='white')
        self.ax.tick_params(colors='white')
        for spine in self.ax.spines.values():
            spine.set_color('white')
            
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
    def plot_curve(self, optimal_price):
        """
        Plots a heuristic profit curve peaking at optimal_price.
        """
        self.ax.clear()
        
        # Create a quadratic curve centered at optimal_price
        # Profit = -a(x - h)^2 + k
        # purely visual heuristic: Profit peaks at optimal_price
        
        x = np.linspace(max(0, optimal_price * 0.5), optimal_price * 1.5, 100)
        # Assume profit is 0 at 0 and 2*optimal_price for simplicity visual
        # P(p) = p * (Demand) -> Demand = a - b*p
        # If optimal_price is where MR=MC or simple max revenue P*Q
        # Let's just draw a parabola peaking at optimal_price
        
        peak_profit = optimal_price * 100 # Arbitrary scale
        y = -1 * (x - optimal_price)**2 + peak_profit
        
        self.ax.plot(x, y, color='#1f6aa5', linewidth=2)
        self.ax.axvline(x=optimal_price, color='green', linestyle='--', label=f'Optimal: ${optimal_price:.2f}')
        
        self.ax.set_title("Profit Prédictif vs Prix", color='white')
        self.ax.set_xlabel("Prix ($)", color='white')
        self.ax.set_ylabel("Profit (Indice)", color='white')
        self.ax.tick_params(colors='white')
        self.ax.legend()
        for spine in self.ax.spines.values():
            spine.set_color('white')
            
        self.canvas.draw()
