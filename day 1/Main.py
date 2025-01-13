print("Hello! I am a Ai bot what's your name? : ")

name = input()

print(f"Nice to  Meet you {name}")

print("How are you feeling today? (good/bad)")

mood = input().lower()


if mood =="good":
    print("I am glad to hear that")
elif mood ==  "bad":
    print("I'm Sorry  to hear that. Hope things get better soon.")
else:
    print("I see.  Sometimes it's haard to put feelings into words")

print(f"It was nice meeting you {name}")