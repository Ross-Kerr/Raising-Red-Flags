$ told_truth = False

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


            
