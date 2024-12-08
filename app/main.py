class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def remove_dead(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    @classmethod
    def __str__(cls) -> str:
        return str([repr(animal) for animal in cls.alive])

    @classmethod
    def print_alive(cls) -> list:
        return cls.alive


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: "Animal") -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                other.health = 0
                Animal.remove_dead()
