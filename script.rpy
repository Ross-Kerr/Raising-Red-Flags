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
        ava "Try to learn as much about the suspects as you can and don't forget to keep me updated on your progress."
        ava "Also don't forget to keep your cover story straight, we don't want to scare off the suspect."
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

            $ interacted_emma_day1 = False
            $ interacted_frank_day1 = False
            $ interacted_oscar_day1 = False
            "After looking at the three possible suspects, its far too early into your investigation to guess who the fraudster is."
            "You decide it's time to make contact with your first suspect, since you can do this work anywhere you decided to go for a walk and stretch your legs whilst working."
            scene park 1 day
            with fade
            stop music
            play music "Panaram.wav"
            "You find a nice spot in the park and open up the dating app."
            menu first_chat_menu:
                "who do you want to chat to?"
                "Emma" if not interacted_emma_day1:
                    $ interacted_emma_day1 = True
                    call emma_first_interaction
                "Frank" if not interacted_frank_day1:
                    $ interacted_frank_day1 = True
                    call frank_first_interaction
                "Oscar" if not interacted_oscar_day1:
                    $ interacted_oscar_day1 = True
                    call oscar_first_interaction
                    return
            
            "Before you know it, the sun is setting and it's time to head home."
            "You've made good progress today, but you know there's still a long way to go before you can catch the fraudster."
            "Perhaps Ava has some more information for you tomorrow."
            jump day1_debrief
        return     
# Scripts for Emma
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
            $ told_truth = True
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
            emma "I've always wanted to develop my own computer game."
            emma "The problem is though, the cost involved in making games is super high."
            
    
    "You chat with Emma for a little while longer before wrapping up the conversation."
    hide emma normal with moveoutright
    jump first_chat_menu

# Scripts for Frank
label frank_intro:
        show phone at left
        "This profile shows Frank, he's 26 and an artist."
        show frank normal at right with moveinright
        "His profile shows a free-spirited artist. His bio says he's \"hoping to find someone to share sunsets with and to be his muse\", he appears to be quite the romantic soul."
        hide frank normal with moveoutright
        jump profile_menu
        return

label frank_first_interaction:
    show phone at left with moveinbottom
    show frank normal at right with moveinright
    "Time to see what Frank is all about."
    frank "Hey there! I’m really glad we matched. You seem really interesting."
    frank "So tell me, what’s something unique about you? I’d love to know more."
    
    menu:
        "Share something personal":
            "Well, I have a hobby that not many people know about. I love painting."
            frank "That’s amazing! Art is such a great way to express yourself."
            frank "I’d love to see your work sometime—only if you’re comfortable, of course!"
            jump frank_interest
        
        "Keep it vague":
            "Oh, I don’t know. I guess I just have a unique perspective on things."
            frank "That’s intriguing. I’d love to hear more about your perspective sometime."
            frank "Conversations like this are what really make connections special."
            jump frank_interest

label frank_interest:
    frank "I have to say, there’s something really captivating about you."
    frank "Like, I can already tell you’re someone worth knowing."
    menu:
        "Flirt back":
            "Oh? And what makes you say that?"
            frank "Just a feeling. Call it an artist’s intuition."
            frank "There’s something about the way you express yourself—I can tell you have depth."
            jump frank_personal
        
        "Play it cool":
            "Well, that’s very kind of you. I appreciate it."
            frank "Just being honest. I like getting to know genuine people."
            frank "And you seem like someone really special."
            jump frank_personal

label frank_personal:
    frank "So, what do you do for work?"
    menu:
        "Tell him you're in law enforcement (truthful, vague)":
            "I work in law enforcement."
            $ told_truth = True
            frank "Wow, that’s really cool. Must be tough, though."
            frank "I respect people who dedicate their lives to helping others."
            jump frank_suspicious
        
        "Give a fake job (undercover strategy)":
            "I work in event planning."
            frank "Oh, that sounds fun! Bringing people together and making memories."
            frank "I bet you have an eye for detail. That’s something I really admire."
            jump frank_suspicious

label frank_suspicious:
    frank "I feel like we really click, you know?"
    menu:
        "Agree with him":
            "Yeah, this conversation has been really nice."
            frank "Exactly! It’s not every day you meet someone who just gets it."
        
        "Keep things neutral":
            "I’m enjoying our chat too."
            frank "That means a lot. I really value good conversation."
    
    "You chat with Frank for a while longer before wrapping up the conversation."
    hide frank normal with moveoutright
    jump first_chat_menu

