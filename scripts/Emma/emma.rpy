default shared_dream = False
default asked_dream = False


$ shared_dream = False
$ asked_dream = False
$ told_truth = False

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
    return

label emma_day2:
    scene bg downtown1
    with fade
    stop music fadeout 2.0
    play music "the_cafe.wav" fadein 2.0

    "As you walk through the city, on your way to get yourself a coffee, you hear a buzz from your work phone."
    play sound "audio/Effects/phone-vibration.wav"
    show phone at left with moveinleft
    "It's a message from Emma."
    show emma normal at right with moveinright
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
           
        
        "Stay neutral":
            "That’s nice of you to say. I appreciate it."
            emma "Just being honest! I like this."
            emma "I hope you feel the same way."
    emma "I’m really glad we matched. I can’t wait to see where this goes."
    emma "Tell me have you ever had a big dream? something you've always wanted to do?"
    menu emma_dreams:
        "Share your dream" if shared_dream == False:
            "I've always wanted to travel the world. I want to see everything."
            $ shared_dream = True
            emma "That’s amazing! I love that. I think everyone should travel at least once."
            emma "There’s so much to see and learn out there."
            call emma_dreams
            return
        
        "Ask her about her dream" if asked_dream == False:
            "What about you? What’s something you’ve always wanted to do?"
            $ asked_dream = True
            emma "I've always wanted to develop my own computer game."
            emma "The problem is though, the cost involved in making games is super high."
            emma "But I'm working on it, slowly but surely."
            emma "I think it would be so cool to see something I made out there in the world."
            emma "Maybe one day, right?"
            call emma_dreams
            return

        "Continue" if shared_dream and asked_dream:
            jump emma_day2_continue
            return
    return 
label emma_day2_continue:
    emma "I just feel like I could talk to you all day"
    emma "I hope you feel the same way."
    "You chat with Emma for a little while longer until your phone buzzes again."
    play sound  "audio/Effects/phone-vibration.wav"
    "Its a message from Oscar."
    "You let Emma know you have to go and say goodbye."
    hide emma normal with moveoutright
    jump oscar_day2
    return

label emma_day3:
    show phone at left with moveinleft
    show emma normal at right with moveinright
    "You take another look at Emma's profile."
    "The few photos she has of herself are all taken in a professional setting, theres no photos of her in a casual setting or anyone else in the pictures."
    "You decide to send her a message and see how she responds."
    emma "Hey there! How’s your day going?"
    "Not bad, just doing some work. How about you?"
    emma "I'm just working on some code for a new project. It's a big one."
    emma "I'm hoping to get it finished soon so I can continue on my game."
    emma "I'm excited to show you what I've been working on."
    "That sounds interesting, I'd love to see it."
    emma "I'm glad you think so. I'm really proud of it."
    emma "I'm hoping it'll be a big hit."
    "I was wondering do you have photos of your game? or any other projects you've worked on?"
    emma "I do, but I'm not ready to show them yet. I want it to be a surprise."
    emma "I promise I'll show you soon though."
    "I was just looking through your profile, you have some great photos, they look almost too good."
    emma "Thanks! I like to keep things professional."
    emma "I think it's important to present yourself well, you know?"
    emma "My little sister is actually a photographer, she takes all my photos."
    "That's cool, she must be really talented."
    emma "She is! I'm lucky to have her."
    "Do you have pictures of yourself that she didn't take? Selfies maybe? It would be great to you see you in a more relaxed setting."
    emma "I don't really take selfies. I'm not really a fan of them."
    "Not even with friends or family?"
    emma "No not really. I prefer to be behind the camera."
    emma "I don’t really like sending pictures, to be honest."
    "Oh is there a reason for that?"
    emma "Why? Do you not trust me?"
    menu:
        "Tell her the truth":
            "I'm just curious. I like to know the people I'm talking to."
            emma "So you don't trust me?"
            emma "I thought we had something special."
            emma "I guess I was wrong."
            jump emma_defensive
        
        "Lie":
            "No, not at all. I was just curious."
            emma "I get that. I'm just a private person, you know?"
            emma "I like to keep things professional."
    
    emma "I'm sorry, I have to go. I have a meeting to get to."
    emma "I'll talk to you later."
    "You watch as Emma logs off the app."
    "You're left feeling a little unsure about the situation. Perhaps that was one of the red flags Ava mentioned."
    hide emma normal with moveoutright
    jump suspect_choice2
    return

label emma_defensive:
    "You try to explain that you're just trying to get to know her better."
    emma "I don't know, it just feels like you're prying."
    emma "I thought we had a real connection."
    emma "You are supposed to trust me."
    hide emma normal with moveoutright   
    "You try to explain yourself but Emma has already logged off the app."
    "You're left feeling a little unsure about the situation. Perhaps that was one of the red flags Ava mentioned."
    jump suspect_choice2
    return

