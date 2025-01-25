# List of the top 10 emojis with their details
emoji_data = [
    (1, "U+1F602", "FACE WITH TEARS OF JOY", "😂"),
    (2, "U+2764", "HEAVY BLACK HEART", "❤"),
    (3, "U+1F60D", "SMILING FACE WITH HEART-EYES", "😍"),
    (4, "U+1F609", "WINKING FACE", "😉"),
    (5, "U+1F618", "FACE THROWING A KISS", "😘"),
    (6, "U+1F62D", "LOUDLY CRYING FACE", "😭"),
    (7, "U+1F621", "POUTING FACE", "😡"),
    (8, "U+1F609", "WINKING FACE", "😉"),
    (9, "U+1F614", "PENSIVE FACE", "😔"),
    (10, "U+1F60E", "SMILING FACE WITH SUNGLASSES", "😎")
]

# List of emojis that the user uses most frequently (you can change these emojis)
user_emojis = ["😂", "❤", "😍"]

# Print the header for the output table
print(f"{'Rank':<5}{'Unicode':<12}{'Unicode Name':<25}{'Emoji'}")
print("-" * 50)   #print '-' 50 times

# Loop through each emoji that the user uses
for emoji in user_emojis:
    # Search through the emoji_data list to find details about the emoji
    for rank, unicode_num, name, em in emoji_data:
        if em == emoji:  # If the emoji matches
            # Print the details in a neatly aligned format
            print(f"{rank:<5}{unicode_num:<12}{name:<25}{em}")
