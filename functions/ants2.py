#!/usr/bin/python3.8

""" ants2.py
    classic counting song
    use parameters and return statements
    """

def getChorus():
    """ creates and returns the chorus """
    output = """
    ...and they all go marching
    down-
    to the ground-
    to get out-
    of the rain.
    Boom boom boom boom boom boom boom
    """
    return output



def getVerse(verseNum):
    """ creates a verse based on verseNum """

    if verseNum == 1:
        distraction = "suck his thumb"
    elif verseNum == 2:
        distraction = "tie his shoe"
    else:
        distraction = "I have no idea"


    output = f"""
    The ants go marching {verseNum} by {verseNum} hurrah, hurrah.
    The ants go marching {verseNum} by {verseNum} hurrah, hurrah.
    The ants go marching {verseNum} by {verseNum}.
    The little one stops to {distraction}
    """

    return output

def main():
    """ the road map """
    print (getVerse(1))
    print (getChorus())
    print (getVerse(2))
    print (getChorus())

main()

