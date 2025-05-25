default astra_points = 0
define receptionist = Character("Receptionist")

label astra_quest:

    "You can’t help but notice the start of the quests’ shenanigans as the receptionist glances at the document and back at you."
    receptionist "\"Thank you, for accepting this… quest.\" She states with some bemusement as she too flips the page around a few times. Seemingly puzzled at how something this unprofessional could’ve ended up on the quest board."
    "Some rather frantic and frustrated flipping through records ensues, but somehow the receptionist does come back with an item to send along on your quest. Placing it on the counter and looking expectant at you to know what it is."
    "A fist-sized red ball sits lightly on the counter. From one end, a single large and very worn yellow feather is attached with twine."
    menu:
        "Take the item to save face.":
            pass
        "What is this supposed to be?":
            receptionist "I’m afraid I couldn’t tell you. I’m actually quite surprised to see anything associated with this quest."
            receptionist "From how poor- *ahem* From how the paperwork looks, it had seemed to be something placed without our knowledge, but from the looks of it someone working here did speak to the poster and seems to have not filled out the necessary documentation."
    receptionist "I’m so sorry we don’t have more information, but from the looks of it you have things well in hand. Thank you again for accepting this most desperate quest, and I wish you the best in its resolution."
    "She gives you a slight bow as you depart the counter."    
    "Your attention returns to the drawn map and now with the ratted feather for comparison you can almost make out the doodled birds as chocobos."
    p "Dravanian Forelands?"
    "You ponder the idea. The volcano really should have been a dead giveaway, but the longer you decipher the scratches of color the more the geography lines up."
    p "Well then. Off to Tailfeather."

    scene tailfeather

    "Nothing seems to be immediately out of the ordinary."
    "You ask a few nearby hunters if anything has been amiss and show them the note."
    "The hunters debate a bit and say nothing’s been overly out of the ordinary. Not since peace was brokered with the dragons at least."
    "It might be best to talk to the dragons themselves"

    scene anyx

    "According to the dragons, the only notable event has been a suspicious lack of chocobos in the area, and a very unusual figure that's been seen among them."

    scene river

    "You go to investigae the last known sighting of this figure."
    "At the river, you instead find a flock of red chocobo!"
    "Upon seeing you, they let out a mighty 'KWEH' and attack!"

    am "Would you mind taking that somewhere else?"

    "You have no time to identify the stranger as you are forced to defend yourself."

    am "If you don't they'll start dropping meteors."

    "Your vision is obscured by masses of crimson feathers, but the voice sounds closer."

    am "*sigh*"
    am "Guess I have to do everything myself."

    "A basket sails over your head and lands an impressive distance away, followed soon by the flock"
    "Freed from the onslaught, you turn and face the stranger."

    #Do chocobos eat fish?
    #also will need a head shaded astra
    show astra concept upset
    am "What were you thinking!?"
    am "Thanks to all the ruckus you caused, the fish are all scared off!"
    am "What do you have to say for yourself!?"

    menu:
        "Um, I'm sorry?":
            $ astra_points += 1
            am "Yeah, you better be sorry."
        "Wait, who are you?":
            show astra concept speaking
            am "A humble fishmonger and chocobo wrangler."
            show astra concept upset
            am "But that doesn't change what you did!"
    #unclear sequence of events? shouldn't the chocobos be running in a linear line
    "Before the conversation can go much further, the chocobos 'KWEH' in trumph."
    "You turn back around and notice that the basket had been rigged with an oversized fishing hook attached to a line of string."
    "It also appears the basket has been broken up, as fish lay scattered all around it to the delight of the chocobos who busy themselves pecking at their spoils."
    #need astra panic
    show astra concept upset
    am "My fish!!!"
    hide astra
    "The stranger dons an even stranger helm, and charges into the herd."
    "Alas, it is too late, and moments later the chocobos have scattered with their ill-gotten gains."
    "Her shoulders slumped, the stranger returns in visible defeat."

    show astra concept chicken
    am "Now I'm going to starve..."
    am "You, this is your fault, why'd you show up!?"
    am "Saving you better have been worth this loss, those fish took me all morning to hunt down."
    am "You owe me a life debt."

    menu:
        "You're crazy, and seriously, who are you?":
            $ astra_points -= 1
            am "I… am a fisher. There are some here in the Forelands who call me… 'Astra'"
        "I didn't mean to cause any trouble.":
            $ astra_points += 1
            am "Didn’t anyone tell you this place is dangerous. Yada yada here be dragons."
            am "Anyways, my name is Astra"
        "(Astra write me a dramatic response)":
            am "I feel like I’ve made a terrible mistake."
            am "-figure out how WOL learns her name.-"
    
    show astra concept speaking
    a "So what brings you to my sacred fishing…hole, …river, ….spot? Ehhh, not that sacred actually.. Anyway yeah what brings an adventurer like you out to a place like this? What’s your name?"
    p "I'm [povname]"
    show astra concept confused
    a "Wait, you're [povname] the stealer of pants!?"
    "Astra flails her fishing rod at you."
    a "I'm watching you!"
    p "It was only one, no… two times at best?"
    show astra concept upset
    a "Either way that’s one time two many and you ain’t gunna catch me off guard, I’ve got a whole suit to go with this here chicken head if I need to break out the big guns." 
    p "I’m not going to try to steal your pants. I’m here because I am answering a quest, I’ve got this…"
    "You realize your quest paper is now gone. Did the chocobos take it?"
    p "Well I had an urgent request, but it didn’t have any location or name to it. I’ve been trying to track down who could have posted it."
    show astra concept speaking
    a "It said death imminent? Wow that sounds pretty important. So where do we start?"
    p "What do you mean? You don't need to join me, and besides you don't seem to have any weapons to defend yourself with. Are you capable of any combat?"
    show astra concept confused
    a "Not at all. I’ve got this rod, a knife for skinning, and these bombs."
    p "Bombs… BOMBS. Why do you have bombs?"
    a "Yeah these ones, I use them as backup to fishing, sometimes…"
    show astra concept neutral
    p "Bombs shouldn’t be used for… you know what… never mind. Just don’t blow me up." 

    "(End of current Astra Quest draft)"

    jump job_board