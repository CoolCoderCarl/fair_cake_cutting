from random import choice, randrange
from typing import Dict, List

persons = 2


def generate_cake_tastes() -> List[str]:
    filling = ["chocolate", "vanilla"]
    cherry = randrange(6)
    return [choice(filling), cherry]


def generate_preferences() -> Dict[int, list[str]]:
    persons_preferences = {}
    for p in range(persons):
        persons_preferences[p] = generate_cake_tastes()
    return persons_preferences


if __name__ == "__main__":
    cake = generate_cake_tastes()
    preferences = generate_preferences()
    print("The cake is " + cake[0] + " with " + str(cake[1]) + " cherries.")
    for keys in preferences:
        print(preferences[keys])

