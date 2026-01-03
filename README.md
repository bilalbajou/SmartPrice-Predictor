# SmartPrice Predictor 📊

**SmartPrice Predictor** is a powerful desktop application tailored for business decision-making. It leverages advanced mathematical modeling (**LU Decomposition**) to solve market equilibrium problems and predict optimal pricing strategies.

Designed with a modern, business-centric interface, it bridges the gap between complex linear algebra and actionable strategic insights.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

## 🌟 Features

*   **Advanced Math Engine**: Utilizes `Scipy` and `NumPy` for efficient LU Decomposition ($A = LU$) to solve linear systems ($Ax = b$).
*   **Business Intelligence**:
    *   Translates mathematical results into strategic business advice (Opportunity vs Risk).
    *   Calculates Market Stability using Determinants.
    *   Provides clear actionable pricing recommendations.
*   **Interactive Visualization**: Real-time **Matplotlib** charting to visualize purely predictive Profit vs Price curves.
*   **Modern UI**: Built with **CustomTkinter** for a sleek, dark-themed professional experience.
*   **French Localization**: Fully localized user interface for French-speaking business environments.

## 🛠️ Technology Stack

*   **Language**: Python 3.x
*   **GUI Framework**: [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
*   **Mathematics**: NumPy, SciPy
*   **Visualization**: Matplotlib

## 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/smartprice-predictor.git
    cd smartprice-predictor
    ```

2.  **Install Dependencies**
    Ensure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    python main.py
    ```

## 📖 Usage Guide

The application is divided into two main panels:

1.  **Left Panel (Entrées du Marché)**
    *   **Matrice A (Facteurs)**: Input your market constraints coefficients (e.g., cost structures, elasticity).
    *   **Vecteur b (Objectifs)**: Input your market targets (e.g., demand limits, stock constraints).
    *   Select Matrix Size (2x2 or 3x3) to match your model complexity.

2.  **Right Panel (Résultats & Stratégie)**
    *   Click **"Calculer l'Optimisation"**.
    *   **Stability Check**: The app inspects the determinant.
        *   🟢 **Green**: Market is stable. Optimal prices are displayed.
        *   🔴 **Red**: Market is unstable (Singular Matrix). Risk warning displayed.
    *   **Visuals**: View the projected profit curve based on the calculated optimal price point.

## 📂 Project Structure

```
SmartPrice-Predictor/
├── core/               # Mathematical Logic
│   └── solver.py       # LU Decomposition Implementation
├── ui/                 # User Interface
│   ├── app_window.py   # Main Window Setup
│   ├── panels.py       # Input/Result Panels
│   └── charts.py       # Matplotlib Visualizations
├── tests/              # Unit Tests
├── main.py             # Application Entry Point
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
