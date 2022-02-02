from typing import List


class Hero:
    def __init__(self, x_pos: int, y_pos: int) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, dx: int, dy: int) -> None:
        self.x_pos += dx
        self.y_pos += dy


class Villain:
    def __init__(self, x_pos: int, y_pos: int) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, dx: int, dy: int) -> None:
        self.x_pos += dx
        self.y_pos += dy


class World:
    def __init__(
        self, name: str, heroes: List[Hero] = [], villains: List[Villain] = []
    ) -> None:
        self.name = name
        self.heroes: List[Hero] = []
        self.villains: List[Villain] = []

    def add_hero(self, hero: Hero) -> None:
        self.heroes.append(hero)

    def add_villain(self, villain: Villain) -> None:
        self.villains.append(villain)


if __name__ == "__main__":
    world = World("Earth")
    hero = Hero(0, 0)
    villain = Villain(-5, 10)
    world.add_villain(hero)
