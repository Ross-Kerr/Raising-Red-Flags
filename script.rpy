# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define ava = Character("Detective Ava")
define emma = Character("Emma")
define frank = Character("Frank")
define oscar = Character("Oscar")
define unknown = Character("...")
define config.main_menu_music = "audio/everyday_life.ogg"

# The game starts here.

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music
    scene bg gate_day
    with fade
    play music "lets_go.wav"
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Today is your first day at your new job."
    "You've finally managed to become a detective with your local police force and you're excited to see what your first case will be."

    scene bg locker_room_day
    with fade

    "You make your way to your locker, as you reach it you see a note stuck to the door."
    '"Meet me in the research room. Signed your new partner"'
    "Looks like you've already been assigned a partner to work with, better not keep them waiting long."

    scene bg library_day
    with fade

    "You arrive in the research room, there are other staff members working away on their own cases, some are reading up on past cases, others researching for whatever case they are currently on. "
    "You feel someone tap you on the the shoulder"
    unknown '"Hello there"'

    show detective normal
    with dissolve
    ava "I'm Detective Ava, nice to meet you."
    show detective talking
    with dissolve
    ava "I'm your new partner, we'll be working together alot."
    show detective normal
    with dissolve
    ava "I know today is your first day and you probably haven't been given time to settle in but we've already been assigned a case!"
    show detective talking
    with dissolve
    ava "We've been tasked with catching an online romance fraudster! I have to admit I'm not entirely sure what those are, do you?"

    menu:
        "I don't know anything about them.":
            jump no_knowledge
        "I have some knowledge on them.":
            jump some_knowledge

    return

    # These display lines of dialogue.

label no_knowledge:
        show detective sad
        with dissolve
        ava "Well that's okay, I'm sure we will figure this out"
        jump Case_breifing
        return
    
    
label some_knowledge:
        show detective normal
        with dissolve
        ava "Great that will help us out as we go."
        jump Case_breifing
        return

label Case_breifing:

        $ viewed_emma = False
        $ viewed_frank = False
        $ viewed_oscar = False

        show detective normal
        with dissolve
        ava "I was speaking with the boss this morning about the case and we came up with a plan."
        show detective talking
        with dissolve
        ava "We've set up an online dating account for you, don't worry it's not real and doesn't use any real information."
        show detective normal
        with dissolve
        ava "We've already gotten you matched up with three people the problem is we don't know which one is the fraudster!"
        show detective talking
        with dissolve
        ava "So this is where you come in, you are going to pretend to date these people and figure out which one is really the scammer!"
        show detective normal
        with dissolve
        ava "I'll be working behind the scenes gathering information on how these scammers work and letting you know what to look out for."
        show detective talking
        with dissolve
        ava "Once you're certain who the scammer is we can have the cyber folks in the lab track them down and then we can arrest them."
        hide detective talking
        with dissolve
        hide detective normal
        show phone
        with dissolve
        "she hands you a smart phone."
        hide phone
        with dissolve
        show detective normal
        with dissolve
        ava "You'll be using this phone to communicate with our three suspects, the tech guys have set it up to capture everything you guys talk about for evidence."
        show detective talking
        with dissolve
        ava "I'm going to go and research more into how these scammers work why don't you spend some time looking at our suspects profiles before they message you."
        "Ava heads off to start her research, leaving you with your new work phone."
        hide detective talking
        with moveoutright
        show phone
        with moveinbottom
        "On the phone you can see the only app installed is the dating app Ava mentioned. You open it and are greeted with three profiles to look at."
    
        menu profile_menu: 
            "Which profile do you want to view?"

            "Emma" if not viewed_emma:
                $ viewed_emma = True
                call emma_intro
            "Frank" if not viewed_frank:
                $ viewed_frank = True
                call frank_intro
            "Oscar" if not viewed_oscar:
                $ viewed_oscar = True
                call oscar_intro
            
            "continue" if viewed_emma and viewed_frank and viewed_oscar:
                jump getting_started
                return
            
        return


        label getting_started:
            "After looking at the three possible suspects, its far too early into your investigation to guess who the fraudster is."
            "You decide it's time to make contact with your first suspect, since you can do this work anywhere you decided to go for a walk and stretch your legs whilst working."
            scene park 1 day
            with fade
            stop music
            play music "Panaram.wav"
            "You find a nice spot in the park and open up the dating app."
            menu first_chat_menu:
                "who do you want to chat to?"
                "Emma":
                    call emma_first_interaction
                "Frank":
                    call frank_first_interaction
                "Oscar":
                    call oscar_first_interaction
                    return
        return     


