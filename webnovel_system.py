from ai import call_gpt

def main ():
    print("THE HEAVENLY WEBNOVEL ARCHIVE SYSTEM")
    name= input("State your reader name, Cultivator :")
    trope= input ("Favorite trope? (eg, reincarnation weak to strong, system ui, Villainess")
    vibe= input("Enter your desired mood(eg; dark and gritty, Peak fiction, Pure comedy, slop)")

    print("\n[System] Accessing the heaveenly Archives....\n")
    prompt =f"""
    Act as a dramatic Webnovel system spirt assigning a novel to a reader {name}.
    1 real popular webnovel matching the trope '{trope}'and vibe '{vibe}'.
    Format your output exactly like this template:
    *********************************************
    TITLE: [Novel Title]
    TROPE:[TROPE]
    BINGE RATING: [Rating out of 10]

    SYNOPSIS
    [2-sentense hook]
    SYSTEM'S WARNING TO {name}:
    [1 funny warning about reading late at night]
    **********************************************

    """
    recommendation= call_gpt(prompt)
    print(recommendation)
if __name__=="__main__":
    main()