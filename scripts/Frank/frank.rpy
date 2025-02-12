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

label frank_day3:
    show phone at left with moveinleft
    show frank normal at right with moveinright
    "You take another look at Frank's profile."
    "His photos are all of his artwork, there's no photos of himself other than his profile picture."
    "This seems a little strange and even suspicious."
    "You decide to send him a message and see how he responds."
    frank "Hey there! How’s your day going?"
    "Not bad, just doing some work. How about you?"
    frank "Not great, to be honest."
    frank "Thats why I haven't messaged, I've been dealing with an emergency."
    "I'm sorry to hear that. What happened?"
    frank "I had a leak in my apartment, it's been a nightmare."
    frank "I had to call a plumber and it's going to cost a fortune."
    frank "I don't know how I'm going to afford it."
    "That sounds really stressful. I hope it gets sorted out soon."
    frank "Thanks, I appreciate it. I just feel like everything is going wrong."
    frank "I'm sorry to unload on you like this."
    "It's okay, I'm here to listen if you need to talk."
    frank "You're really sweet. I'm glad we matched."
    "I actually wanted to ask you something."
    frank "Ask away mon cheri."
    "Do you have any pictures of yourself? I'd love to see more of you."
    "you only have pictures of your artwork on your profile."
    frank "I'm sorry, I don't have any pictures of myself."
    frank "I'm a little camera shy."
    frank "The only picture I have on my phone is of my latest artwork."
    "He sends you a picture of his latest painting, it's a beautiful landscape."
    hide phone with dissolve
    hide frank normal with dissolve
    show franks_art at truecenter with dissolve
    "Wow, that's really impressive. You're really talented."
    hide franks_art with dissolve
    show frank normal at right with dissolve
    show phone at left with dissolve
    frank "Thank you, I'm glad you like it."
    frank "I'm really proud of that one."
    frank "I'm glad I can share it with you."
    "It just seems a shame that you don't have any pictures of yourself."
    "It's just a little strange."
    frank "I know, I'm sorry. I'm just not comfortable with it."
    frank "I hope you understand."
    frank "Maybe if I can fix my apartment I can find the time to take a picture of myself."
    frank "I'd love to show you who I am."
    "That would be nice, I'd like to see who I'm talking to."
    "You chat with Frank for a little while longer before wrapping up the conversation."
    "You're left feeling a little unsure about the situation. Perhaps that was one of the red flags Ava mentioned."
    hide frank normal with moveoutright
    hide phone with moveoutleft
    jump suspect_choice2
    return

label frank_day4:
    show phone at left with moveinleft
    "You open up your phone and send a message to Frank, after several minutes you get a response."
    show frank normal at right with moveinright
    frank "Well my day just got a whole lot better, now that I'm talking to you."
    frank "I've been thinking about you all day."
    "That's really sweet of you to say."
    frank "It's true. I can't get you out of my head."
    frank "It's the thought of you that has kept me going over the last few days."
    "I'm flattered, but that's a lot of pressure."
    frank "Don't worry, just your natural charm is enough."
    frank "You've been a massive inspiration lately, I got the repair bill for my apartment."
    frank "It's going to cost a lot more than I thought. Close to £1000!"
    "That's a lot of money. I'm sorry to hear that."
    frank "I don't know how I'm going to afford it."
    frank "I thought that since your such a positive part of my life, I'd see if you could help me."
    "You recall that Ava mentioned that scammers often ask for money for emergencies."
    frank "So I buckled down and got to work painting! I used you as my muse and I think I've outdone myself."
    frank "I've spent all night working on a few new pieces and I think they're some of my best work."
    frank "Now I just need to sell them!"
    "Well I'm flattered that I inspired you."
    frank "I was hoping you could help me sell them this weekend."
    frank "I know it's a lot to ask, but I'm desperate."
    "He sends you a link to an art gallery where his work is being displayed."
    "The gallery is real and located in the next city over but there is no mention of his work specifically. There is an amatuer art display on this weekend."
    frank "I just thought it would be a great opportunity for us to meet."
    frank "Plus if you help me sell my art, you will literally be my hero coming to save me!"
    frank "Also who knows maybe you'll find something you like."
    "The situation leaves you feeling a little uneasy. It seems like Frank is asking for a lot."
    "It's a delicate situation, how will you respond?"
    menu:
        "Lie and say you can't make it":
            "I'm so sorry Frank, I have to work this weekend."
            frank "Oh."
            frank "That's a shame."
            frank "I really thought you'd want to help me."
            frank "I guess I was wrong."
            "Before you have a chance to respond, Frank logs off."
            "You're not sure if you made the right choice. He could be attempting to emotionally manipulate you into helping like Ava mentioned."
            "This could be a red flag."
            hide frank normal with moveoutright
            hide phone with moveoutleft
            jump emma_day4_part2

        "Agree to go":
            "I'd love to help you out Frank."
            frank "Really? That's amazing!"
            frank "I can't wait to see you in person."
            frank "I'll make sure you have a great time."
    
    frank "Anyway I better go and keep working on my art."
    frank "I'll see you this weekend."
    "You watch as Frank logs off and you're left feeling a little uneasy."
    hide frank normal with moveoutright
    hide phone with moveoutleft
    jump emma_day4_part2
    return


        
