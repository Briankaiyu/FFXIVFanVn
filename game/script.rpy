# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default povname ="John Final Fantasy"
define config.menu_include_disabled = True
define p = Character("[povname]")
python:
    povname = renpy.input("What is your name?")
    povname = povname.strip()

    if not povname:
        povname = "John Final Fantasy"

pov "My name is [povname]!"
define implemented = False

define bartender = Character("Bartender")

define am = Character("???",color="#621A13")

define a = Character("Astra", color="#621A13")
default astra_denial=0
image astra concept neutral = "Astra/Astra Concept Neutral.png"
image astra concept confused = "Astra/Astra Concept Confused.png"
image astra concept speaking = "Astra/Astra Concept Speaking.png"
image astra concept upset = "Astra/Astra Concept Upset.png"
image astra concept chicken = "Astra/Astra Concept Chicken.png"
image astra chicken = "Astra/Astra_Chicken.png"
image astra chicken angry = "Astra/Astra_Chicken_Angry.png"
image astra chicken sad = "Astra/Astra_Chicken_Sad.png"
image astra chicken surprise = "Astra/Astra_Chicken_Surprise.png"
image astra cri = "Astra/Astra_Cri.png"
image astra grin = "Astra/Astra_Grin.png"
image astra perplex = "Astra/Astra_Perplex.png"
image astra pout = "Astra/Astra_Pout.png"
image astra smile = "Astra/Astra_Smile.png"

define dm = Character("???",color="#2E381A")
define d = Character("Dagan", color="#2E381A", image="dagan")
image dagan bent angry= "Dagan/Dagan_Bent_Angry.png"
image dagan bent confused = "Dagan/Dagan_Bent_Confused.png"
image dagan bent laugh = "Dagan/Dagan_Bent_Laugh.png"
image dagan bent neutral = "Dagan/Dagan_Bent_Neutral.png"
image dagan bent smile = "Dagan/Dagan_Bent_Smile.png"
image dagan bent smug = "Dagan/Dagan_Bent_Smug.png"
image dagan stand neutral = "Dagan/Dagan_Stand_Neutral.png"

define h = Character("Hawke", color="#FF6600")
image hawke = "Hawke/Hawke Concept Cropped.png"


define s = Character("Saran")
image saran = "Saran/test.png"
image saran embarassed = "Saran/EmbarassedSaran.jpg"
default saran_points = 0

image costa del sol day = "bg/BG Costa Del Sol Day.png"
image uldah day = "bg/BG Uldah Day.png"
image garlemald night = "bg/BG Garlemald Night.png"
image tailfeather = "bg/BG Tailfeather.png"
image anyx = "bg/BG Anyx Trine.png"
image river = "bg/BG River.png"
image coffer and coffin = "bg/BG Coffer and Coffin.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene costa del sol day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "Wow, what a pretty background!"

    "This is definitely what it looks like in that hit award winning game by default, right?"

    "Well, you should go ahead a pick a route."

    "Luckily there's a convenient job board you can look over."

    jump job_board

