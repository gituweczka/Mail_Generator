#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_content = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    guests = invited_names.readlines()
    for guest in guests:
        next_guest = guest.strip("\n")
        invitation = letter_content.replace("[name]", next_guest)
        new_letter = open(f"./Output/ReadyToSend/{next_guest}.txt", mode="w")
        new_letter.write(invitation)
        new_letter.close()