label emma_intro:
        show phone at left
        "This profile shows Emma, she's 29 and a software developer."
        show emma normal at right with moveinright
        "Her profile has a witty bio filled with tech jargon and memes. She claims she is looking for \"the real deal\", you notice she has a lot of photos of herself each one 
        perfectly taken, as though by a professional."
        hide emma normal with moveoutright
        jump profile_menu
        return

label emma_first_interaction:
    show phone at left with moveinbottom
    show emma normal at right with moveinright
    "Lets see what Emma is all about."
    emma "Hey I'm Emma nice to meet you. I saw your profile and you seem pretty cool."
    emma "So what do you like to do for fun?"
    menu:
        "Respond about your hobbies":
            "I'm into reading, going out with friends, that kind of thing."
            emma "Nice! I like someone who can balance chill time and social time."
            emma "Ever tried coding or gaming? I Could teach you!"
            jump emma_hobbies

        "Change the subject and ask Emma about her job":
            "What do you do for a living?"
            emma "I'm a software developer. I spend alot of time debugging code for work and working on apps."
            emma "but don't worry I'm not just a computer nerd, I swear!"
            jump emma_hobbies
    return

label emma_hobbies:
    menu:
        "Ask her about gaming":
            "You mentioned gaming. What kind of games do you play?"
            emma "Oh, a little bit of everything. Mostly strategy games and RPGs."
            emma "Actually, I’ve been working on a small indie game on the side. Maybe I’ll show you sometime."
            jump emma_personal
        
        "Ask her about coding":
            "So, what kind of coding do you do?"
            emma "Mainly app development. I love creating things people actually use."
            emma "Right now, I’m working on a finance app—kind of boring but super useful!"
            jump emma_personal

label emma_personal:
    emma "So what about you? What do you do for work?"
    menu:
        "Tell her you're in law enforcement (truthful, vague)":
            "I work in law enforcement. It keeps me busy."
            emma "Whoa, that’s kind of cool! But also, kind of scary?"
            emma "I promise I haven’t done anything illegal... lately. Kidding!"
            jump emma_suspicious
        
        "Give a fake job (undercover strategy)":
            "I work in customer service. Pretty standard stuff."
            emma "Ah, dealing with people all day—I respect that."
            emma "People can be… interesting. I bet you get some weird calls."
            jump emma_suspicious

label emma_suspicious:
    emma "So, tell me something random about yourself!"
    menu:
        "Share a fun fact":
            "I once went skydiving on a dare."
            emma "No way! That’s so cool. I don’t think I could ever do that."
        
        "Ask her something instead":
            "What’s something you’ve always wanted to do?"
            emma "Travel more, for sure. I’ve been to a few places, but I’d love to see the world."
            emma "Actually, I have a trip planned soon. Just waiting for the right time."
            "(Her profile didn’t mention traveling. Odd.)"
    
    "You chat with Emma for a little while longer before wrapping up the conversation."
    hide emma normal with moveoutright
    return


label frank_intro:
        show phone at left
        "This profile shows Frank, he's 26 and an artist."
        show frank normal at right with moveinright
        "His profile shows a free-spirited artist. His bio says he's \"hoping to find someone to share sunsets with and to be his muse\", he appears to be quite the romantic soul."
        hide frank normal with moveoutright
        jump profile_menu
        return

label oscar_intro:
        show phone at left
        "This profile shows Oscar, he's 30 and a financial advisor"
        show oscar normal at right with moveinright
        "Oscars bio is full of motivational quotes and photos showing off a somewhat lavish lifestyle, pictures of himself at parties or possible work gatherings. He's clearly quite sociable."
        hide oscar normal with moveoutright
        jump profile_menu
        return
    
# This ends the game.  
label end_game:
        scene bg gate_day
        "You've finished the game thanks for playing"
return
