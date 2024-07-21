import tkinter as tk

class NQueensVisualizer:
    def __init__(self, N):
        self.N = N
        self.window = tk.Tk()
        self.window.title(f"{N}-Queens Problem")
        self.canvas = tk.Canvas(self.window, width=600, height=600)
        self.canvas.pack()
        self.board = [[0] * N for _ in range(N)]
        self.cell_size = 600 // N
        self.draw_board()  
        self.solve_n_queens()

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.N):
            for j in range(self.N):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                color = "white" if (i + j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                if self.board[i][j] == 1:
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="black")

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(row, self.N), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True

    def solve_n_queens_util(self, col):
        if col >= self.N:
            return True
        for i in range(self.N):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                self.draw_board()
                self.window.update_idletasks()
                if self.solve_n_queens_util(col + 1):
                    return True
                self.board[i][col] = 0
                self.draw_board()
                self.window.update_idletasks()
        return False

    def solve_n_queens(self):
        if not self.solve_n_queens_util(0):
            print("Solution does not exist")
        else:
            print("Solution found")

if __name__ == "__main__":
    N = 8  # N values
    visualizer = NQueensVisualizer(N)
    visualizer.window.mainloop()

