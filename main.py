
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def ceasar(start_text, shift_amount, cipher_direction):
  converted_text = ""
  if cipher_direction == 'decode':
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      converted_text += char
    elif char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      converted_text += alphabet[new_position]
  print(f"The {cipher_direction}d text is {converted_text}")

should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % len(alphabet)
  
  ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to restart, type 'no' if you want to exit.\n")

  if restart == "no":
    should_continue = False
    print("Goodbye!")