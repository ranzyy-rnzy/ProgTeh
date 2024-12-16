import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Крестики-Нолики")
        master.geometry("320x450")

        self.size = 10
        self.win_length = 4

        # Цвета
        self.bg_color = "#F0F0F0"
        self.line_color = "#333333"
        self.default_tile_color = "#ADD8E6"
        self.x_color = "#007AFF"
        self.o_color = "#FF3B30"
        self.menu_bg_color = "#4CAF50"

        self.create_main_menu()

    def create_main_menu(self):
        self.main_menu_frame = tk.Frame(self.master, bg=self.menu_bg_color)
        self.main_menu_frame.pack(fill="both", expand=True)

        # Заголовок
        title_label = tk.Label(
            self.main_menu_frame,
            text=" Крестики-Нолики \n\n(▀̿Ĺ̯▀̿̿)\n 0_//||\\\_X \n||\n _|| ||_",
            font=("Helvetica", 24, "bold"),
            bg=self.menu_bg_color
        )
        title_label.pack(pady=30)

        # Кнопка "Играть"
        play_button = tk.Button(
            self.main_menu_frame,
            text="  Играть  ",
            font=("Helvetica", 24),
            command=self.start_game,
            bg="#4CAF50",
            activebackground="#45a049"
        )
        play_button.pack(pady=10)

        # Кнопка "Выйти"
        exit_button = tk.Button(
            self.main_menu_frame,
            text="  Выйти  ",
            font=("Helvetica", 24),
            command=self.master.destroy,
            bg="#4CAF50",
            activebackground="#45a049"
        )
        exit_button.pack(pady=10)

    def start_game(self):
        self.main_menu_frame.destroy()
        self.create_game_board()

    def create_game_board(self):
        self.current_player = "X"
        self.board = [['' for _ in range(self.size)] for _ in range(self.size)]

        self.game_frame = tk.Frame(self.master)
        self.game_frame.pack(fill="both", expand=True)

        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j] = tk.Button(
                    self.game_frame,
                    text="",
                    font=("Helvetica", 14),
                    width=2,
                    height=1,
                    command=lambda i=i, j=j: self.button_click(i, j),
                    bg=self.default_tile_color,
                    activebackground="#D0D0D0"
                )
                self.buttons[i][j].grid(row=i, column=j)

    def button_click(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player

            if self.current_player == "X":
                self.buttons[row][col].config(text=self.current_player, bg=self.x_color)
            else:
                self.buttons[row][col].config(text=self.current_player, bg=self.o_color)

            self.buttons[row][col]['state'] = 'disabled'

            if self.check_win():
                self.show_game_over_menu("Победа!", f"Игрок {self.current_player} победил!\nദ്ദി( • ᴗ - ) ✧")
            elif self.is_board_full():
                self.show_game_over_menu("Ничья!", "Доска заполнена!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Проверка по горизонтали и вертикали
        for i in range(self.size):
            for j in range(self.size - self.win_length + 1):
                if self.check_line(self.board[i][j:j + self.win_length]) or \
                   self.check_line([self.board[k][i] for k in range(j, j + self.win_length)]):
                    return True

        # Проверка по диагоналям
        for i in range(self.size - self.win_length + 1):
            for j in range(self.size - self.win_length + 1):
                if self.check_line([self.board[i + k][j + k] for k in range(self.win_length)]) or \
                   self.check_line([self.board[i + k][j + self.win_length - 1 - k] for k in range(self.win_length)]):
                    return True

        return False

    def check_line(self, line):
        return len(set(line)) == 1 and line[0] != ''

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True

    def show_game_over_menu(self, title, message):
        self.game_frame.destroy()
        self.result_frame = tk.Frame(self.master, bg=self.menu_bg_color)
        self.result_frame.pack(fill="both", expand=True)

        result_label = tk.Label(
            self.result_frame,
            text=message,
            font=("Helvetica", 24),
            bg=self.menu_bg_color
        )
        result_label.pack(pady=20)

        # Кнопка "Играть снова"
        play_again_button = tk.Button(
            self.result_frame,
            text="  Играть снова  ",
            font=("Helvetica", 24),
            command=self.restart_game,
            bg="#4CAF50",
            activebackground="#45a049"
        )
        play_again_button.pack(pady=10)

        # Кнопка "Выйти"
        exit_button = tk.Button(
            self.result_frame,
            text="  Выйти  ",
            font=("Helvetica", 24),
            command=self.master.destroy,
            bg="#4CAF50",
            activebackground="#45a049"
        )
        exit_button.pack(pady=10)

    def restart_game(self):
        self.result_frame.destroy()
        self.create_game_board()

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
