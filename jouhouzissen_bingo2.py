import tkinter as tk
import random

class BingoCard:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo Card Generator")
        self.card_numbers = self.generate_card()
        self.selected_cells = set()
        self.buttons = []

        self.create_card_gui()

    def generate_card(self):

        ranges = {
            'B': range(1, 16),
            'I': range(16, 31),
            'N': range(31, 46),
            'G': range(46, 61),
            'O': range(61, 76)
        }
        
        card = []
        for col, num_range in ranges.items():
            numbers = random.sample(num_range, 5)
            card.append(numbers)
        
        card[2][2] = "FREE"  
        return list(map(list, zip(*card)))  

    def create_card_gui(self):
        for row in range(5):
            row_buttons = []
            for col in range(5):
                number = self.card_numbers[row][col]
                btn = tk.Button(
                    self.root, text=str(number), width=6, height=3,
                    command=lambda r=row, c=col: self.select_number(r, c)
                )
                btn.grid(row=row, column=col)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def select_number(self, row, col):
        if (row, col) in self.selected_cells:
            return
        self.selected_cells.add((row, col))
        self.buttons[row][col].config(bg="yellow")
        self.check_bingo()

    def check_bingo(self):
        bingo_count = 0
        reach_count = 0

        for i in range(5):
            row_selected = [1 if (i, j) in self.selected_cells or (i == 2 and j == 2) else 0 for j in range(5)]
            col_selected = [1 if (j, i) in self.selected_cells or (j == 2 and i == 2) else 0 for j in range(5)]
            
            if sum(row_selected) == 5:
                bingo_count += 1
            elif sum(row_selected) == 4:
                reach_count += 1
                
            if sum(col_selected) == 5:
                bingo_count += 1
            elif sum(col_selected) == 4:
                reach_count += 1

        diag1_selected = [1 if (i, i) in self.selected_cells or (i == 2 and i == 2) else 0 for i in range(5)]
        diag2_selected = [1 if (i, 4 - i) in self.selected_cells or (i == 2 and 4 - i == 2) else 0 for i in range(5)]
        
        if sum(diag1_selected) == 5:
            bingo_count += 1
        elif sum(diag1_selected) == 4:
            reach_count += 1
            
        if sum(diag2_selected) == 5:
            bingo_count += 1
        elif sum(diag2_selected) == 4:
            reach_count += 1

        if bingo_count > 0:
            print("ビンゴ！")
        elif reach_count > 0:
            print("リーチ！")

root = tk.Tk()
bingo_app = BingoCard(root)
root.mainloop()