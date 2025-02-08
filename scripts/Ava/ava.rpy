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

