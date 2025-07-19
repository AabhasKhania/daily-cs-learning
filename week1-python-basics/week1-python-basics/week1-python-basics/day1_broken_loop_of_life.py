# Day 1 – The Broken Loop of Life
# I am not doing the traditional Hello World.
# This is not a perfect code. Just like life, it breaks if you don’t think deeply.
# Try to understand why it fails — and fix it. That's your first lesson.

energy = 100
dream = "To master CS and build my own future"
day = 1

while energy > 0:
    print(f"Day {day}: Still chasing the dream -> {dream}")
    energy -= 10
    day += 1

    if day == 4:
        print("⚠️ Something went wrong. You scrolled the internet for 6 hours.")
        break

print("💡 Lesson: If you don’t break the loop, the loop breaks you.")
