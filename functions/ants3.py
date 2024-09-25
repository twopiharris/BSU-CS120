""" ants3.py
    classic counting song
    further improvement with a list
"""


def getChorus():
    """ returns the chorus """
    output = """
    ...and they all go marching
    down-
    to the ground-
    to get out-
    of the rain.
    Boom boom boom boom boom boom boom
    """
    return output

def getVerse(distraction, verseNum):
    """ returns the verse, this time via a lookup of the distraction tuple """

    problem = distraction[verseNum]

    output = f"""
    The ants go marching {verseNum} by {verseNum} hurrah, hurrah.
    The ants go marching {verseNum} by {verseNum} hurrah, hurrah.
    The ants go marching {verseNum} by {verseNum}.
    The little one stops to {problem}
    """

    return output

def main():
    """ sets up distraction tuple, prints song by calling other methods """

    distraction = (
      "",
      "suck his thumb",
      "tie his shoe",
      "climb a tree",
      "shut the door"
      )

    for verseNum in range(1, len(distraction)):
        print(getVerse(distraction, verseNum))
        print(getChorus())

main()