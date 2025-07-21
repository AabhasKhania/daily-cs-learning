# Day 4 – The Foundation Block
# Aabhas Khaniya
# This script simulates confusion and finding stability through logic.

print("🌀 You’re inside The Fog Loop – running but not reaching.")

thoughts = input("What’s on your mind right now? ")
actions = input("What did you do today that felt like progress? ")

print("\n🧱 Processing your mental loop...\n")

if thoughts.strip() == "" and actions.strip() == "":
    print("Silence can be a good start. But don’t mistake stillness for clarity.")
elif "code" in actions.lower():
    print("You showed up to code — that’s enough to plant a seed.")
elif "ran" in actions.lower() or "scroll" in actions.lower():
    print("Sometimes movement is noise. Ask yourself: what was I trying to avoid?")
else:
    print("Whatever you did today, it was real. But was it aligned? That’s the key.")

# Reminder
print("\n📌 Golden Rule: Thinking is not building. Building is building.")
