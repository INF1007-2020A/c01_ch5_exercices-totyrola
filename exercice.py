#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
from timeit import repeat
from itertools import product



def convert_to_absolute() -> float:
    nombre = float(input("Veuillez choisir un nombre:"))
    return abs(nombre)


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    resultat = []
    for i in range(len(prefixes))
        nom = prefixes[i] + suffixe


def prime_integer_summation() -> int:
    return 0


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
