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

label emma_day2:
    scene bg downtown1
    with fade
    "As you walk through the city, on your way to get yourself a coffee, you hear a buzz from your work phone."
    play sound phone_vibrate
    show phone at left with moveinleft
    "It's a message from Emma."
    emma "Hey you! I was hoping to hear from you."
    emma "You know, I feel like we’re really clicking. Like, I can talk to you about anything."
    emma "Is that weird to say? I don’t know, I just trust you already."
    emma "I just feel like we really clicked, you know? Like, there’s something about you."
    emma "I don’t open up to people this quickly usually, but with you, it feels easy."
    emma "Maybe it’s crazy, but do you ever just meet someone and feel like you were meant to?"
    menu:
        "Encourage her":
            "That’s really sweet. I feel like we’re building something good too."
            emma "I love that! It’s so rare to just click with someone so quickly."
            emma "I don’t know... I just feel like I can be myself with you."
            jump suspect_menu2
        
        "Stay neutral":
            "That’s nice of you to say. I appreciate it."
            emma "Just being honest! I like this."
            emma "I hope you feel the same way."
            jump suspect_menu2
