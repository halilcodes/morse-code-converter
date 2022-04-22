# import morse_list
from morse_list import morse_list

# get input from user
original_text = input("Enter the text to convert: ").lower().strip()
original_text = original_text.replace(" ", "-")


# split input
# pass one by one and convert to morse code
output_list = [morse_list[char] for char in original_text]

# show output
output = "".join(output_list)
print(f"output: {output}")

