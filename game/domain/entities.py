class Player:
    """
    Упрощенное представление игрока
    """
    def __init__(self):
        self.health = 0
        self.defence = 0
        self.attack = 0


class Turn:
    """
    Определяем атаку/защиту каждой части тела
    """
    def __init__(self):
        self.left_arm = False
        self.right_arm = False
        self.left_leg = False
        self.right_leg = False
        self.body = False
        self.head = False
