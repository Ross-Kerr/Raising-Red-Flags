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
    scene bg office
    with fade
    show detective normal
    with dissolve
    ava "Good morning! How are you feeling today?"
    ava "I’ve been researching more about romance fraud and I think I’ve found something interesting."
    ava "It seems like the scammer often uses a fake identity to gain trust and manipulate their victims."
    ava "So, it could be that the suspect is using a fake name or identity to lure in their victims."
    ava "Look out for things like photographs that look too good to be true or photographs that don't really show the person's face."
    ava "And remember, trust your instincts. If something feels off, it probably is."
    ava "Maybe try and get a photograph of the suspect to see if it matches up with what you know."
    ava "It might help us narrow down our list of suspects."
    ava "Just be careful to not blow your cover, you're doing great so far."
    hide detective normal
    jump end_game
            
