from dataclasses import dataclass
from Options import DefaultOnToggle, Toggle, Range, Choice, PerGameCommonOptions, OptionList


class EndGoal(Choice):
    """
    Determine the goal for the seed

    Defeat Voldemort: Collect the 7 Horcruxes and defeat Voldemort in The Flaw in the Plan
    House Champion: Receive enough House Crests to Complete X number of Hogwarts Crests
    Levels Beaten: Beat X number of levels to win
    """
    display_name = "Goal"
    option_defeat_voldemort = 0
    option_house_champion = 1
    option_levels_beaten = 2
    default = 0


class NumHorcruxesRequired(Range):
    """
    Determine the required number of Horcruxes to beat the game.
    """
    display_name = "Number of Horcruxes"
    range_start = 1
    range_end = 7
    default = 4


class NumHouseCrestsRequired(Range):
    """
    Determine the required number of Hogwarts Crests to beat the game.
    Please note that 1 Hogwarts Crest is all 4 House Crests in the same level.
    """
    display_name = "Number of House Crests Required"
    range_start = 1
    range_end = 24
    default = 12


class NumLevelsRequired(Range):
    """
    Determine the required number of Levels Required to beat the game.
    """
    display_name = "Number of Levels Required"
    range_start = 1
    range_end = 24
    default = 12


class NumStartSpells(Range):
    """
    Determine the number of starting spells (excludes joke spells).
    """
    display_name = "Number of Starting Spells"
    range_start = 0
    range_end = 14
    default = 0


class NumStartLevels(Range):
    """
    Determine the number of starting levels.
    """
    display_name = "Number of Starting Levels"
    range_start = 0
    range_end = 24
    default = 0


class StartingLevelOptions(OptionList):
    """
    Determines which levels you start with.

    Valid Keys:
    "Dark Times"
    "Dumbledore's Army"
    "Focus!"
    "Kreacher Discomforts"
    "A Giant Virtuoso"
    "A Veiled Threat"
    "Out of Retirement"
    "Just Desserts"
    "A Not So Merry Christmas"
    "Love Hurts"
    "Felix Felicis"
    "The Horcrux and the Hand"
    "The Seven Harry's"
    "Magic is Might"
    "In Grave Danger"
    "Sword and Locket"
    "Lovegood's Lunacy"
    "DOBBY!"
    "The Thief's Downfall"
    "Back to School"
    "Burning Bridges"
    "Fiendfyre Frenzy"
    "Snape's Tears"
    "The Flaw in the Plan"
    """

    display_name = "Starting Level Options"

    valid_keys = {
        "Dark Times",
        "Dumbledore's Army",
        "Focus!",
        "Kreacher Discomforts",
        "A Giant Virtuoso",
        "A Veiled Threat",
        "Out of Retirement",
        "Just Desserts",
        "A Not So Merry Christmas",
        "Love Hurts",
        "Felix Felicis",
        "The Horcrux and the Hand",
        "The Seven Harrys",
        "Magic is Might",
        "In Grave Danger",
        "Sword and Locket",
        "Lovegood's Lunacy",
        "DOBBY!",
        "The Thief's Downfall",
        "Back to School",
        "Burning Bridges",
        "Fiendfyre Frenzy",
        "Snape's Tears",
        "The Flaw in the Plan",
    }

    default = [
        "Dark Times",
        "Dumbledore's Army",
        "Focus!",
        "Kreacher Discomforts",
        "A Giant Virtuoso",
        "A Veiled Threat",
        "Out of Retirement",
        "Just Desserts",
        "A Not So Merry Christmas",
        "Love Hurts",
        "Felix Felicis",
        "The Horcrux and the Hand",
        "The Seven Harrys",
        "Magic is Might",
        "In Grave Danger",
        "Sword and Locket",
        "Lovegood's Lunacy",
        "DOBBY!",
        "The Thief's Downfall",
        "Back to School",
        "Burning Bridges",
        "Fiendfyre Frenzy",
        "Snape's Tears",
        "The Flaw in the Plan",
    ]


