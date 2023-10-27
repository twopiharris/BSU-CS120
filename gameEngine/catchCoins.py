import pygame, simpleGE, moveCharlieC, coinFall

""" catchCoins.py """

def main():
    
    scene = simpleGE.Scene()
    charlie = moveCharlieC.Charlie(scene)
    coin = coinFall.Coin(scene)
    scene.sprites = (charlie, coin)
    
    scene.start()
    
if __name__ == "__main__":
    main()
