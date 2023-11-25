# Treasure Island
print("""
                                                     o         _ _ _ _ _
                                                _----|         I-I-I-I-I
                             _ _ _ _ _ _      o  ----|     o   \~~`~'~~/
                             ]-I-I-I-I-[ _----|      |_----|    |.    |
                             \~`\~~~/'~/  ----|     / \----|    |  /^\|
                              [*] ' __|       ^    / ^ \   ^    |_ |*||
                              |__    ,|      / \  /    `\ / \   |  ===|
                            __|  ___ ,|__   /    /=_=_=_=\   \  |,  __|
                            I_I__I_I__I_I  (====(_________)___|_|_____|___
                            \-\--|-|--/-/  |'    I~~[ ]~~I I_I__|IIII|_I_l
                             | [ ]    '|   | [~] |_`_~_ _[  \-\--|-|--/-/
                             |.   | |' |___|____`I_I_|_I_I___|---------|
                            / \| [] ~ .|_|-|_|-|-|_|-|_|-|_|-| []   [] |
                           <===>  |  ~.|-=-=-=-=-=-=-=-=-=-=-|~  |  ~ / \|
                           | []|`   []~||.|.|.|.|.|.|.|.|.|.||-~   ~ <===>
   O O      o o            | []| ` |   |/////////I\\\\\\\\\\||__. ~| |[*]I
  O * O    o * o           <===> ~   ' ||||| |   |   | ||||.||  []  ~<===>
   O O      o o             \T/  |~|-- ||||| | O | O | ||||.|| . |'~  \T/
   \I        I/              |     ~.~_||||| |~~~|~~~| ||||.|| | ~   | |
____I/______\I____\/..___.../|' v . | .|||||/____|____\|||| /|. . | . .|\.\/_
""")
print("Welcone to Treasure Island.")
print("Your mission is to find the treasure.")
print(f"You're at cross road. Where do you want to go? Type {'"left"'} or {'"right"'}")
direction = input().lower()
print(direction)
if direction == "left":
    print("You're at a crossroad, where do you want to go? Type \"left\" or \"right\".")    
    direction = input().lower()
    if direction == "wait":
        print("You arrive to the island inharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        direction = input().lower()
        if direction == "yellow":
            print("You found the treasure! You win!")
        elif direction == "red":
            print("Burned by fire.\nGame Over.")
        elif direction == "blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")




