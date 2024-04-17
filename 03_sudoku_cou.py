import numpy as np

# Následující program obsahuje kostru řešení klasického sudoku.
# Vaším úkolem je upravit a doplnit program tak, aby řešil vám zadané sudoku a navíc spočetl počet všech možných řešení.

# Hodnocení:
# Za správný load ze souboru [+5]
# Za správně ověřovaný řádek [+0.5]
# Za správně ověřovaný sloupec [+0.5]
# Za správně ověřovaný blok [+0.5]
# Za správně ověřovanou pozici [+0.5]
# Za správně spočítaná různá řešení sudoku [+7]


class SudokuSolver:

    # neupravujte signaturu konstruktoru, tělo konstruktoru doplňte podle vaší potřeby
    def __init__(self, *args, **kwargs):
        #  !! neupravujte jméno proměnné (self.sudoku) bude použito pro automatickou kontrolu. Rozměr pole samozřejmě upravit můžete.
        self.sudoku = np.zeros([9, 9], dtype=int)

    def load(self, filepath: str) -> None:
        """
        Metoda načte sudoku ze souboru a uloží jej do proměnné self.sudoku.
        args:
            filepath: cesta k souboru se sudoku. Pro přesný formát souboru viz přiložené soubory.
        """
        # todo implementujte načítání ze souboru. Viz přiložené soubory.
        pass

    def check_one_cell(self, row_index: int, column_index: int) -> bool:
        """
        Metoda zkontroluje, zda je konkrétní pozice na souřadnici v self.sudoku v souladu s pravidly.
        args:
            row_index: index řádku
            column_index: index sloupce
        return:
            bool: True, pokud je pozice v souladu s pravidly, jinak False
        """
        # TODO implementujte kontrolu konkrétní souřadnice v sudoku
        return True

    def check_row(self, r_index: int) -> bool:
        """
        Metoda zkontroluje, zda je řádek v self.sudoku v souladu s pravidly.
        args:
            r_index: index řádku
        return:
            bool: True, pokud je řádek v souladu s pravidly, jinak False
        """
        # TODO implementujte kontrolu řádku
        return True

    def check_column(self, c_index: int) -> bool:
        """
        Metoda zkontroluje, zda je sloupec v self.sudoku v souladu s pravidly.
        args:
            c_index: index sloupce
        return:
            bool: True, pokud je sloupec v souladu s pravidly, jinak False
        """
        # TODO implementujte kontrolu sloupce
        return True

    def check_block(self, number_row_position: int, number_col_position: int) -> bool:
        """
        Metoda zkontroluje, zda je blok v self.sudoku v souladu s pravidly. Každý blok je jednoznačně určen kterýmkoli prvkem, který v něm leží.
        V klasickém sudoku, kde jsou bloky v rozměru 3x3 tedy všechny kombinace (0,0), (1,2), ..., (2,2). vede na stejný blok.

        args:
            number_row_position: index řádku konkrétního čísla v sudoku
            number_col_position: index sloupce konkrétního čísla v sudoku
        return:
            bool: True, pokud je blok, ve kterém leží souřadnice na vstupu, v souladu s pravidly, jinak False
        """

        # TODO implementujte kontrolu bloku nezapomeňte, že vám přidělená rodina sudoku může mít jiný tvar bloku.
        return True

    def solve(self) -> bool:
        """
        Metoda vyřeší sudoku. Tj. upraví pole self.sudoku tak, aby bylo vyřešené.
        return:
            bool: True, pokud se sudoku podařilo vyřešit, jinak False
        """

        # TODO implementujte řešení sudoku
        return False

    def check_field(self) -> bool:
        """
        Metoda zkontroluje, zda je celé pole self.sudoku v souladu s pravidly.
        return:
            bool: True, pokud je celé pole v souladu s pravidly, jinak False
        """
        # TODO implementujte kontrolu celého pole
        return True

    def count_all_different_solutions(self) -> int:
        """
        Metoda spočte všechna rozdílná řešení self.sudoku
        Returns:
            int: počet různých validních řešení self.sudoku
        """
        # TODO implementujte kód, který spočte všechna rozdílná řešení sudoku
        return 0


def main(filepath: str) -> int:
    """
    Hlavní funkce programu. Zde načtěte sudoku ze souboru a zavolejte metodu pro spočítání všech různých řešení.

    args:
        filepath: cesta k souboru se sudoku. Pro přesný formát souboru viz přiložené soubory.
    return:
        int: počet různých řešení konkrétního sudoku
    """
    n_solutions = 0

    sudoku_solver = SudokuSolver()

    # TODO načtete sudoku z filepath  pomocí metody load(self, filepath:str)

    # TODO Spočítejte počet všech různých řešení sudoku pomocí metody count_all_different_solutions() a uložte do proměnné n_solutions

    return n_solutions  # pro automatickou kontrolu


if __name__ == "__main__":
    # Program přijímá cestu k souboru. Bude spouštěn následujícím příkazem "python main.py path_to_sudoku.txt"
    # todo implementujte zpracování argumentu z příkazové řádky.
    sudoku_filepath = ""
    main(sudoku_filepath)


