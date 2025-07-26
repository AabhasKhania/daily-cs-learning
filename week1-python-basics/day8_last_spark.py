# Day 8 – The Last Spark
# Aabhas Khaniya
# A code for the days when everything feels meaningless — but we still type.

def write_one_line():
    line = input("Write one sentence — anything: ")
    return line

def check_for_spark(text):
    if any(word in text.lower() for word in ["hope", "try", "again", "still", "breathe", "live"]):
        return True
    return False

print("📉 You’re here. No purpose, no plan, just typing.\n")

entry = write_one_line()

if check_for_spark(entry):
    print("\n⚡ There’s still a spark. However faint, it’s real.")
else:
    print("\n🌑 That’s okay. You showed up. That’s everything today.")

print("\n💬 Final note:")
print("Even a blank page is progress. Come back tomorrow. You don’t need to be brilliant. Just be.")