# Scripts for Oscar
label oscar_intro:
        show phone at left
        "This profile shows Oscar, he's 30 and a financial advisor"
        show oscar normal at right with moveinright
        "Oscars bio is full of motivational quotes and photos showing off a somewhat lavish lifestyle, pictures of himself at parties or possible work gatherings. He's clearly quite sociable."
        hide oscar normal with moveoutright
        jump profile_menu
        return

label oscar_first_interaction:
    show phone at left with moveinbottom
    show oscar normal at right with moveinright
    "Time to see what Oscar is all about."
    oscar "Hey! Nice to match with you. You have great taste."
    oscar "So, tell me, do you like the finer things in life?"
    
    menu:
        "Play along":
            "Oh, absolutely. A little luxury never hurts."
            oscar "Exactly! Life’s too short not to enjoy it."
            oscar "I love traveling, fancy dinners, and good company. Speaking of, ever been to Paris?"
            jump oscar_travel
        
        "Keep it modest":
            "I think simple things can be just as enjoyable."
            oscar "I respect that! Though, sometimes treating yourself is worth it."
            oscar "I love traveling, fancy dinners, and good company. Speaking of, ever been to Paris?"
            jump oscar_travel

label oscar_travel:
    menu:
        "Say you've been to Paris":
            "Yeah, I’ve been once. It was amazing."
            oscar "Right? The vibe, the food, the art—it’s unmatched."
            oscar "Actually, I might be heading there soon for work. Business and pleasure, you know?"
            jump oscar_job
        
        "Say you haven't been":
            "Not yet, but I'd love to go someday."
            oscar "You totally should! I could even give you some recommendations."
            oscar "Actually, I might be heading there soon for work. Business and pleasure, you know?"
            jump oscar_job

label oscar_job:
    oscar "What about you? What do you do for work?"
    menu:
        "Tell him you're in law enforcement (truthful, vague)":
            "I work in law enforcement."
            $ told_truth = True
            oscar "Oh wow, that’s intense. Must be exciting though."
            oscar "I bet you see some crazy stuff. Hopefully nothing that involves me! Haha."
            jump oscar_suspicious
        
        "Give a fake job (undercover strategy)":
            "I work in marketing. Pretty standard stuff."
            oscar "Ah, making people want what they don’t need. Smart."
            oscar "I respect that hustle. The right branding makes all the difference."
            jump oscar_suspicious

label oscar_suspicious:
    oscar "So, what’s something you’d splurge on if money wasn’t an issue?"
    menu:
        "Talk about travel":
            "Definitely travel. Seeing new places, experiencing different cultures."
            oscar "Yes! That’s what life is about."
            oscar "Actually, I have a big trip planned soon. Just waiting for the right moment."
            
        
        "Talk about investments":
            "Honestly? I’d invest it. Make that money work for me."
            oscar "Smart thinking. It’s all about financial freedom."
            oscar "I actually help people with that. If you ever want tips, let me know."
    
    "You chat with Oscar for a while longer before wrapping up the conversation."
    hide oscar normal with moveoutright
    jump first_chat_menu

# Scripts for Ava
label day1_debrief:
    scene bg library_day
    with fade
    show detective normal
    with dissolve
    ava "So, how did it go? Ready for the next step?"
    "You tell Ava about your conversations with the three suspects and how they went."
    
    if told_truth:
        show detective angry
        with dissolve
        ava "Wait a second—did you tell any of them that you're in law enforcement?"
        ava "You can’t just go around giving out that kind of information! You could have compromised the entire operation."
        ava "From now on, keep your cover story straight. We don’t want to scare off the suspect."
        show detective normal
        with dissolve
    
    ava "Alright, I've done some research, let’s talk about a key tactic romance fraudsters use."
    ava "They often give away harmless personal details early on—like where they grew up, what they do for work, or what their dreams are."
    ava "Later, they use these same details as ‘evidence’ to build their scam, making their requests for money seem more legitimate and urgent."
    ava "So pay attention to what they tell you at the start. It might seem innocent now, but it could be part of a bigger scheme."
    ava "Got it? Good. I'll keep researching and you keep talking to them and let's see what we uncover."

    
# This ends the game.  
label end_game:
        scene bg gate_day
        "You've finished the game thanks for playing"
return
