import numpy as np

def search_square(field: np.ndarray) -> tuple[int, np.ndarray]:
    row_count, col_count = field.shape
    max_possible_size = min(row_count, col_count)

    for size in range(max_possible_size, 0, -1):
        seen = {}
        for start_row in range(row_count - size + 1):
            for start_col in range(col_count - size + 1):
                valid = True
                sub_square = field[start_row:start_row+size, start_col:start_col+size]
                unique_elements = set()
                
                for i in range(size):
                    for j in range(size):
                        element = sub_square[i, j]
                        if element in unique_elements:
                            valid = False
                            break
                        unique_elements.add(element)
                    if not valid:
                        break
                
                if valid:
                    return size, sub_square

    return 0, None

def main():
    rows = 10
    cols = 15
    field = np.arange(rows * cols, dtype=int).reshape(rows, cols)
    print("Initial array (10x15):")
    print(field)
    print("Largest unique square:")
    print(search_square(field))

    rows = 20
    cols = 5
    field = np.random.randint(100, size=(rows, cols), dtype=int)
    print("\nInitial array (20x5) with random numbers:")
    print(field)
    print("Largest unique square:")
    print(search_square(field))

if __name__ == "__main__":
    main()
