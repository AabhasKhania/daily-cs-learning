 # Day 5 – The Script That Wrote You
# Aabhas Khaniya
# This script reflects the repetitive loops in life... and asks if you're awake.

def ask(prompt):
    return input(f"{prompt}\n> ")

def reflect_on_life():
    print("🎭 Welcome to 'The Script That Wrote You'\n")
    name = ask("What’s your name?")
    stage = ask(f"{name}, where are you in life? (student / worker / unsure)")

    script = [
        "Study hard or you'll fail.",
        "Get marks or you won't get a job.",
        "Get a job or you’ll be a failure.",
        "Buy a house or you won’t be respected.",
        "Get married or you’ll be alone.",
        "Have kids or your life is incomplete.",
        "Work till 60 and then... rest.",
    ]

    print("\n📜 Loading script you were handed...\n")
    for line in script:
        print(f"– {line}")
    
    pause = ask("\nHave you ever questioned this script? (yes / no)")
    
    if pause.lower() == "no":
        print("\n🤖 You’ve just been executing. That’s okay. We all start somewhere.")
    else:
        print("\n🧠 Good. Awareness is the first step to authorship.")
    
    passion = ask("\nWhat would you do if no one was watching?")
    
    if passion.strip() == "":
        print("\n🕳️ Even emptiness is a good place to begin. At least it’s yours.")
    else:
        print(f"\n💡 That spark matters. Build a life where you don’t bury it.")

    print("\n📌 Final Thought:")
    print("The difference between the child in class 6 and the adult now isn't age. It's authorship.")
    print("Write your own script, one line a day.")

# Run the program
reflect_on_life()
