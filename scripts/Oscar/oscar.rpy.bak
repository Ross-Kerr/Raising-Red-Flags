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

label oscar_day3:
    show oscar normal at right with moveinright
    show phone at left with moveinleft
    "You take another look at Oscar's profile."
    "His photos show him at various events and gatherings, always surrounded by people."
    "He has quite a few photos of landmarks from other countries, suggesting he travels often."
    "You see photos of the Eiffel Tower, the Leaning Tower of Pisa and even the Great Wall of China."
    "You decide to send him a message and see how he responds."
    oscar "Hey I was hoping to hear from you today. How’s your day going?"
    "Not bad, just doing some work. How about you?"
    oscar "My day is going okay despite the stress of the meeting yesterday."
    oscar "I was able to get the investors on board with the project, they loved the idea."
    oscar "However they didn't invest as much as I was hoping for, so I'm still a bit stressed."
    "I'm glad to hear it went well for you."
    oscar "Thanks, I appreciate that. I'm just hoping I can make this project a success."
    oscar "I dont suppose you know anyone who would be interested in investing in a project like this?"
    menu:
        "Offer to help":
            "I might know someone who would be interested. I can ask around for you."
            oscar "That would be amazing! I'd really appreciate that."
            oscar "I'm hoping to get the funding I need to make this project a success."
            oscar "I'll owe you big time if you can help me out."
            oscar "I don't suppose you'd be interested in investing yourself?"
            menu:
                "Say you'd consider it":
                    "I'd have to look into it, but I'm open to the idea."
                    oscar "That's all I ask."
                    oscar "I just need to get the funding I need to make this project a success."
                    oscar "I'll owe you"

                "Say you are not interested":
                    "I'm not in a position to invest right now."
                    oscar "That's okay, I understand."
                    oscar "I'm just hoping I can get the funding I need to make this project a success."
                    oscar "I'll owe you big time if you can help me out."
        
        "Stay neutral":
            "I'm not sure, but I'll keep an ear out."
            oscar "That's okay, I appreciate you even considering it."

    "Do you have any photos of the project you could show me?"
    "I'd love to see what you're working on."
    oscar "Not at the moment, all I have are a few boring blueprints."
    oscar "I'm hoping to get some photos of the building soon though."
    oscar "I'll make sure to show you when I do."
    "I was just looking through your profile, you seem to travel a lot."
    "What's your favorite place you've visited?"
    oscar "That's a tough one, I've been to so many amazing places."
    oscar "I think my favorite would have to be Venice, it's just so beautiful."
    oscar "The food, the art, the culture, it's all amazing."
    "I'd love to visit Venice one day."
    oscar "You should, it's an amazing experience."
    oscar "I could even show you around if you wanted."
    oscar "If I'm able to pull of this big project, I might even be able to take you there."
    "That sounds amazing, I'd love to see Venice."
    oscar "I'll make sure to keep you updated on the project then."
    "You chat with Oscar for a little while longer and then say goodbye."
    hide oscar normal with moveoutright
    hide phone with moveoutleft
    "You decide its best to start filling in your report for today before you forget anything."
    jump suspect_choice2
    return

label oscar_day4:
    scene bg library_day
    "You arrive at work and continue to work on your case notes."
    "You're interrupted by a message from Oscar."
    play sound "audio/Effects/phone-vibration.wav"
    show phone at left with moveinleft
    show oscar normal at right with moveinright
    oscar "Hey there! How’s your day going?"
    "Not bad, just doing some work. How about you?"
    oscar "Pretty good, I can't really complain about my office today haha!"
    hide oscar normal with dissolve
    hide phone with dissolve
    show oscar_beach at truecenter with dissolve
    "An image appears in the chat window, it shows a beach with a stunning cityscape in the background."
    "The message reads 'Wish you were here'."
    hide oscar_beach with dissolve
    show oscar normal at right with dissolve
    show phone at left with dissolve
    oscar "I'm just taking a break from work and enjoying the view."
    oscar "I've got some great news I was able to find another investor for the project."
    oscar "So I think I've earned a little break don't you think?"
    "That's great news, congratulations!"
    oscar "Thanks, it does mean I'll need to extend my stay here a little longer."
    oscar "Maybe you could come out and join me for the weekend?"
    oscar "It would be great to meet you in person and show you around."
    "That sound like fun, I'd love to be able to come out."
    oscar "Great! I'll start looking at flights and hotels for you."
    oscar "I'll make sure to keep you updated on the details."
    "A few moments go by before you receive another message from Oscar."
    oscar "So slight issue, my credit card isn't working out here."
    oscar "I'll see what I can figure out, but you might need to book the flights yourself."
    oscar "I'll keep trying and keep you posted, maybe I can get through to the credit card company later."
    oscar "It's a shame as I was really looking forward to meeting you, and really wanted to spoil you for the weekend."
    oscar "Anyway I better get back to work, I'll message you later."
    hide oscar normal with moveoutright
    hide phone with moveoutleft
    "You're left feeling a little unsure about the situation. Perhaps that was one of the red flags Ava mentioned."
    "You haven't heard from Frank yet, maybe you should check in with him."
    jump frank_day4
    return