class DisabledLevels(OptionList):
    """
    Determines which levels won't have any checks.
    Each level disabled removes 3 purple studs from the pool (6 in the case of The Seven Harrys).
    If there are no purple studs remaining, Gold bricks will then be removed.

    Valid Keys:
    "Dark Times"
    "Dumbledore's Army"
    "Focus!"
    "Kreacher Discomforts"
    "A Giant Virtuoso"
    "A Veiled Threat"
    "Out of Retirement"
    "Just Desserts"
    "A Not So Merry Christmas"
    "Love Hurts"
    "Felix Felicis"
    "The Horcrux and the Hand"
    "The Seven Harry's"
    "Magic is Might"
    "In Grave Danger"
    "Sword and Locket"
    "Lovegood's Lunacy"
    "DOBBY!"
    "The Thief's Downfall"
    "Back to School"
    "Burning Bridges"
    "Fiendfyre Frenzy"
    "Snape's Tears"
    "The Flaw in the Plan"
    """

    display_name = "Disabled Levels"

    valid_keys = {
        "Dark Times",
        "Dumbledore's Army",
        "Focus!",
        "Kreacher Discomforts",
        "A Giant Virtuoso",
        "A Veiled Threat",
        "Out of Retirement",
        "Just Desserts",
        "A Not So Merry Christmas",
        "Love Hurts",
        "Felix Felicis",
        "The Horcrux and the Hand",
        "The Seven Harrys",
        "Magic is Might",
        "In Grave Danger",
        "Sword and Locket",
        "Lovegood's Lunacy",
        "DOBBY!",
        "The Thief's Downfall",
        "Back to School",
        "Burning Bridges",
        "Fiendfyre Frenzy",
        "Snape's Tears",
        "The Flaw in the Plan",
    }

    default = []


class ShuffleCharacterTokens(Choice):
    """
    Determines how Character Tokens are shuffled in the Multiworld.

    Tokens & Purchases means the tokens collected and purchases and unlocks are items and location (2 separate items & 2 separate locations).
    Tokens only means that tokens collected are locations and extras unlocks are items (1 item & 1 location).
    Purchases only means that purchases are locations and extras unlocks are items (1 item & 1 location). In this setting you, you have to collect the token before you can purchase it.

    Please note that Purchases only and Disabled Levels are incompatible settings
    """
    display_name = "Character Token Shuffle"
    option_tokens_and_purchases = 0
    option_tokens_only = 1
    option_purchases_only = 2
    default = 0


class ShuffleRedBricks(Choice):
    """
    Determines how Red Bricks are shuffled in the Multiworld.

    Bricks & Purchases means the red bricks collected in the hub and purchases and unlocks are items and location (2 separate items & 2 separate locations).
    Bricks only means that red bricks collected in the hub are locations and extras unlocks are items (1 item & 1 location).
    Purchases only means that purchases are locations and extras unlocks are items (1 item & 1 location). In this setting you, you have to collect the red brick in the hub before you can purchase it.
    """
    display_name = "Red Brick Shuffle"
    option_bricks_and_purchases = 0
    option_bricks_only = 1
    option_purchases_only = 2
    default = 0


class ShuffleJokeSpells(DefaultOnToggle):
    """
    Turning this on makes it so Joke Shop purchases are shuffled
    """
    display_name = "Shuffle Joke Shop Purchases"


class ShuffleGoldBrickPurchases(DefaultOnToggle):
    """
    Turning this on makes it so Gold Brick purchases are shuffled
    Removes Purples studs from the pool first and then removes Gold Bricks
    """
    display_name = "Shuffle Gold Brick Purchases"


class CheaperShops(Range):
    """
    Determines how many times cheaper purchases are from vanilla game.
    1 is no change and 10 is 10x cheaper.
    This is taken into account for stud multiplier logic
    """
    display_name = "Cheaper Shop Purchases"
    range_start = 1
    range_end = 10
    default = 5


