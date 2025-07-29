# Day 10 – The 3300 Hour Mirror
# Aabhas Khaniya
# How are you using your free time? This script helps you face that and refocus.

def get_hours(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        return 0.0

print("🪞 Welcome to your 3300-Hour Mirror")
print("⏳ Let’s figure out where your time is really going...\n")

sleep = get_hours("How many hours do you sleep per day (avg)? ")
work = get_hours("How many hours do you work/study per day (avg)? ")
deep_work = get_hours("How many hours of true Deep Work per day? (0–4) ")

total = 24
free_time = total - (sleep + work)

print("\n📊 DAILY TIME STATS:")
print(f"😴 Sleep: {sleep} hrs")
print(f"💼 Work/Study: {work} hrs")
print(f"🧠 Deep Work: {deep_work} hrs")
print(f"🪂 Free Time Left: {free_time:.2f} hrs")

if deep_work < 2:
    print("\n⚠️ Warning: You’re not hitting even 2 hours of focused deep work.")
else:
    print("\n✅ Good job! You’re doing focused work that builds momentum.")

print("\n📌 Reminder:")
print("You don’t need to do more. You need to do what matters — with fewer distractions.")

print("\n💬 Final Note: Use your 3300 hrs wisely. They determine your next 3 years.")
