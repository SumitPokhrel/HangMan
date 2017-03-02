def getRandomWord():
    import random
    words = ("""stack trump summit rhythm zephyr jazz bernie hilary vagina python annual iran iraq syria vulva agenda soccer jesus shiva macbook
            llama mole monkey moose mouse mule newt buzz fizz fuzz otter owl panda bear deer cobra badger tiger rhino catfish goat hen
            depth curve dance dozen drama boost broke fault filfth fifth herpes force newton glass grace grade guide guest 
            minor trade tirade accused aids arrive rim bishop became coffee ethnic expert format gender injury guilty invest
            killed labour launch space spacex orbit texas merger moment proven random secure seller senior tenant unable valley 
         """.split())
    chosenWord = random.choice(words) #Choose a random element
    return chosenWord

