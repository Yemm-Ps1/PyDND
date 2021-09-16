
class AbilityEntity:
    """
    Relates to ability scores (1 when constructed) and saving throws (not proficient when constructed)
    """
    pass


class SkillEntity:
    """
    Relates to proficiency and expertise in skills (not proficient when constructed).
    """
    pass


class LeveledEntity:
    """
    Relates to levels in what classes (no levels when constructed).
    """
    pass


class Character(AbilityEntity, SkillEntity):
    """
    Defines meta data (names, description etc) and inherits Ability and Skill properties.
    """
    def __init__(self, name):
        AbilityEntity.__init__(self)
        SkillEntity.__init__(self)
        self.name = name


class Player(Character, LeveledEntity):
    """
    Extends the Character class to allow player specific things e.g. leveling.
    Also derives new things which combine the elements of the parent class
    For example, finding the Roll for a particular skill, this uses:
        ability scores (AbilityEntity),
        skill proficiency or expertise (SkillEntity) and
        Proficiency Bonus (LevelEntity)
    So we can now combine these things to calculate the roll in this class.
    """
    def __init__(self, name):
        Character.__init__(self, name)
        LeveledEntity.__init__(self)


class CharacterBuilder:
    def __init__(self, name):
        self.to_build = Character(name) # Only name is required to initially construct character.

    def add_ability_scores(self, *scores):
        # sets the ability scores for each of the abilities
        return self

    def add_saving_throw_proficiencies(self, *saving_throws):
        # sets the ability scores for each of the abilities
        return self

    def add_skill_proficiencies(self, *skill_proficiencies):
        # sets the ability scores for each of the abilities
        return self

    def build(self):
        return self.to_build


class PlayerBuilder(CharacterBuilder):
    def __init__(self, name):
        # No need to init parent ()since we only need the methods
        self.to_build = Player(name)

    def add_levels(self, *levels_in_classes):
        # Adds levels in each class
        return self


if __name__ == '__main__':
    character_builder = CharacterBuilder("Alice")
    # Just writing none so I don't have to write arguments
    character = character_builder.add_ability_scores(None).add_skill_proficiencies(None).add_skill_proficiencies(None).build()

    player_builder = PlayerBuilder("Bob").add_ability_scores(None).add_skill_proficiencies(None).add_skill_proficiencies(None)
    player = player_builder.add_levels(None)