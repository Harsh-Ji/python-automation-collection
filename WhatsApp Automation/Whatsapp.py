import pywhatkit

# Send a WhatsApp Message to a Contact instantly
pywhatkit.sendwhatmsg_instantly("+911234567890", "Hi!\nHow are you?\nthis is an automated message...")

# Send a WhatsApp Message to a Contact at 11:02 PM and 15 sec
pywhatkit.sendwhatmsg("+911234567890", "Hi !\nHow are you?",23,2,15)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+911234567890", "Hello ", 22, 58, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")
