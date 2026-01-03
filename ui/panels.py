import customtkinter as ctk

class InputPanel(ctk.CTkFrame):
    def __init__(self, master, calculate_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.calculate_callback = calculate_callback
        
        # Title
        self.label = ctk.CTkLabel(self, text="Entrées du Marché", font=("Roboto", 16, "bold"))
        self.label.pack(pady=(10, 0), padx=10, anchor="w")
        
        # Subtitle/Description
        self.desc_label = ctk.CTkLabel(self, text="Configurez les paramètres d'offre et de demande.", font=("Roboto", 12), text_color="gray")
        self.desc_label.pack(pady=(0, 10), padx=10, anchor="w")
        
        # Matrix Size Selection
        self.size_var = ctk.StringVar(value="2")
        self.size_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.size_frame.pack(fill="x", padx=10)
        ctk.CTkLabel(self.size_frame, text="Taille Matrice:").pack(side="left")
        ctk.CTkRadioButton(self.size_frame, text="2x2", variable=self.size_var, value="2", command=self.update_inputs).pack(side="left", padx=10)
        ctk.CTkRadioButton(self.size_frame, text="3x3", variable=self.size_var, value="3", command=self.update_inputs).pack(side="left", padx=10)
        
        # Matrix A Inputs
        self.matrix_frame = ctk.CTkFrame(self)
        self.matrix_frame.pack(pady=10, padx=10, fill="x")
        self.a_entries = []
        
        # Vector b Inputs
        self.vector_frame = ctk.CTkFrame(self)
        self.vector_frame.pack(pady=10, padx=10, fill="x")
        self.b_entries = []
        
        self.update_inputs()
        
        # Calculate Button
        self.btn_calc = ctk.CTkButton(self, text="Calculer l'Optimisation", command=self.on_calculate)
        self.btn_calc.pack(pady=20, padx=10, fill="x")
        
    def update_inputs(self):
        # Clear existing
        for widget in self.matrix_frame.winfo_children(): widget.destroy()
        for widget in self.vector_frame.winfo_children(): widget.destroy()
        self.a_entries = []
        self.b_entries = []
        
        n = int(self.size_var.get())
        
        # Matrix A Header
        ctk.CTkLabel(self.matrix_frame, text="1. Paramètres d'Influence", font=("Roboto", 12, "bold")).grid(row=0, column=0, columnspan=n, pady=(5,0))
        ctk.CTkLabel(self.matrix_frame, text="(Coûts, Concurrence, Saisonalité)", font=("Roboto", 10), text_color="gray").grid(row=1, column=0, columnspan=n, pady=(0,5))
        
        for i in range(n):
            row_entries = []
            for j in range(n):
                entry = ctk.CTkEntry(self.matrix_frame, width=40, placeholder_text=f"A{i}{j}")
                entry.grid(row=i+2, column=j, padx=2, pady=2)
                # Default values for demo
                if i==j: entry.insert(0, "2")
                else: entry.insert(0, "1")
                row_entries.append(entry)
            self.a_entries.append(row_entries)
            
        # Vector b Header
        ctk.CTkLabel(self.vector_frame, text="2. Objectifs Commerciaux", font=("Roboto", 12, "bold")).grid(row=0, column=0, columnspan=n, pady=(5,0))
        ctk.CTkLabel(self.vector_frame, text="(Volume Cible, Capacité Max)", font=("Roboto", 10), text_color="gray").grid(row=1, column=0, columnspan=n, pady=(0,5))
        
        for i in range(n):
            entry = ctk.CTkEntry(self.vector_frame, width=40, placeholder_text=f"b{i}")
            entry.grid(row=2, column=i, padx=5, pady=2)
            entry.insert(0, "10")
            self.b_entries.append(entry)

    def on_calculate(self):
        try:
            n = int(self.size_var.get())
            A = []
            for i in range(n):
                row = []
                for j in range(n):
                    val = float(self.a_entries[i][j].get())
                    row.append(val)
                A.append(row)
            
            b = []
            for i in range(n):
                val = float(self.b_entries[i].get())
                b.append(val)
                
            self.calculate_callback(A, b)
        except ValueError:
            print("Entrée Invalide") # Should show error in UI ideally

class ResultPanel(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label = ctk.CTkLabel(self, text="Rapport d'Analyse Stratégique", font=("Roboto", 16, "bold"))
        self.label.pack(pady=10, padx=10, anchor="w")
        
        self.status_lbl = ctk.CTkLabel(self, text="Statut: En attente", text_color="gray")
        self.status_lbl.pack(anchor="w", padx=10)
        
        self.result_text = ctk.CTkTextbox(self, height=300)
        self.result_text.pack(fill="x", padx=10, pady=10)
        self.result_text.configure(state="disabled")
        
    def display_results(self, data):
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", "end")
        
        if data['stable']:
            self.status_lbl.configure(text="Statut: Marché Stable (Opportunité)", text_color="#2CC985") # Bright Green
            
            res = "INTERPRÉTATION BUSINESS:\n"
            res += "Le marché est en équilibre. Les paramètres actuels permettent une stratégie de prix viable.\n\n"
            res += f"Indice de Stabilité (Déterminant): {data['det']:.4f}\n"
            res += "--------------------------------------------------\n\n"
            
            res += "RECOMMANDATION STRATÉGIQUE (Solution x):\n"
            res += "Voici les valeurs optimales calculées (Prix/Unités) :\n"
            for i, val in enumerate(data['x']):
                res += f"  - Variable {i+1} : {val:.2f}\n"
            
            res += "\n--------------------------------------------------\n"
            res += "ANNEXE TECHNIQUE (Pour Analystes):\n"
            res += "Décomposition LU effectuée pour valider la robustesse du modèle.\n\n"
            
            res += "Facteurs de Scaling (L):\n"
            for row in data['L']:
                res += str([round(x, 2) for x in row]) + "\n"
            
            res += "\nMatrice Échelonnée (U):\n"
            for row in data['U']:
                res += str([round(x, 2) for x in row]) + "\n"
                
            self.result_text.insert("0.0", res)
        else:
            self.status_lbl.configure(text="Statut: Marché Instable (Risque Élevé)", text_color="#FF4B4B") # Bright Red
            
            res = "ALERTE CRITIQUE:\n"
            res += "Les contraintes du marché sont conflictuelles ou insuffisantes (Matrice Singulière).\n"
            res += "Impossible de déterminer un point d'équilibre unique.\n\n"
            res += f"Erreur Technique: {data.get('error', 'Déterminant = 0')}"
            
            self.result_text.insert("0.0", res)
            
        self.result_text.configure(state="disabled")
