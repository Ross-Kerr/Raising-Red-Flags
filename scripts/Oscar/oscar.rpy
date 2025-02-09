default current_investments = False
default previous_investments = False


$ told_truth = False



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

label oscar_day2:
    scene bg downtown1
    show phone at left
    "It looks like Oscar has sent you a message."
    show oscar normal at right with moveinright
    oscar "Hey there! Hope you’re having a great day."
    oscar "I hope you don't mind me messaging you back so soon, to be honest I'm hoping you can help me with something."
    oscar "I have a big investors meeting later today and I'm feeling a bit stressed."
    oscar "I'm just not sure of myself, what if I screw this up? A lot is riding on this."
    oscar "Any advice?"
    menu:
        "Offer advice":
            "You've got this! Confidence is key. Just be yourself and you'll do great."
            oscar "You really think so?"
            "Of course! You're a pro at this. Just remember to breathe and take it one step at a time."
            oscar "Thanks, I needed that. I'll let you know how it goes."
            oscar "I really appreciate you taking the time to chat with me."

        "Stay neutral":
            "I'm sure you'll be fine, dont stress too much."
            oscar "I guess you're right, thanks."

    oscar "Anyway, I just wanted to say I enjoyed our chat yesterday. I feel like we really connected."
    oscar "I hope we can keep talking, I'd love to get to know you better."
    oscar "Tell you what, I could tell you about some of my investments, let you get a better understanding of what I do."
    menu oscar_investments:
        "Ask about his big meeting today" if current_investments == False:
            "So what is this investment meeting you have today about?"
            $ current_investments = True
            oscar "It's a big one. I'm meeting with some potential investors for a new project."
            oscar "It's a big deal for me, I'm hoping to get them on board."
            oscar "I just need to make sure I'm on top of my game."
            oscar "It's a bid to turn a local abandoned building into an entertainment complex."
            oscar "It'll have things like bowling, arcade games, a bar, and a restaurant."
            oscar "I'm hoping to get the investors to see the potential in it."
            call oscar_investments
        
        "Ask about his previous investments" if previous_investments == False:
            "What kind of investments do you usually work on?"
            $ previous_investments = True
            oscar "I usually work with property investments. I find it's a good way to make money."
            oscar "I've had some good success with it in the past."
            oscar "I'm hoping this new project will be a big hit."
            oscar "I'm always looking for new opportunities to invest in, it's exciting."
            oscar "Like previously I invested in a local coffee shop, it's doing really well."
            oscar "I also managed to get funding for a set of luxury apartments, they're almost finished."
            call oscar_investments
        
        "Continue" if current_investments and previous_investments:
            jump oscar_day2_continue
            return
    return
        
label oscar_day2_continue:
    "You seem to be doing pretty well for yourself."
    "I'm sure you'll do great at your meeting today."
    oscar "Thanks, I appreciate the support. It's a strange feeling sometimes to be dealing with so much money."
    oscar "I think I've managed to get a good grip on it though, anyway I better get going and prepare for this meeting thanks again for the advice."
    hide oscar normal with moveoutright
    hide phone with moveoutright
    "Having finished your chat with Oscar, you decide to continue with your day."
    jump frank_day2
return