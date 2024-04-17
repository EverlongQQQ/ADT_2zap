import os
import random
import sys
import numpy as np



EMPTY_VALUE=0



class SudokuSolver:
    sudoku: np.ndarray

    def __init__(self, *args, **kwargs):
        self.sudoku = np.zeros([12, 12], dtype=int)#поменять размер массива на нужный

    @property
    def n_rows_prop(self) -> int:
        return self.sudoku.shape[0]

    @property
    def n_columns_prop(self) -> int:
        return self.sudoku.shape[1]


    def load(self, filepath: str) -> None:

        with open(filepath, 'r') as file:

            sudoku = []
            for line in file:

                row = []
                for char in line.strip().split():

                    if char.isdigit():

                        row.append(int(char))

                    elif char == "~":#заменить знак на нужный

                        row.append(EMPTY_VALUE)

                if row:

                    sudoku.append(row)

            self.sudoku = np.array(sudoku)

    def check_field(self) -> bool:
      for i in range(self.n_rows_prop):
          for j in range(self.n_columns_prop):
              if not self.check_one_cell(i, j):
                  return False
      return True






    def check_sequence(self, sequence: np.ndarray) -> bool:

        contains = set()


        for cell in sequence:


            if cell == 0:
                continue


            if cell in contains:

                return False

            contains.add(cell)


        return True


    def check_row(self, row_index: int) -> bool:

        row = self.sudoku[row_index, :]

        return self.check_sequence(row)


    def check_column(self, column_index: int) -> bool:

        column = self.sudoku[:, column_index]

        return self.check_sequence(column)


    def check_block(self, row, col):

      start_row = (row // 2) * 2
      start_col = (col // 6) * 6
      #start_row = (row // M) * M
      #start_col = (col // N) * N   где M - количество строк в блоке, а N - количество столбцов в блоке.
      block_values = set()
    # Проходим по всем ячейкам в блоке
    #for r in range(start_row, start_row + M):
    #for c in range(start_col, start_col + N):
      for r in range(start_row, start_row + 2):
          for c in range(start_col, start_col + 3):
              value = self.sudoku[r, c]
              if value != 0:
                # Если значение уже встречалось, возвращаем False
                  if value in block_values:
                      return False
                  block_values.add(value)
    # Если все значения уникальны, возвращаем True
      return True



    def check_one_cell(self, row_index: int, column_index: int) -> bool:
        return (

            self.check_row(row_index)

            and self.check_column(column_index)

            and self.check_block(row_index, column_index)
        )


    def solve(self) -> bool:

        for r in range(self.n_rows_prop):

            for c in range(self.n_columns_prop):

                if self.sudoku[r, c] != EMPTY_VALUE:
                    continue



                possible_values = list(range(1, 13))#первое число не трогать, второе заменить на максимальное возможное +1

                random.shuffle(possible_values)

                for value in possible_values:
                    self.sudoku[r, c] = value



                    if not self.check_one_cell(r, c):
                        continue



                    if self.solve():

                        return True


                self.sudoku[r, c] = EMPTY_VALUE

                return False



        return True




def main(filepath: str) -> None:

    sudoku_solver = SudokuSolver()

    sudoku_solver.load(filepath)

    sudoku_solver.solve()
    print(sudoku_solver.check_field())

    print(sudoku_solver.sudoku)


if __name__ == "__main__":

    arguments = sys.argv
    if len(arguments) < 2:
        print("give me file!")
        exit(1)
    sudoku_filepath = sys.argv[1]
    if not os.path.exists(sudoku_filepath):
        print("give me my file!")
        exit(2)

    main(sudoku_filepath)
