alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text,shift_key):
    chiper_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position+shift_key)%26
            chiper_text += alphabets[new_position]
        else:
            chiper_text+=char
    print(f"Text After Encryption {chiper_text}")

def decryption(chiper_text,shift_key):
    plain_text = ""
    for char in chiper_text:
        if char in chiper_text:
            position = alphabets.index(char)
            new_position = (position-shift_key)%26
            plain_text += alphabets[new_position]
        else:
            plain_text+=char
    print(f"Text After decryption {plain_text}")

wanna_end = False
while not wanna_end:
    what_to_do = input("Type 'encrypt' for Encryption,Type 'decrypt' for Decryption: \n")
    text = input("Type the Message: \n").lower()
    shift = int(input("Enter shift Key: \n"))
    if what_to_do == "encrypt":
        encryption(plain_text = text,shift_key = shift)
    else:
        decryption(chiper_text =  text,shift_key = shift)
    play_again = input("Type 'YES' to Continue and 'No' to Exist: \n")
    if play_again == "NO" or play_again == "no":
        wanna_end = True
        print("HAVE A NICE DAY!BYE...")
