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
