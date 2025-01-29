# Exercise 02.2.4
# Popular emojis

# Let's say that my most popular emoji are the following:
" 👍 🙂 😲 "

# To get the Unicode value you can use the ord() function
# ord('👍') --> 128077
# In Unicode tables usually the expressed value is in base 16
# which can be received through hex()
# hex(128077) --> '0x1f44d'
# or directly: hex(ord('👍')) --> '0x1f44d'

emoji1 = '👍'
rank1 = 4 # from https://home.unicode.org/emoji/emoji-frequency/
unicode1 = '1F44D' # from https://unicode-table.com/en/1F44D/
name1 = 'Thumbs Up Sign'

emoji2 = '🙂'
rank2 = 28 # from https://home.unicode.org/emoji/emoji-frequency/
unicode2 = '1F642' # from https://unicode-table.com/en/1F642/
name2 = 'Slightly Smiling Face'

emoji3 = '😲'
rank3 = 111 # from https://home.unicode.org/emoji/emoji-frequency/
unicode3 = '1F632' # from https://unicode-table.com/en/1F632/
name3 = 'Astonished Face'

print(f"{'Emoji':<15}{'Position':<15}{'Number':<15}{'Name':<15}")
print(f"{emoji1:<14}{rank1:<15}{unicode1:<15}{name1:<15}")

print(f"{emoji2:<14}{rank2:<15}{unicode2:<15}{name2:<15}")

print(f"{emoji3:<14}{rank3:<15}{unicode3:<15}{name3:<15}")

# Note: if you read more in depth the cited article in the text, in the bottom part it referes to this document
# https://docs.google.com/spreadsheets/d/1Zs13WJYdZL1pNZP0dCIXkWau_tZOjK3mmJz0KNq4I30/edit#gid=196891844
# which contains in tabular form all the needed informations!
# Reading until the end is always helpful...
