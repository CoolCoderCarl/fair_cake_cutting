from random import choice, randrange
from typing import Dict, List

persons = 2


def generate_cake_tastes() -> List[str]:
    filling = ["chocolate"] #, "vanilla"]
    cherry = randrange(6)
    return [choice(filling), cherry]


def generate_preferences() -> Dict[int, list[str]]:
    persons_preferences = {}
    for p in range(persons):
        persons_preferences[p] = generate_cake_tastes()
    return persons_preferences


def who_wants(cake: list, preferences: dict):
    want_count = 0
    wont_count = 0
    for keys in preferences:
        for l in range(persons):
            if cake[0] == preferences[keys][l]:
                print(
                    "Person " + str(list(preferences.keys())[keys]) + " is want a cake"
                )
                want_count += 1
                if want_count == persons:
                    # print(cake[1])
                    for v in list(preferences.values()):
                        print(v[1])
                break
            elif cake[0] != preferences[keys][l]:
                print(
                    "Person "
                    + str(list(preferences.keys())[keys])
                    + " is do not want a cake"
                )
                wont_count += 1
                if wont_count == persons:
                    print("No one want a cake")
                    exit(1)
                break


if __name__ == "__main__":
    cake = generate_cake_tastes()
    preferences = generate_preferences()
    print("The cake is " + cake[0] + " with " + str(cake[1]) + " cherries.")
    print(preferences)
    who_wants(cake, preferences)
