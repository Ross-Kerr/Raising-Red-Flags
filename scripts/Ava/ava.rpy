$ told_truth = False
$ final_choice = ""

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
    ava "We should keep an eye out for these red flags when talking to the suspects."
    ava "So pay attention to what they tell you at the start. It might seem innocent now, but it could be part of a bigger scheme."
    ava "Got it? Good. I'll keep researching and you keep talking to them and let's see what we uncover."
    hide detective normal
    jump emma_day2

$ suspect_reasoning = ""
label ava_day2:
    scene bg downtown 3 night light
    with fade
    "As you walk home, you hear a buzz from your work phone."
    play sound "audio/Effects/phone-vibration.wav"
    show phone at left with moveinleft
    "It's a message from Ava."
    show detective normal at right with moveinright
    ava "Hey there! How’s the investigation going?"
    ava "I've got some more information for you. So turns out there are some common signs of romance fraud."
    ava "They often profess their love quickly, claim to be working overseas, and ask for money for emergencies or travel."
    ava "So keep an eye out for any of these signs in your conversations. It could be a red flag."
    ava "Stay sharp and let me know if you need anything. We’re in this together."
    ava "And remember, we’re here to help the victims. So let’s get to the bottom of this."
    ava "Do you have idea so far as to who the suspect might be?"
    menu suspect_choice:
        "Oscar":
            "I think it might be Oscar."
            ava "Interesting choice. What makes you think it’s him?"
            $ suspect_reasoning = renpy.input("Enter your reasoning:")
            ava "That’s a good point. Keep an eye on him and see if he fits the profile."
            
        "Frank":
            "I think it might be Frank."
            ava "Interesting choice. What makes you think it’s him?"
            $ suspect_reasoning = renpy.input("Enter your reasoning:")
            ava "That’s a good point. Keep an eye on him and see if he fits the profile."
            
        "Emma":
            "I think it might be Emma."
            ava "Interesting choice. What makes you think it’s her?"
            $ suspect_reasoning = renpy.input("Enter your reasoning:")
            ava "That’s a good point. Keep an eye on her and see if she fits the profile."

        "I dont know":
            "I'm not sure yet."
            ava "That's okay. Keep talking to them and see if you can gather more information."
    ava "Alright, keep me updated on your progress. We’ll catch this scammer together."
    ava "I'm going to pull a late nighter to dig up more information. Talk to you in the morning."
    hide detective normal with moveoutright
    hide phone with moveoutleft
    jump day3
    return.

label day3:
    $ emma_questioned = False
    $ frank_questioned = False
    $ oscar_questioned = False

    scene bg library_day
    with fade
    stop music fadeout 2.0
    play music "audio/Wav/1. Playground.wav" fadein 2.0
    show detective normal
    with dissolve
    ava "Good morning! How are you feeling today?"
    ava "I’ve been researching more about romance fraud and I think I’ve found something interesting."
    ava "It seems like the scammer often uses a fake identity to gain trust and manipulate their victims."
    ava "So, it could be that the suspect is using a fake name or identity to lure in their victims."
    ava "Look out for things like photographs that look too good to be true or photographs that don't really show the person's face. These are red flags"
    ava "And remember, trust your instincts. If something feels off, it probably is."
    ava "Maybe try and get a photograph of the suspect to see if it matches up with what you know."
    ava "It might help us narrow down our list of suspects."
    ava "Just be careful to not blow your cover, you're doing great so far."
    hide detective normal
    show phone with moveinleft 
    "Which suspect do you want to talk to first?"
    
    menu suspect_choice2:
        "Oscar" if not oscar_questioned:
            $ oscar_questioned = True
            jump oscar_day3
        "Frank" if not frank_questioned:
            $ frank_questioned = True
            jump frank_day3
        "Emma" if not emma_questioned:
            $ emma_questioned = True
            jump emma_day3
        "Continue" if emma_questioned and frank_questioned and oscar_questioned:
            jump day3_debrief
    return

$ suspect_reasoning2 = ""
label day3_debrief:
    
    scene bg library_afternoon
    with fade
    show detective normal
    with dissolve
    ava "How did your conversations go today?"
    ava "Did you manage to get any photographs of the suspects?"
    "You tell Ava about your conversations with the three suspects and how they went."
    ava "Well that doesn't really narrow it down much."
    ava "But don't worry, we'll get there. We just need to keep digging."
    ava "Have any of them asked for money yet? Or hinted at needing some?"
    ava "Romance fraudsters often ask for money for emergencies or travel, sometimes they do it indirectly by hinting at needing money."
    "You explain that Oscar asked if you would interested in investing in his project and that Frank mentioned he was struggling financially."
    ava "Interesting. Keep an eye on that. It could be a sign that they’re setting you up for a scam."
    ava "Emma hasn't mentioned anything about money yet?"
    "You tell Ava that Emma hasn't mentioned much about money other than that it costs alot to develop a computer game and that she's working on one."
    ava "Well it's hard to say for sure at this point. But keep an eye on all of them."
    ava "Another tactic that is often used is that they attempt to manipulate their victims by playing on their emotions."
    ava "Have any of them tried to manipulate you in any way?"
    "You explain that Emma seemed to be hurt when you asked for a picture of her and that Franks burst water pipe could be potentially be a way of making you feel sorry for him."
    ava "Interesting."
    ava "Unfortunately, we are running out of time. We need to make a decision soon."
    ava "Do you have more thoughts on who our suspect might be? Have you been able to spot any red flags?"
    menu suspect_choice3:
        "Oscar":
            "I think it might be Oscar."
            ava "Interesting choice. What makes you think it’s him?"
            $ suspect_reasoning = renpy.input("Enter your reasoning:")
            ava "Alright, I'll add that to our report."
            
        "Frank":
            "I think it might be Frank."
            ava "Interesting choice. What makes you think it’s him?"
            $ suspect_reasoning = renpy.input("Enter your reasoning:")
            ava "Alright, I'll add that to our report."
            
        "Emma":
            "I think it might be Emma."
            ava "Interesting choice. What makes you think it’s her?"
            $ suspect_reasoning = renpy.input("Enter your reasoning:")
            ava "Alright, I'll add that to our report."

        "I dont know":
            "I'm not sure yet."
            ava "That's okay. We should be able to get more information tomorrow."

    ava "I think we have one more day to gather information before we need to make a decision."
    ava "Keep talking to them, see if you can gather any more information and remember what we've learned. Tomorrow you'll need to decide who our fraudster is."
    hide detective normal
    with dissolve

    jump emma_day4
    return

