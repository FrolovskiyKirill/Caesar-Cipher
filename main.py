alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(text, shift_amount, direction):
  converted_text = ""
  for letter in text:
    position = alphabet.index(letter)
    if direction == 'encode':
      new_position = position + shift_amount
    elif direction == 'decode':
      new_position = position - shift_amount
    new_letter = alphabet[new_position]
    converted_text += new_letter
  print(f"The {direction}d text is {converted_text}")

ceasar(text=text, shift_amount=shift, direction=direction)