class RemoveFillerCharacters(Toggle):
    """
    This option removes any character that isn't considered progression from the pool.
    """
    display_name = "Remove Filler Characters"


class RemoveExtraProgressionChars(Toggle):
    """
    This option makes it so there is only 1 character with each ability in the pool
    Characters who have overlap with the starting trio or red bricks (dig/strength) are removed
    Dark Magic, Ravenclaw, Arthur, and Key Characters will only have 1
    Please note that DLC Characters will not be your selected characters so the seed will always be beatable on standalone
    """
    display_name = "Remove Extra Progression Characters"


class HardPurchases(Toggle):
    """
    Turning this on makes it so purchases no longer require a stud multiplier.
    """
    display_name = "Hard Purchases"


class LowMultiplierPriceMinimum(Range):
    """
    Determines the starting price for a low multiplier.
    A low multiplier is defined as any multiplier.
    """
    display_name = "Low Multiplier Price Minimum"
    range_start = 10
    range_end = 10000000
    default = 50000


class HighMultiplierPriceMinimum(Range):
    """
    Determines the starting price for a high multiplier.
    Must be larger than Low Multiplier Price.
    A high multiplier is defined as Score x6, Score x8, Score x10 or both Score x2 and Score x4.
    """
    display_name = "High Multiplier Price Minimum"
    range_start = 10
    range_end = 10000000
    default = 100000


class StartingDetectors(DefaultOnToggle):
    """
    Determines if the player starts with Character Token, Red Brick, Hogwarts Crest, & Gold Brick Detectors.
    """
    display_name = "Start With Detectors"


class StartingFastMagic(DefaultOnToggle):
    """
    Determines if the player starts with Fast Magic & Dig.
    """
    display_name = "Start With Fast Magic & Dig"


class FasterDuels(DefaultOnToggle):
    """
    Turning this on means that all enemies and players only have 1 HP in duels
    """
    display_name = "Faster Duels"


class TrapPercentage(Range):
    """
    Determines what percentage of filler items are traps.
    Traps are effects on the player, Stupefy, Immobulus, Slugulus Eructo, Incarcerous
    Note: If you have no filler items, there will be no traps.
    """
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class GameVersion(Choice):
    """
    The version of the game you play this seed on.

    Legacy: the original LEGO Harry Potter: Years 5-7 (Steam / GOG).
    Collection: LEGO Harry Potter Collection. Adds its 10 extra characters sold at Madam Malkin's as items and
    purchase locations (not with Character Token Shuffle set to Tokens only).

    On the Legacy game, a Collection seed still works: the DLC purchases are sent automatically.
    """
    display_name = "Game Version"
    option_legacy = 0
    option_collection = 1
    default = 0


@dataclass
class LHP2Options(PerGameCommonOptions):
    EndGoal: EndGoal
    NumHorcruxRequired: NumHorcruxesRequired
    NumHouseCrestsRequired: NumHouseCrestsRequired
    NumLevelsRequired: NumLevelsRequired
    NumStartSpells: NumStartSpells
    NumStartLevels: NumStartLevels
    StartingLevelOptions: StartingLevelOptions
    DisabledLevels: DisabledLevels
    ShuffleCharacterTokens: ShuffleCharacterTokens
    ShuffleRedBricks: ShuffleRedBricks
    ShuffleJokeSpells: ShuffleJokeSpells
    ShuffleGoldBrickPurchases: ShuffleGoldBrickPurchases
    CheaperShops: CheaperShops
    RemoveFillerCharacters: RemoveFillerCharacters
    RemoveExtraProgressionChars: RemoveExtraProgressionChars
    HardPurchases: HardPurchases
    LowMultiplierPriceMinimum: LowMultiplierPriceMinimum
    HighMultiplierPriceMinimum: HighMultiplierPriceMinimum
    StartingDetectors: StartingDetectors
    StartingFastMagic: StartingFastMagic
    FasterDuels: FasterDuels
    TrapPercentage: TrapPercentage
    GameVersion: GameVersion