label final_debrief:
    scene bg library_afternoon
    with fade
    show detective normal with dissolve
    ava "So how did you get on today any final bits of evidence that might help us make a decision?"
    "You tell Ava about your conversations with the three suspects and how they went."
    if emma_paid:
        ava "You gave Emma the money?!"
        ava "You can't give money to a suspect! You could have compromised the entire operation."
        ava "Not to mention you've never met this person in real life. You can't trust them."
    else:
        ava "Well I guess we better quickly recap, the red flags we've learned about, before you make your final decision."
        ava "Romance fraudsters often profess their love quickly, claim to be working overseas, and ask for money for emergencies or travel."
        ava "They often give away harmless personal details early on—like where they grew up, what they do for work, or what their dreams are."
        ava "Later, they use these same details as ‘evidence’ to build their scam, making their requests for money seem more legitimate and urgent."
        ava "They often use a fake identity to gain trust and manipulate their victims into feeling sorry for them. They also try to keep their victims isolated."
        ava "Often the photos they use are too good to be true or don't show the person's face. They can also be photos of someone else."
        ava "They don't always ask for money directly, sometimes they hint at needing money or ask for investments. Sometimes it can be small amounts that they pay back to gain trust."
        ava "They try to make their victims feel special, they often will message the victim frequently and will usually be the first to message. This helps make the victim feel as though they are wanted."
        ava "Finally, these scammers can be incredibly patient and will often work to develop what feels like a true relationship over time, before asking for money."
        ava "So, who do you think our scammer is?"
        menu final_choice:
            "Oscar":
                "I think it might be Oscar."
                $ final_choice = "Oscar"
                ava "Interesting choice. What makes you think it’s him?"
                $ suspect_reasoning = renpy.input("Enter your reasoning:")
                ava "Alright, I'll add that to our report."
                
            "Frank":
                "I think it might be Frank."
                $ final_choice = "Frank"
                ava "Interesting choice. What makes you think it’s him?"
                $ suspect_reasoning = renpy.input("Enter your reasoning:")
                ava "Alright, I'll add that to our report."
                
            "Emma":
                "I think it might be Emma."
                $ final_choice = "Emma"
                ava "Interesting choice. What makes you think it’s her?"
                $ suspect_reasoning = renpy.input("Enter your reasoning:")
                ava "Alright, I'll add that to our report."
        
        ava "Okay I trust your judgement. I'll get a warrant ready and we'll make an arrest tomorrow."
        ava "Thank you for all your hard work. You did great."
        ava "I'll catch up with you tomorrow"
        hide detective normal
        with dissolve

        "You finally made your decision. You hope it's the right one."
        jump case_results
        return

label case_results:
    scene bg courtyard2
    with fade
    "The next day, you meet with Ava at the station."
    show detective normal
    with dissolve
    ava "So, I have the outcome of our investigation."
    ava "We sent uniformed officers to arrest [final_choice] this morning."
    if final_choice == "Oscar":
        ava "Oscar was taken into custody and questioned by the local officers based on the information we sent them."
        ava "I'm sorry to say his story checked out. He's not our scammer."
        ava "He really is an investor and he's been working on a project in the area."
        ava "One of his investors was able to confirm his story."
        ava "I under stand why you thought he was our scammer the story truly did sound like a scam."
        ava "I'm afraid however we need to set him free."
        jump wrong_choice

    elif final_choice == "Frank":
        ava "Frank was taken into custody and questioned."
        ava "I'm sorry to say his story checked out. He's not our scammer."
        ava "He really is a struggling artist and he's been working on a project in the area."
        ava "We were able to confirm his story with his landlord."
        ava "I under stand why you thought he was our scammer the story truly did sound like a scam."
        ava "I'm afraid however we need to set him free."
        jump wrong_choice
    elif final_choice == "Emma":
        ava "Emma was taken into custody and questioned."
        ava "I'm glad to say you were right. She's our scammer."
        ava "She's been using a fake identity to manipulate her victims and has been asking for money for her 'game'."
        ava "We found evidence of her scamming multiple people."
        ava "She's been arrested and will be charged with fraud."
        jump correct_choice
    return
return

label correct_choice:
        
        "You feel a sense of relief."
        "You made the right choice."
        "You helped Ava catch the scammer."
        "You feel like you made a difference."
        "The case is solved."
        jump end_game
        return

label wrong_choice:
    
    "You feel a sinking feeling in your stomach."
    "You made the wrong choice."
    "You let the scammer get away."
    "You feel like you let Ava down."
    "You'll have to live with the consequences of your decision."
    "The case remains unsolved."
    jump end_game
    return




            
