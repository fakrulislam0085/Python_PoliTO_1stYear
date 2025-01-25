'''
Here's the basic idea behind aligning text in Python:
Left alignment: <
Right alignment: >
Center alignment: ^
You can also specify the width of the string, i.e., 
how many characters wide the field should be.
'''

# Print with alignment
print(f"{'Rank':<5}{'Unicode':<12}{'Unicode Name':<20}{'Emoji'}")


#Right alignment (>):
print(f"{'Rank':>5}{'Unicode':>12}{'Unicode Name':>20}{'Emoji'}")


#Center alignment (^):
print(f"{'Rank':^5}{'Unicode':^12}{'Unicode Name':^25}{'Emoji'}")