label job_board:
    
    scene garlemald night
    menu:
        "What quest do you check? (Pretend the background is a job board)"

        "Astra’s Kidnapping":
                "You’ve found yourself staring at the quest board, skimming through the collection of fetch quests and escort missions that nobody ever seems to pick up."
                "How up to date is this board? You wonder as you note a few requests mentioning the Garlean outposts nearby." 
                "Curiosity plucked a parchment from the board, the pin holding it clinking to the ground before rolling down beneath the floorboards followed by the slow descent of another quest landing on your boot."
                "A pound beats in your chest as you easily read the large letters fallen at your feet."
                "Unable to resist, you snatch it up and give it a look over."
                "{size=*1.5}URGENT HELP NEEDED! DEATH IMMINENT{/size}"
                "Several poorly drawn faces with crossed out eyes cover the paper in place of any actual description."
                menu:
                    "Take a closer look.":
                        "While the form itself appears to be a proper quest form, it would seem the writer has included no helpful information. You can’t help but notice they’ve failed to even keep the writing on the lines provided."
                p "Is this a real quest?"        
                menu:
                    "Turn the page over?":
                        pass
                    "Turn the page over.":
                        pass
                "On the back is a doodled map seeming to indicate a red smoking mountain with a bunch of angry red and yellow birds in the sky and at its base. A waterfall and river in… green? Seems to be drawn off to the right."
                "A giant arrow seems to be pointing to a spot on the river, but it is too vague to discern an actual location."
                "You flip the page back, its foreboding words don’t provide a lot to go off of, but then again you’ve taken stranger requests before."
                menu:
                    "Accept the quest":
                        jump astra_quest
                    "Pin it back to the wall":
                        jump job_board
        
        
        "A Great Hunt":
            "Higher up on the job board is a small scrawled note requesting a strong hunter interested in testing their mettle. There also appears to be a crudely drawn beast on the paper with a sword stabbing it."

            "Confused, you take the note to the bartender who seems to recognize it."

            bartender "Yeah, I remember the guy, a Xaela with green scales and a greatsword came in and asked if anyone was good at hunting."

            p "Good at hunting? Was he more specific?"

            bartender "Nope. On top of that, he didn’t seem impressed by anyone who offered, so he left a note on the board."

            bartender "Seemed like a cocky bastard to me - didn't think anyone here was good enough, I guess."

            "The bartender shrugs, going back to cleaning a glass. You do notice a couple of adventurers looking a bit disheartened at their tables, perhaps this encounter wounded their pride."

            "You wonder what kind of hunt this man is on. Surely there were capable adventurers in the room right now? How dangerous was this going to be?"

            "You have handled worse, but you wonder if you are interested in battling monsters at this moment."

            "The location on the note appears to request those interested to meet at the tavern, Coffer & Coffin in South Thanalan. There doesn’t seem to be any monetary information."

            "Seriously? Did this person expect someone to just come without pay? Surely not…?"

            "Will you take this quest?"
            menu:
                "Okay, I’m curious. Let’s see if they have a challenge!":
                    jump dagan_quest
                "Let some other smuck do unpaid labor.":
                    jump job_board
        
        "Hawke: Hehe Hot. Also Pirates":

            show hawke  at left with dissolve

            h "Just like, don't fuck up Becky."

            jump job_board

        "Hang out with the Coolest Paladin (Route Demo)":
            show saran at right
            "Huh, that's odd. This quest notice is to just hang out with someone?"
            
            "It looks like there will just be a simple Q and A game."

            "What a weird request."

            "Do I want to take this quest?"
            menu:
                "Accept the quest":
                    jump saran_route
                "Take a look at the board again":
                    jump job_board
label astra_demo:

    show astra concept speaking

    a "Perfect! Here, hold this."

    "The Miqo'te hands you her fishing rod."

    "She then collects the mascot chicken head, before scurrying behind a rock."

    hide astra with dissolve

    p "Wait, where are you going?"

    "A few moments pass as you receive no answer, before your quest giver emerges from her hiding spot."

    show astra concept chicken with dissolve

    a "{size=*1.5}WHY HELLO THERE MORTAL.{/size}"

    p "What."

    a "{size=*1.5}THANK YOU FOR HEEDING MY SUMMONS.{/size}"

    a "{size=*1.5}I AM ASTRA, FINDER OF FEESH.{/size}"

    p "Do you mean fish?"

    a "{size=*1.5}I SAID WHAT I SAID.{/size}"

    a "{size=*1.5}ANYWAYS, TO YOU BRAVE ADVENTURER FALLS A TASK.{/size}"

    a "{size=*1.5}I REQUIRE AID IN CONQUERING THE LEVIATHAN KNOWN AS THE RUBY DRAGON.{/size}"

    hide astra with dissolve

    show astra concept speaking with dissolve

    a "Anyways, that's where my particular route will pick up, or something along those lines."

    show astra concept confused

    a "I guess Saran didn't want to write too many lines that wouldn't make it in the final cut."

    a "Plus who knows what actual script my real creator will come up with?"

    show astra concept speaking

    a "It'll probably be better than whatever this current bit is!"

    a "And it's about time I got my own screen time too~~"

    show astra concept upset

    a "Stupid Saran...getting all the cute pictures from Kari..."

    a "Lazing about in her office while I do all the actual Free Company work..."

    show astra concept speaking

    a "But, that's neither here nor there!"

    a "For now, this will loop you back to the job board menu, so you can view the expressions again."

    show astra concept chicken
    
    a "See you next time!"

    jump job_board

