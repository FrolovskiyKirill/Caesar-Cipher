alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(start_text, shift_amount, cipher_direction):
  converted_text = ""
  if cipher_direction == 'decode':
    shift_amount *= -1
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    converted_text += alphabet[new_position]
  print(f"The {cipher_direction}d text is {converted_text}")

ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)