# Day 2 – The Inner Agent
# Aabhas Khaniya
# This program responds to your mood and reminds you of your deeper goal.

name = input("What’s your name, traveler of code? ")
mood = input("How are you feeling today, honestly? ")
goal = input("What do you want to become? ")

print("\n🧠 Analyzing your current vibe...\n")

if mood.lower() in ["tired", "lost", "sad", "lazy"]:
    print(f"Hey {name}, I hear you're feeling {mood}.")
    print(f"But remember your goal: {goal}")
    print("Sometimes, the only way forward is through. Let’s not stop.")
else:
    print(f"Nice energy, {name}! Being {mood} is power.")
    print(f"Let’s move a little closer to your goal: {goal}")

print("\n💡 Daily Reminder: Don’t trust how you feel. Trust what you’re building.")
