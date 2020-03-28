# Import the re module for matching regular expressions
import os
import re

#  Define working variables cc, wc, and sc for character, word and sentence counts
cc = 0
wc = 0
sc = 0

# Used handwritten paraghraph to develop and test the original code to be followed by reading files
#paragraph = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold."

# Load paragraph from provided text files, each one used separately
# filepath = os.path.join('.', 'raw_data', 'paragraph_1.txt')
filepath = os.path.join('.', 'raw_data', 'paragraph_2.txt')
file = open(filepath, 'r')
paragraph = file.read()

# Derive character and word counts using regular expressions
cc = len(re.sub("\s",'',paragraph))
words = re.split("\s", paragraph)
wc = len(words)

# Regular expression based split to identify all sentences and hence count them
sentences = re.split("(?<=[.!?]) +", paragraph)
sc = len(sentences)

# Formatted Approximate letter count (per word) and Average sentence length (in words)
average_letter_count = format(cc / wc, ",.1f")
average_sentence_length = format(wc / sc, ",.1f")


# Generate the report to the console
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Character Count: {cc}")
print(f"Approximate Word Count: {wc}")
print(f"Approximate Sentence Count: {sc}")
print(f"Average Letter Count: {average_letter_count}")
print(f"Average Sentence Length: {average_sentence_length}")
