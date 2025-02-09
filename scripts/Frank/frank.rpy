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

label frank_day2:
    scene bg hall day
    with fade
        
    "You've spent the afternoon filling out paperwork and updating your notes on the case."
    "As you head out of the office, you decide you should contact Frank and send him a message." 
    show phone at left with moveinleft
    show frank normal at right with moveinright
    frank "Hey there! I was hoping to hear from you."
    frank "I’ve been feeling kind of down lately."
    frank "Selling art has been tough, and money’s getting tight."
    frank "I pour my heart into my paintings, but it’s like no one sees their worth."
    frank "Sometimes I wonder if I should just give up, but I don’t know who I’d be without my art."
    menu:
        "Offer support":
            "That sounds really hard. I’m sorry you’re going through that."
            frank "Thanks... It means a lot to hear that."
            frank "I just wish people appreciated art more, you know?"
            frank "It’s not just about the money, it’s about feeling like what I create matters."
            frank "But enough about me... Tell me, what keeps you going when things get tough?"
            menu:
                "Share something motivational":
                    "I try to remind myself why I started. Passion is worth the struggle."
                    frank "That’s a beautiful way to look at it."
                    frank "Maybe I need to stop worrying about the sales and just focus on creating."
                    
                "Keep it lighthearted":
                    "Honestly? Coffee and good music."
                    frank "Ha! I love that. Simple joys, right?"
                    frank "Maybe I just need a good playlist while I paint."
                    
        
        "Change the subject":
            "That’s rough. But hey, let’s talk about something fun to cheer you up."
            frank "Yeah... maybe that would help."
            frank "Tell me something good that happened to you lately."
            menu:
                "Share a positive moment":
                    "I had a really good day at work recently."
                    frank "That’s great to hear! I love when things just fall into place."
                    frank "Maybe my luck will turn around too."
                    
                "Make a joke":
                    "I finally managed to cook a meal without burning it."
                    frank "Oh, that’s an accomplishment worth celebrating!"
                    frank "Maybe you’ll have to cook for me sometime."
    
    frank "Maybe I should use you as an inspiration for my next painting."
    frank "I feel like you have a lot of depth and emotion. It could be really powerful."
    menu:
        "Encourage him":
            "I’d be honored. Your art is amazing, I’d love to see your vision of me."
            frank "Thank you. I’ll make sure it’s something special."
        
        "Stay neutral":
            "That’s a really kind offer. I appreciate it."
            frank "I just think you have a lot of stories to tell. I’d love to capture that."
    frank "I really think that anything is possible when you have the right inspiration."
    frank "And I definitely feel inspired when I talk to you."
    frank "I know it might seem intense but that is just who I am."
    frank "You just got to embrace the intensity of life."
    "You chat with Frank for a little while longer before wrapping up the conversation."
    hide frank normal with moveoutright
    hide phone with moveoutleft
    "You head home, you try and recall anything that might help you in your investigation."
    jump ava_day2
    return
