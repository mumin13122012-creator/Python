import datetime

# --- Step 1: Display Current Date and Time ---
current_time = datetime.datetime.now()
print("=" * 45)
print("          MY DAILY MOOD ADVISOR          ")
print("=" * 45)
print("Date & Time:", current_time.strftime("%A, %B %d, %Y - %I:%M %p"))
print("-" * 45)

# --- Step 2: Collect User Inputs ---
user_name = input("Enter your name: ")
mood = input("How are you feeling today? (happy, sad, stressed, tired, energetic): ").strip().lower()
energy_level = input("What is your energy level? (high / low): ").strip().lower()

print("\n" + "-" * 45)
print(f"Hello, {user_name}! Here is your personalized daily advice:")

# --- Step 3: Conditional Logic for Advice ---
if mood == "happy":
    if energy_level == "high":
        print("Advice: You're bursting with positivity! Use this energy to tackle a creative project or help a friend.")
    else:
        print("Advice: Enjoy your peaceful, happy mood. Relax with a good book, music, or a favorite movie.")

elif mood == "sad":
    if energy_level == "high":
        print("Advice: Channel that extra energy into physical activity like going for a run or working out to clear your mind.")
    else:
        print("Advice: Be gentle with yourself today. Take rest, sip a warm drink, and take things step by step.")

elif mood == "stressed":
    if energy_level == "high":
        print("Advice: Break your tasks into smaller steps. Focus on finishing one high-priority item first!")
    else:
        print("Advice: Pause and practice deep breathing. Step away from work for 15 minutes to clear your head.")

elif mood == "tired":
    print("Advice: Listen to your body! Get some extra rest tonight and avoid overworking yourself.")

elif mood == "energetic":
    print("Advice: Great energy! Set an ambitious goal for today and work toward achieving it.")

else:
    # Default fallback for unlisted moods
    if energy_level == "high":
        print("Advice: You have great energy today! Put it toward something meaningful and exciting.")
    else:
        print("Advice: Take it easy today and make time for something you enjoy.")

print("=" * 45)