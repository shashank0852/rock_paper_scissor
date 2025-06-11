import tkinter as tk
from tkinter import font as tkfont
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        # --- Color Palette ---
        self.COLOR_BACKGROUND = "#2c3e50"  # Dark Slate Blue
        self.COLOR_PRIMARY = "#3498db"     # Bright Blue
        self.COLOR_SECONDARY = "#2ecc71"   # Emerald Green
        self.COLOR_TEXT = "#ecf0f1"        # Light Gray/White
        self.COLOR_BUTTON = "#34495e"      # Wet Asphalt
        self.COLOR_BUTTON_HOVER = "#4a627a"
        
        self.COLOR_WIN = "#27ae60"         # Nephritis Green
        self.COLOR_LOSE = "#c0392b"        # Pomegranate Red
        self.COLOR_DRAW = "#f39c12"        # Orange

        self.root.configure(bg=self.COLOR_BACKGROUND)

        # --- Fonts ---
        self.title_font = tkfont.Font(family="Segoe UI", size=26, weight="bold")
        self.score_font = tkfont.Font(family="Segoe UI", size=14)
        self.result_font = tkfont.Font(family="Segoe UI", size=18, weight="bold")
        self.button_font = tkfont.Font(family="Segoe UI", size=14, weight="bold")

        # --- Game State ---
        self.game_over = False
        self.choices = ["Rock", "Paper", "Scissors"]
        
        # --- Create Widgets ---
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        # --- Title Label ---
        title = tk.Label(self.root, text="Rock Paper Scissors", font=self.title_font, bg=self.COLOR_BACKGROUND, fg=self.COLOR_TEXT)
        title.pack(pady=(20, 10))

        # --- Score Frame ---
        score_frame = tk.Frame(self.root, bg=self.COLOR_BACKGROUND)
        score_frame.pack(pady=20, fill="x", padx=30)
        
        self.player_label = tk.Label(score_frame, text="PLAYER", font=self.score_font, bg=self.COLOR_BACKGROUND, fg=self.COLOR_PRIMARY)
        self.player_label.pack(side="left", expand=True)
        
        vs_label = tk.Label(score_frame, text="VS", font=self.score_font, bg=self.COLOR_BACKGROUND, fg=self.COLOR_TEXT)
        vs_label.pack(side="left", expand=True)
        
        self.computer_label = tk.Label(score_frame, text="COMPUTER", font=self.score_font, bg=self.COLOR_BACKGROUND, fg=self.COLOR_PRIMARY)
        self.computer_label.pack(side="right", expand=True)

        # --- Player/Computer Choice Display ---
        choice_frame = tk.Frame(self.root, bg=self.COLOR_BACKGROUND)
        choice_frame.pack(pady=5, fill="x", padx=30)
        
        self.player_choice_label = tk.Label(choice_frame, text="---", font=self.result_font, bg=self.COLOR_BACKGROUND, fg=self.COLOR_TEXT, width=10)
        self.player_choice_label.pack(side="left", expand=True)

        self.computer_choice_label = tk.Label(choice_frame, text="---", font=self.result_font, bg=self.COLOR_BACKGROUND, fg=self.COLOR_TEXT, width=10)
        self.computer_choice_label.pack(side="right", expand=True)

        # --- Result Label ---
        self.result_label = tk.Label(self.root, text="Make your choice!", font=self.result_font, bg=self.COLOR_BACKGROUND, fg=self.COLOR_TEXT, pady=10)
        self.result_label.pack(pady=(15, 20))

        # --- Buttons Frame ---
        button_frame = tk.Frame(self.root, bg=self.COLOR_BACKGROUND)
        button_frame.pack(pady=20)
        
        self.rock_btn = self.create_choice_button(button_frame, "🗿 Rock", "Rock")
        self.paper_btn = self.create_choice_button(button_frame, "📄 Paper", "Paper")
        self.scissor_btn = self.create_choice_button(button_frame, "✂️ Scissors", "Scissor")

        self.rock_btn.pack(side="left", padx=10)
        self.paper_btn.pack(side="left", padx=10)
        self.scissor_btn.pack(side="left", padx=10)

        # --- Reset Button ---
        self.reset_btn = tk.Button(self.root, text="Play Again", font=self.button_font, bg=self.COLOR_SECONDARY, fg=self.COLOR_BACKGROUND,
                                   width=15, relief=tk.FLAT, bd=0, command=self.reset_game)
        self.reset_btn.pack(pady=(10, 20))
        self.bind_hover(self.reset_btn, self.COLOR_SECONDARY, "#25a25a")


    def create_choice_button(self, parent, text, choice):
        """Helper to create a styled choice button."""
        btn = tk.Button(parent, text=text, font=self.button_font, bg=self.COLOR_BUTTON, fg=self.COLOR_TEXT,
                        width=10, relief=tk.FLAT, bd=0, command=lambda: self.play(choice))
        self.bind_hover(btn, self.COLOR_BUTTON, self.COLOR_BUTTON_HOVER)
        return btn

    def bind_hover(self, button, bg_color, hover_color):
        """Binds Enter and Leave events to change button color."""
        button.bind("<Enter>", lambda e: button.config(bg=hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=bg_color))

    def play(self, player_choice):
        if self.game_over:
            return

        self.game_over = True
        comp_choice = random.choice(self.choices)

        self.player_choice_label.config(text=player_choice)
        self.computer_choice_label.config(text=comp_choice)
        
        self.toggle_choice_buttons(state="disabled")

        if comp_choice == player_choice:
            self.result_label.config(text="It's a Draw!", bg=self.COLOR_DRAW)
        elif (player_choice == "Rock" and comp_choice == "Scissors") or \
             (player_choice == "Paper" and comp_choice == "Rock") or \
             (player_choice == "Scissors" and comp_choice == "Paper"):
            self.result_label.config(text="You Win!", bg=self.COLOR_WIN)
        else:
            self.result_label.config(text="Computer Wins!", bg=self.COLOR_LOSE)

    def reset_game(self):
        self.game_over = False
        self.result_label.config(text="Make your choice!", bg=self.COLOR_BACKGROUND)
        self.player_choice_label.config(text="---")
        self.computer_choice_label.config(text="---")
        self.toggle_choice_buttons(state="normal")
        
    def toggle_choice_buttons(self, state):
        """Enables or disables the choice buttons."""
        if state not in ["normal", "disabled"]: return
        self.rock_btn.config(state=state)
        self.paper_btn.config(state=state)
        self.scissor_btn.config(state=state)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()

