# Day 3 – The Decision Tree
# Aabhas Khaniya
# Simulates choosing between life paths when you're not sure where you're heading.

print("🚦 Welcome to the Life Decision Tree.\n")
name = input("What's your name, wanderer? ")
print(f"\nHi {name}, let’s explore what path you feel drawn to today.\n")

print("Choose your current interest:")
print("1. BSc Nursing")
print("2. Computer Science")
print("3. I don’t know / I'm confused")

choice = input("Enter 1, 2 or 3: ")

if choice == "1":
    print("\n🩺 You chose Nursing. You care deeply about helping others.")
    print("That path takes courage, empathy, and deep emotional balance.")
    print("Keep observing: Is this interest coming from passion or pressure?")

elif choice == "2":
    print("\n💻 You chose Computer Science. A world of logic and creation awaits.")
    print("Keep showing up. Mastery comes from patience, not speed.")

elif choice == "3":
    print("\n🌫️ Uncertainty is not a weakness.")
    print("Explore widely. Talk less. Notice what pulls your heart quietly.")
    print("Even walking confused is better than standing still.")

else:
    print("\n❌ Invalid choice. Life won’t wait forever for clarity — choose again tomorrow.")

print("\n🧠 Daily Insight: You don’t need the whole map. Just the next step.")
