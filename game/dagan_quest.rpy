default dagan_points = 0
label dagan_quest:

    scene coffer and coffin
    "The Thanalan sun beams down against you as you make your way into the bar, the smell of dried wood and alcohol filling your senses as you swing the door open and step inside."
    "Coffer and Coffin has not changed, you see most of the same folk there, drinking cold mugs of alcohol to stave off the desert heat. You look to the bar and see someone that stands out though."

    show dagan stand neutral with dissolve

    "A very tall Xaela man sits at the mostly empty bar. He appears to be studying a map, scrawled with markings you can’t make out, his other hand holds a cup that he sips from occasionally. He does not seem to pay you any mind as you walk up and sit yourself beside him."
    
    #suggestion: use more descriptive but short menu option rather than entire quote?
    menu:
        "Hello, I'm [povname]. I heard about your request?":
            "Well, you might as well introduce yourself, you’ve done this song and dance countless times."
            p "Hello, I'm [povname]. I heard about your request?"
            "The man looks at you calmly, his eyes examining you. There is no recognition on his face at your name. But he leans forward, a bit close as he speaks."
            dm "Hm? So you did."
            show dagan bent smug
            "He seems to have finished scanning you, a smile on his face as speaks."
            dm "And you do look strong. Capable enough to look after yourself, yeah?"
            "You smile, a little amused that this man does not know about you or your escapades. It has been a while since that has been the case. It’s a little refreshing and you savor the anonymity for now."
            p "Player: You could say that. I’ve been doing this for a while."
        "I heard you were looking for someone strong? I hope I’m up to your standard.":
            $ dagan_points += 1
            "You lean against the bar, ordering yourself a drink with the bartender. Once you do, you look up to the distracted man and smile."
            p "I heard you were looking for someone strong? I hope I’m up to standard."
            "The man turns away from his map to look at you. He tilts his head, staring at you a bit intensely, before he seems to smile."
            show dagan bent smug
            dm "Hm, yes. I think you are."
            "He leans forward, a bit closer than strangers typically get with you. He is tall, even for an au'ra."
            "His sharp teeth show as watches you, there is an excited look to his gaze, and you wonder if he actually recognizes you as the Warrior of Light for a second. But then he speaks."
            dm "You have the aura of a great beast. I’m sure you’ve felled many before."
            p "Hah. Perhaps. Maybe a couple. Though I don’t know about having an aura per say… Do I seem like a beast to you?"
            show dagan bent smile
            "The man shakes his head, he pauses as if to reconsider his words."
            dm "I mean it as a compliment. I mean that you seem capable. What do I call you?"
            "You laugh a bit, but he does not look offended. He seems a little strange, but you’ve known plenty of strange people, not to mention being a little odd yourself. Still, the way he navigates conversation makes you wonder how often he interacts with others like this."
            p "I’m [povname]. And you?"
        "Are you the man that came into the Rising Stone and insulted those adventurer’s skills?":
            $ dagan_points -= 1
            "The man does not flinch at your words. He turns to look at you and tilts his head. His eyes seem confused by your statement."
            dm "Insult? I simply did not find who I was looking for."
            p "And who would that be?"
            dm "Someone strong."
            show dagan bent smug
            dm "Someone like you, from the looks of it."
            "You frown, continuing to match his gaze. This xaela was pretty nonchalant about it, but he still hurt some of those adventurers' feelings. You shake your head, telling yourself to keep a level head."
            p "What’s your name?"
            show dagan bent neutral
            "He doesn’t answer, lifting his hand and gesturing at you."
            dm "You first."
            "You grit your teeth, but then your rational side tells you to let your irritation go. You sigh."
            p "I'm [povname]."
            dm "Well, [povname]. I meant no offense. I did not think I insulted anyone. I’m just looking for someone strong."
            "He seems sincere now, his eyes appearing confused that he has upset you."
            p "And who might you be?"
    show dagan bent neutral
    "The xaela takes another sip of his drink, relaxing a little as he leans away from you."
    d "Dagan Dotharl."
    p "…Wait, Dotharl? Like, from the Steppe?"
    "He nods, his expression hard to read. You remember the Dotharl of the Steppe. Fearsome as enemies and allies, a tribe that values martial prowess at all cost."
    "A tribe that also does not fear death."
    "His forward way of speaking, and his enthusiasm for strength are starting to make sense now…"
    "Dagan studies your face, as if trying to see if he recognizes you. You do not recognize him, despite having visited the Dotharl before in your travels."
    d "Dagan: You know of our tribe."
    p "A little. I met them when I visited the Steppe a few years back."
    "Has he been away from the Steppe? You remember the close knit community you interacted with"
    show dagan bent smug
    d "And they did not kill you. Impressive."
    "You decide not to explain that you are the current khagan. That would open more questions than you would like to answer right now."
    p "I mean, they tried. But we came to an understanding."
    "He chuckles at this, going to take a drink."
    d "Hm, you are unusual then. Most outsiders would steer clear of us, once they know what we are."
    "You notice he is not wearing the traditional garb of the dotharl either. He is wearing a black, worn cape. The dotharl are known to welcome death, so it makes sense that he is not wearing a lot of heavy armor."
    "His large sword is leaned against the bar, and you recognize it as a sword carried by a Dark Knight. He seems a lot more well traveled than the Dotharl you have met."
    menu:
        "Ask him why he isn’t with the tribe?":
            p "You know… I’ve gotten to know the Dotharl, but I don’t remember meeting you, though."
            p "What’s a Dotharl doing hunting so far from home?"
            show dagan stand neutral
            "Dagan leans back, a quiet somber look on his face. You wonder if you overstepped by asking him that. Before you can say anything, he shrugs, a nonchalant look now on his face."
            d "I left the Steppe a while ago."
            "He doesn’t say anything else. You can tell he doesn’t feel like talking about it at the moment. Perhaps it’s better to drop it for now."
        "Update him on the Dotharl tribe.":
            "This choice does not have lines yet."
            "Please look forward to them soon."

    p "So, you needed someone strong. I’m assuming you’re hunting something big?"
    "He nods, leaning to get closer to you as he pushes the map towards you. His largeness makes him feel closer than he is, and his glowing pink eyes watch you as you scan the map."
    "You try your best to ignore how close he is while you look at the areas he has circled and marked off."

    "(End of current Dagan Quest draft)"

    jump job_board






