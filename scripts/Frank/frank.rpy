$ told_truth = False

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