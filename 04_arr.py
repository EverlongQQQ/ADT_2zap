import numpy as np

# Hodnocení
# Za správnou hodnotu answ [+3]
# Za správnou hodnotu square [+3]



def search_square(field: np.ndarray) -> tuple[int, np.ndarray]:
    """
    Funkce postupně vyzkouší všechny výřezy pole dle zadané otázky a vrátí odpověď.

    arguments:
        field: np.ndarray - dvourozměrné pole s celými čísly
    returns
        tuple[int,np.ndarray] - odpověď na otázku.

    """
    # následující 2 řádky zjistí velikost pole
    row_count = field.shape[0]
    col_count = field.shape[1]

    answ = 0
    square = None

    
    # TODO Otázka: Jaký největší čtverec v dvourozměrném poli field najdeme, aby v něm nebyl žádný prvek dvakrát? Vraťte velikost strany čtverce a čtverec samotný. Pokud je více takových čtverců, vraťte ten, který má levý horní roh na řádku s nižším indexem, v případě shody na sloupci s nižším indexem.
    
    print(square)
    print(answ)
    
    return answ, square


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


