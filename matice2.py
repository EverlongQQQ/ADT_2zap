import numpy as np

# Hodnocení
# Za správnou hodnotu answ [+3]
# Za správnou hodnotu square [+3]



def search_square(field: np.ndarray) -> tuple[int, np.ndarray]:
    row_count = field.shape[0]
    col_count = field.shape[1]

    largest_square_size = min(row_count, col_count)  # Největší možná velikost čtverce

    answ = 0
    largest_square = None

    for size in range(2, largest_square_size + 1):  # Začínáme od čtverců o velikosti 2x2 a postupně zvětšujeme
        for row in range(row_count - size + 1):  # Iterace přes řádky
            for col in range(col_count - size + 1):  # Iterace přes sloupce
                # Získání aktuálního čtverce o velikosti 'size' na pozici (row, col)
                current_square = field[row:row + size, col:col + size]
                # Kontrola, zda se v tomto čtverci žádné číslo neopakuje
                if np.unique(current_square).size == current_square.size:
                    # Pokud je tento čtverec větší než dosud nalezený, aktualizujeme odpověď
                    if size > answ:
                        answ = size
                        largest_square = current_square

    return answ, largest_square



def main():
    rows = 10
    cols = 15

    field = np.arange(rows * cols, dtype=int).reshape(rows, cols)  # vytvoříme pole 10x15 s čísly 0-99 - žádné se neopakují
    print(field)

    print(search_square(field))

    rows = 20
    cols = 5

    field = np.random.randint(100, size=(rows, cols), dtype=int)  # vytvoříme pole 20x5 s náhodnými čísly 0-99
    print(field)

    print(search_square(field))


if __name__ == "__main__":
    main()


