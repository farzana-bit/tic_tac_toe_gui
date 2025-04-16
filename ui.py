import tkinter as tk
import pygame
import random
import math
from tkinter import messagebox
from game import TicTacToeGame

def draw_heart(canvas, x, y, size, color):
       return canvas.create_text(x, y, text="💗", font=("Arial", size), fill=color)


def draw_star(canvas, x, y, size, color):
       return canvas.create_text(x, y, text="⭐", font=("Arial", size), fill=color)



class TicTacToeGUI:
    def __init__(self):
        self.game = TicTacToeGame()
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#fff5f7")  # pastel blush background
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.build_ui()
        pygame.mixer.init()
        pygame.mixer.music.load("cute_music.mp3")  # or .wav
        pygame.mixer.music.play(-1)  # Loop forever

    def build_ui(self):
        frame = tk.Frame(self.root, bg="#fff5f7")
        frame.pack()
        for row in range(3):
            for col in range(3):
                btn = tk.Button(frame,
                                text="",
                                font=("Segoe Print", 28, "bold"),
                                width=4,
                                height=2,
                                bg="#ffe6f0",  # soft pink
                                fg="#5D3A00",  # chocolate brown
                                activebackground="#ffd9ec",
                                activeforeground="#5D3A00",
                                bd=0,
                                highlightthickness=2,
                                highlightbackground="#ffb6c1",
                                relief="ridge",
                                cursor="hand2",
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col, padx=10, pady=10)
                self.buttons[row][col] = btn

        self.reset_btn = tk.Button(
            self.root,
            text="💖 Play Again",
            font=("Segoe Print", 14, "bold"),
            bg="#c3f0ca",       # pastel green
            fg="#2e4a1b",       # forest green
            activebackground="#a3e4b5",
            activeforeground="#2e4a1b",
            bd=0,
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.reset_game
                                   )
        self.reset_btn.pack(pady=10)

    def on_click(self, row, col):
        if self.game.board[row][col] == "" and self.game.winner is None:
            self.game.make_move(row, col)
            self.update_ui()

            if self.game.winner:
                if self.game.winner == "Draw":
                    messagebox.showinfo("Game Over", "It's a draw!")
                else:
                    messagebox.showinfo(
                        "Game Over", f"Player {self.game.winner} wins!")
                self.disable_buttons()
                self.show_game_over_popup()
                self.show_confetti()  # 🎉

    def update_ui(self):
        for row in range(3):
            for col in range(3):
                # self.buttons[row][col]["text"] = self.game.board[row][col]
                                
                    for row in range(3):
                        for col in range(3):
                            value = self.game.board[row][col]
                            if value == "X":
                                self.buttons[row][col]["text"] = "🥕"
                            elif value == "O":
                                self.buttons[row][col]["text"] = "🐰"
                            else:
                                self.buttons[row][col]["text"] = ""


    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["state"] = "disabled"

    def reset_game(self):
        self.game.reset_game()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
                self.buttons[row][col]["state"] = "normal"

    def show_game_over_popup(self):
       winner = self.game.winner
       if winner == "Draw":
        message = "😸 It's a draw! Try again!"
       else:
        emoji = "🐱" if winner == "X" else "🐰"
        message = f"{emoji} {winner} wins! Yay!! 🎉"

        messagebox.showinfo("Game Over 🎀", message)
    
    
    
    def show_confetti(self):
        canvas = tk.Canvas(self.root, width=400, height=400,
                       bg="#fff5f7", highlightthickness=0)
        canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Fun shapes: circles, hearts, stars
        shapes = ["circle", "heart", "star"]
        colors = ["#ffb6c1", "#ffd700", "#98fb98", "#add8e6", "#ff69b4", "#fcb0b3"]

        particles = []

        for _ in range(40):
            x = random.randint(50, 350)
            y = random.randint(50, 350)
            size = random.randint(10, 20)
            shape_type = random.choice(shapes)
            color = random.choice(colors)

            if shape_type == "circle":
                shape = canvas.create_oval(
                    x, y, x+size, y+size, fill=color, outline="")
            elif shape_type == "heart":
                shape = draw_heart(canvas, x, y, size, color)
            elif shape_type == "star":
                shape = draw_star(canvas, x, y, size, color)

            particles.append(
               (shape, x, y, random.uniform(-1, 1), random.uniform(-2, -1)))

        def animate():
            for i, (shape, x, y, dx, dy) in enumerate(particles):
                x += dx
                y += dy
                dy += 0.1  # gravity
                canvas.move(shape, dx, dy)
                particles[i] = (shape, x, y, dx, dy)
            self.root.after(50, animate)

        animate()
        self.root.after(3000, canvas.destroy)

    

    


    def run(self):
        self.root.mainloop()
