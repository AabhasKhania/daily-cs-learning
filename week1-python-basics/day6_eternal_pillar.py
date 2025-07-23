# Day 6 – The Eternal Pillar
# Aabhas Khaniya
# A simple yet timeless program using all coding fundamentals.

def greet(name):
    return f"🧘 Hello, {name}. You are here. That’s enough for today."

def check_effort(effort_level):
    if effort_level >= 8:
        return "🔥 You're aligned. Your actions match your desire."
    elif effort_level >= 5:
        return "💡 You're trying — now align your focus."
    else:
        return "🌱 At least you're honest. Let this honesty grow roots."

def reflect():
    days = ["Yesterday", "Today", "Tomorrow"]
    reflections = {
        "Yesterday": "Didn’t go as planned. But it’s gone.",
        "Today": "You still have control over your choices.",
        "Tomorrow": "Will be shaped by what you do today."
    }
    for day in days:
        print(f"{day}: {reflections[day]}")

# Execution starts here
name = input("What’s your name, coder? ")
print(greet(name))

effort = int(input("On a scale of 1–10, how much effort are you giving today? "))
print(check_effort(effort))

print("\n📅 Daily Reflection:")
reflect()

print("\n📌 Remember: Coding is not just logic — it’s clarity.")
print("Give your best. Surrender the rest. 🌸")
