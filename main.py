import customtkinter as ctk
from ui.app_window import SmartPriceApp

def main():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    
    app = SmartPriceApp()
    app.mainloop()

if __name__ == "__main__":
    main()
