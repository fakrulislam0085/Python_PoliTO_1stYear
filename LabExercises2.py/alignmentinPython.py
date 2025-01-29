'''
Here's the basic idea behind aligning text in Python:

Left alignment(:<) : When you use left alignment, the text (or number) will be placed starting from the left side of the given width, 
and any extra space will be added on the right.

Right alignment(:>) : With right alignment, the text (or number) will be placed starting from the right side of the given width, 
and any extra space will be added on the left.

Center alignment(:^) : With center alignment, the text (or number) will be placed in the middle of the given width, 
and any extra space will be divided equally on both sides (if possible).

You can also specify the width of the string, i.e., how many characters wide the field should be.
'''

# Print with alignment
print(f"{'Rank':<5}{'Unicode':<12}{'Unicode Name':<20}{'Emoji'}")


#Right alignment (>):
print(f"{'Rank':>5}{'Unicode':>12}{'Unicode Name':>20}{'Emoji'}")


#Center alignment (^):
print(f"{'Rank':^5}{'Unicode':^12}{'Unicode Name':^25}{'Emoji'}")
