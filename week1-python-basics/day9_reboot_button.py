# Day 9 – The Reboot Button
# Aabhas Khaniya
# A fast restart script when life feels scrambled.

def reboot():
    confirm = input("💥 Everything’s noisy. Want to mentally reboot? (yes/no): ")
    if confirm.lower() == "yes":
        print("\n🔄 Clearing emotional cache...")
        print("🧘 Restoring silence...")
        print("💡 Reminder: You can start again. Any day. Any moment.")
    else:
        print("\n⚙️ Staying in current mode. No problem. You're allowed to pause.")

print("🔘 Press the reboot button if you need a mental reset.\n")
reboot()
