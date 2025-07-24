# Day 7 – Life Architect
# Aabhas Khaniya
# Build your life like you build software — with purpose, modules, and clarity.

def choose_from(prompt, options):
    print(f"\n{prompt}")
    for idx, opt in enumerate(options):
        print(f"{idx + 1}. {opt}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return options[choice]

# Step 1 – Foundation
identity = choose_from("Who are you building today?", [
    "Disciplined Coder",
    "Mindful Learner",
    "Spiritual Explorer",
    "Resilient Warrior"
])

# Step 2 – Modules
modules = []
print("\nPick 3 modules to install in your life today:")
options = ["Focus", "Courage", "Clarity", "Gratitude", "Deep Work", "Patience"]
for _ in range(3):
    module = choose_from("Choose a module:", options)
    modules.append(module)
    options.remove(module)

# Step 3 – Trigger
trigger = input("\nWhat usually breaks your focus? Be honest: ")

# Output
print(f"\n🛠️ Booting up your system as: {identity}")
print("🔧 Modules Installed:", ", ".join(modules))
print(f"⚠️ Detected Disruptor: '{trigger}'")

# Final Reminder
print("\n📌 Final System Note:")
print("Build like a coder. Reflect like a monk. Adapt like a warrior.")
