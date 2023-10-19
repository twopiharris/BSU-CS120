""" ants1.py
    classic counting song
    demonstrates use of multi-line strings
    first version
    """


def printChorus():
    """ prints chorus """
    print("""
    ...and they all go marching
    down-
    to the ground-
    to get out-
    of the rain.
    Boom boom boom boom boom boom boom boom
    """)

def printVerse1():
    """ prints first verse """
    print("""
    The ants go marching 1 by 1 hurrah, hurrah!
    The ants go marching 1 by 1 hurrah, hurrah!
    The ants go marching 1 by 1,
    The little one stops to suck his thumb
    """)

def printVerse2():
    """ prints second verse """

    print("""
    The ants go marching 2 by 2 hurrah, hurrah!
    The ants go marching 2 by 2 hurrah, hurrah!
    The ants go marching 2 by 2,
    The little one stops to tie his shoe
    """)

def main():
    printVerse1()
    printChorus()
    printVerse2()
    printChorus()

main()