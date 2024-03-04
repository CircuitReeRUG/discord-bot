from random import choice
from discord import CustomActivity

# DO NOT SCROLL HERE. YES I PUT ALL OF THE STATUSES IN A LIST. 
quotes = [
    ("Building infrastructure with AC/DCee", "🏗️"),
    ("Jumping into action with ActiviTee", "🏃"),
    ("Counting the bag with AudiCee", "💼"),
    ("Steering the ship with the Board of Advisors", "🚢"),
    ("Shorting wires with CircuitRee", "🔌"),
    ("Connecting with ComExA", "🔗"),
    ("Voicing concerns with the Complaints Committee", "🗣️"),
    ("Overflowing with insights with DataDump", "💾"),
    ("Making artricles with DisCover", "🖋️"),
    ("Unlocking achievements with DLCee", "🔓"),
    ("Travelling with ExCee", "✈️"),
    ("Coding with FCG", "💻"),
    ("Being safe with HEROcee", "🛡️"),
    ("Enlightening minds with IlluminaTee", "💡"),
    ("Making grand entrances with IntroCee", "🚪"),
    ("Taking pics with PhotoCee", "📸"),
    ("Spreading the word with PropaganDee", "📢"),
    ("Organizing spaces with RoomCee", "🏠"),
    ("Getting medals with SporTee", "🏅"),
    ("Acquiring knowledge with StudCee", "📚"),
    ("Livin' green with SustainabiliTee", "🌿"),
    ("Conversing with SympoCee", "💬"),
    ("Crafting memories with YearbookCee", "📖")
]


def random_liner() -> CustomActivity:
    quote = choice(quotes)
    return CustomActivity(name=quote[0], emoji=quote[1]) 