label emma_day4:
    scene bg neighborhood
    with fade
    stop music fadeout 2.0
    play music "solvepuzzle.wav" fadein 2.0
    "The next morning, as you walk through your neighborhood on the way to work, you hear a buzz from your work phone."
    play sound "audio/Effects/phone-vibration.wav"
    show phone at left with moveinleft
    "It's a message from Emma."
    show emma normal at right with moveinright
    emma "Hey! how are you?"
    emma "I just wanted to say sorry for being kind of short with you yesterday about the photos."
    emma "I've just been a bit stressed with work lately and I took it out on you and I apologise."
    emma "I hope you can forgive me."
    "It's okay, I understand. We all have bad days."
    emma "Thank you for understanding. I really appreciate it."
    emma "I need to go now, I have a meeting to get to."
    emma "I'll talk to you later."
    "You watch as Emma logs off the app."
    hide emma normal with moveoutright
    hide phone with moveoutleft
    jump oscar_day4
    return

label emma_day4_part2:
    scene bg library_afternoon
    with fade
    "You prepare to meet with Ava to discuss the case. When you hear a buzz from your work phone."
    play sound "audio/Effects/phone-vibration.wav"
    show phone at left with moveinleft
    "It's Emma."
    show emma normal at right with moveinright
    emma "Oh my god! I can't believe it!"
    emma "I just got a call and you wont beleive it!"
    "Is everything okay?"
    emma "Yeah better than okay! I just got a call from game jam I signed up for months ago."
    emma "They rejected me a few months back as they were fully booked but they called to say someone has cancelled and a space has opened up."
    emma "I'm so excited! I can't believe it!"
    "That's great news! I'm so happy for you."
    emma "Thanks! I've been working so hard on my game lately and this could be the big break I've been waiting for."
    emma "There are alot of game developers and publishers going to be there so it's a great opportunity for me to show off my game and maybe even get it picked up."
    "That's amazing! I'm so happy for you."
    emma "Thank you! I have just one massive favour to ask you though and I know it's a big ask."
    emma "There is a £25 entry fee that needs paid today and I don't get paid until tomorrow. I was wondering if you could help me out?"
    "This is exactly what Ava warned you about. It's a red flag."
    emma "I know it's a big ask and I wouldn't ask if I wasn't desperate."
    emma "I'll send you the money back first thing in the morning when I get paid and I'll send you all the information you want so you know I'm legit."
    "A number of links appear in the app."
    "The first is a link to the game jam website, the second is a link to a payment page."
    menu:
        "Check out the webiste":
            "You click on the link to the game jam website."
            "It's a legitimate website for game developers to showcase their work and get it picked up by publishers."
            "You see the event Emma mentioned is taking place this weekend and is located in the city."
            "The website lists the entry fee of £25 and the deadline for payment as today."

        "Check out the payment page":
            "You click on the link to the payment page."
            "It's a well known payment service that is used by many people to send and receive money called 'FundFriends'."
            "You see the payment is for £25 and the recipient is Emma's email address."

    emma "I also have a bunch of screenshots of my game if you want to see them."
    "A number of screenshots appear in the app."
    hide emma normal with moveoutright
    hide phone with moveoutleft
    show emma_game_art at truecenter with dissolve
    "The screenshots show various aspects of the game, such as a main menu, and a few vehicles like tanks and jets."
    hide emma_game_art with moveoutdown
    show phone at left with moveinleft
    show emma normal at right with moveinright
    emma "I'ts a strategy game where you build your own base and army and take on other players."
    emma "I haven't gotten the multiplayer aspect working yet but I'm hoping to have the single player side finished before the event."
    "It looks great! I'm really impressed."
    emma "So what do you think? Can you help me out?"
    emma "You'll be helping to take a chance at my dream and like I said I'll pay you back tomorrow."
    "It is a relatively small amount of money and Emma has promised to pay you back."
    "But it's still a red flag."
    "What do you do?"
    menu:
        "Pay the entry fee":
            "You decide to help Emma out and pay the entry fee."
            "You send the money and Emma thanks you."
            "You feel good about helping her out and hope that she gets her big break."
            jump emma_paid

        "Decline":
            "You decide not to help Emma out and decline her request."
            "You tell her you can't help her out and she seems disappointed but understanding."
            "You wish her luck with the game jam and hope she gets her big break."
            jump emma_refused

    return

label emma_paid:
    emma "Oh my god thank you so much!"
    emma "I can't believe you did that for me."
    emma "I promise I'll pay you back first thing tomorrow."
    emma "You've helped me take a chance at my dream and I'll never forget it."
    "You watch as Emma logs off the app."
    hide emma normal with moveoutright
    hide phone with moveoutleft
    "Maybe this wasn't the best thing to do. You need to go speak to Ava and decide on who your suspect is."
    jump final_debrief
return
label emma_refused:
    emma "What? Why not?"
    emma "I can't beleive you're not going to help!"
    emma "I'm going to miss on a huge opportunity because of you!"
    emma "All for just £25 which I would have paid back tomorrow."
    emma "I can't beleive you!"
    "You watch as Emma logs off the app."
    hide emma normal with moveoutright
    hide phone with moveoutleft
    "You need to go speak to Ava and decide on who your suspect is."
    jump final_debrief

return


    jump end_game

            
