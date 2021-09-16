from model.character import *
from model.dnd_classes import *

PLAYER_GROUP_NAME = "players"
ENEMY_GROUP_NAME = "enemies"


class ModelFacade:
    """
    Encapsulates information of the game state like the characters and groups of characters that exist.
    Also manages loading and writing data to the repository.
    """
    def __init__(self):
        # TODO replace with load from game state in database.
        self.characters = dict()
        self.groups = dict()
        self.groups[PLAYER_GROUP_NAME] = PLAYER_GROUP_NAME

    def get_character(self, name: str) -> Character:
        """
        Gets a character with a given name from the entire pool of characters in the game state.
        :param name: Name of character # TODO define valid name
        :return: character
        """
        return self.characters[name] if self.characters[name] else None

    def get_group(self, name: str) -> list:
        """
        Gets a group of characters from the game-state. Can be native (players or enemies) or can be a user-defined
        group like DragonDenEnemies which the DM could define ahead of time and load quickly into Enemies group.
        :param name:
        :return:
        """
        # TODO Create group-type. Possibly using composite design pattern. Could also use a straight list, but group
        #  could has properties like is_native to avoid deletion and I imagine more things will come up.

    def load_from_db(self):
        """
        Loads data from the database into the facade.
        """
        # Placeholder data until database is greated
        self.characters["Alice"] = Player("Alice", Class("Artificer", 8, 1))
        self.characters["Bob"] = Player("Bob", Class("Bard", 8, 1))
        self.characters["Charles"] = Player("Charles", Class("Cleric", 8, 1))

        # TODO replace with Group types when created
        self.groups[PLAYER_GROUP_NAME] = None
        self.groups[ENEMY_GROUP_NAME] = None

    def update_to_db(self):
        """
        Loads data of the facade into the database.
        :return:
        """
        pass


if __name__ == '__main__':
    model = ModelFacade()
    model.load_from_db()
    for name, ch in model.characters.items():
        print(name, ch)
