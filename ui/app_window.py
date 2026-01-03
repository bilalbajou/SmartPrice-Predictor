import customtkinter as ctk
from .panels import InputPanel, ResultPanel
from .charts import ProfitChart
from core.solver import LUSolver

class SmartPriceApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("SmartPrice Predictor - Moteur de Décomposition LU")
        self.geometry("1100x700")
        
        # Grid Configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Left Sidebar (Inputs)
        self.input_panel = InputPanel(self, calculate_callback=self.handle_calculation, width=300)
        self.input_panel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Right Content Area
        self.right_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        
        # Results (Top Right)
        self.result_panel = ResultPanel(self.right_frame, height=250)
        self.result_panel.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        
        # Chart (Bottom Right)
        self.chart_panel = ProfitChart(self.right_frame)
        self.chart_panel.grid(row=1, column=0, sticky="nsew")
        
    def handle_calculation(self, A, b):
        """
        Callback from InputPanel. Coordinates solving and updating views.
        """
        print(f"Calculating for A={A}, b={b}...")
        results = LUSolver.solve_system(A, b)
        
        self.result_panel.display_results(results)
        
        if results['stable'] and results['x']:
            # Use the first element of solution as 'Optimized Price' for visualization
            optimal_price = results['x'][0]
            self.chart_panel.plot_curve(optimal_price)