label saran_route:
    scene costa del sol day

    "Alright, time to do this quest"

    show saran
    # These display lines of dialogue.

    s "Tada!"

    s "Don't think too hard about the fact I'm in a fancy dress."

    s "Really it's all my creator on hand had at the time with a transparent background."

    s "Anyways - let's get this show on the road!"

    s "So in the full version there'll be more fluff. Actual dialogue and a back and forth."

    s "But I'm hardly defined at the moment, let alone you Protagonist, so we're keeping this simple."

    s "A proof of concept to see what this game can do!"

    p "Sounds good to me. Not that I have a choice."

    s "Okay! So the setup here is we're getting to know each other through a simple game of question and answer."

    s "I'll go first!"

    s "You're walking along when you notice the person before you has dropped their wallet."

    s "What do you do?"

    p "..."

    p "...Really? That's your ethical dilemna?"

    s "Hey, I never said this was deep. Just answer the question!"

    menu:
        "What do you do with the dropped wallet?"

        "Return it":
            $ saran_points+=1
            p "I return it of course." 
            s "Good choice!"
        "Just walk away":
            p "I walk away because it's not my problem."
            s "Huh...I guess you could do that."
        "Take the money inside":
            $ saran_points-=1
            p "I take the money."
            s "Wow...you have no shame, huh?"

    if saran_points >= 0:
        s "Alright, time for your question!"
        p "Hm..."
    else:
        s "Well, legally I still have to let you ask a question I suppose."
        p "So enthusiastic..."

    menu:
        "What do you ask?"

        "What do you do for work?":
            p "What do you do for work?"
            s "I-"
            s "..."
            p "..."
            s "...I don't think that's actually been figured out yet."
            p "What."
            s "I think I'm a paladin? Or was it a free company leader? Or a secretary?"
            s "Continuity sure is hard."
            p "I should've picked a different route."
        "What do you like to do for fun?":
            p "What do you like to do for fun?"
            s "Well I love games and contests!"
            s "It's also fun getting to know people and asking lots of questions."
            p "Wow, who could've guessed you enjoy that."
            s "What'd you say?"
            p "Nothing."
        "How do you like to fuck?":
            s "..."
            p "..."
            if saran_points < 0:
                s "I really should have seen this coming letting you ask a question, huh?"
            else:
                s "Wow just...wow. No shame, huh?"
            $ saran_points -=1
            p "Are you going to answer or not?"
            s "We haven't even decided if this is that kind of game yet!"
            p "Lame."  
            s "You're lame."
    s "Anyways, time to wrap this up so my creator can go look up ren'py best practices and other boring stuff."
    p "So how'd I do?"
    s "Let's see..."
    if saran_points >0:
        s "You did great!"
        s "In fact, if this were that kind of game, you'd get a special reward."
        s "Let me show you!"
        jump saran_reward
    if saran_points==0:
        s "You did okay."
        s "Once we're in the full version, I'm sure there'll be more content to explore our neutral relationship."
        s "Full of neutrality and all that."
        jump end
    if saran_points <0:
        s "Yeah...I don't think I like you."
        s "So it's probably best to end it here, even if this is a proof of concept segment."
        s "Maybe...be a more well adjusted person next time?"
        jump end

label saran_reward:
    scene uldah day
    show saran embarassed:
        xalign 0.5
        yalign 0.5
    s "Ahhhh! I can hardly look!"
    s "If this was one of those games this would be quite the spicy scene!"
    s "And even if it wasn't this would be one of those super cute romance CGs!"
    s "Gosh, they even changed the background!"
    
   
    jump end
    

label end:
    scene costa del sol day
    show saran
    s "Anyways, that's all for now!"
    s "I hope to see you again, in a slightly more fleshed out version of this game!"



                
            

    

    # This ends the game.

    return
