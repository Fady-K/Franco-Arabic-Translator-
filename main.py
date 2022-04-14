# Program Name: Franco Arab Translator
# Author: Fady Kamal Ibrahim
# Program Description: This will help to Translate From Franco To Arabic
# Last Modification Date: 4/13/2022
# Purpose: Trying To Help People Struggling With Franco Letters
################################################################

# program initial status
message = None
choice = None
program_running = True
#in slicing remove one from the last index within the pracets
# Dictionary of letters
letters = {
    'A': u'ا',
    'B': u'ب',
    'C': u'س',
    'D': u'د',
    'E': u'ي',
    'F': u'ف',
    'G': u'ج',
    'H': u'ه',
    'I': u'ي',
    'J': u'ج',
    'K': u'ك',
    'L': u'ل',
    'M': u'م',
    'N': u'ن',
    'O': u'و',
    'P': u'ب',
    'Q': u'ق',
    'R': u'ر',
    'S': u'س',
    'T': u'ت',
    'W': u'و',
    'X': u'س',
    'Y': u'ي',
    'Z': u'ز',
    '2': u'ئ',
    '3': u'ع',
    '4': u'ش',
    '5': u'خ',
    '6': u'ط',
    '8': u'ق',
    '9': u'ص',
    '7': u'ح',
    'KH': u'خ',
    'TH': u'ث',
    'T`': u'ث',
    '$': u'ش',
    'OO': u'و',
    'OU': u'و',
    'EE': u'ي',
    'EI': u'ي',
    'AI': u'ي',
    'AL': u'ال',
    'D\'': u'ذ',
    '6\'': u'ظ',
    'GH': u'غ',
    '‘7': u'خ',
    'LL': u'ل',
}
#####################
# Reversed Dictionary for converting Arabic speach into arabic
reversed_letters = {
    'ا': 'A',
    'ب': 'B',
    'ت': 'T',
    'ث': 'C',
    'ج': 'J',
    'ح': '7',
    'خ': '5',
    'د': 'D',
    'ذ': 'D\'',
    'ر': 'R',
    'ز': 'Z',
    'س': 'S',
    'ش': '4',
    'ص': '9',
    'ض': 'D',
    'ط': '6',
    'ظ': 'Z',
    'ع': '3',
    'غ': 'GH',
    'ف': 'F',
    'ق': 'Q',
    'ك': 'K',
    'ل': 'L',
    'م': 'M',
    'ن': 'N',
    'ه': 'H',
    'و': 'W',
    'ي': 'Y',
    'ة': 'H',
    'ال': 'AL',
    'أ': 'A',
    'إ': 'E',
    'ى': 'A',
}

#########################
# Display Function
def Display(isFirstTime):
    global choice
    if isFirstTime:
        print(f"{'#' * 20}")
        print(f"!!Welcome To Franco Arab Translator!!")
        print(f"{'#' * 20}")
        print(f"Program Name: Franco Arab Translator\nAuthor: Fady Kamal Ibrahim\nProgram Description: This will help to Translate From Franco To Arabic\nLast Modification Date: 4/13/2022\nPurpose: Trying To Help People Struggling With Franco Letters")
        print(f"{'#' * 20}")
    print("1- translate from franco to arabic\n2- translate from arabic to franco\n3- Exit".title())
    choice = input("What Do You Want To Do?: ")
    return choice



########################
# Handle Twos Function  (To Handle Famous Combination comprised of two letters)
def Translate_To_Franco(letters):
    global message
    # take th message from the user
    message = input("Enter The Message You Want To Translate: ").upper()
    # replace any combination of the Following with it's Corresponding
    twos = ['KH', 'TH', 'T`', 'OO', 'OU', 'EE', 'EI', 'AI', 'AL', 'D\'', '6\'', 'GH', '‘7', 'LL']
    for item in twos:
        if item in message:
            message = message.replace(item, letters.get(item))
        else:
            continue

    # handle single letters
    for i in range(len(message)):
        message = list(message)
        Corresponding = letters.get(message[i])
        if Corresponding == None: # not in the dictionary
            continue
        else:
            message[i] = Corresponding
    # return the modified message to handle single letters
    message = "".join(message)
    print(f"{'#' * 20}")
    print(f"Translated Message: {message}")
    print(f"{'#' * 20}")

def Translate_To_Arabic(letters):

    global message
    # take th message from the user
    message = input("Enter The Message You Want To Translate: ").upper()
    # replace any combination of the Following with it's Corresponding
    twos = ['ال']
    for item in twos:
        if item in message:
            message = message.replace(item, letters.get(item))
        else:
            continue

    # handle single letters
    for i in range(len(message)):
        message = list(message)
        Corresponding = letters.get(message[i])
        if Corresponding == None: # not in the dictionary
            continue
        else:
            message[i] = Corresponding
    # return the modifed message to handle single letters
    message = "".join(message)
    print(f"{'#' * 20}")
    print(f"Translated Message: {message}")
    print(f"{'#' * 20}")

# program
Display(True)
while program_running:
    if choice == "1":
        Translate_To_Franco(letters)

    elif choice == "2":
        Translate_To_Arabic(reversed_letters)
    elif choice == "3":
        program_running = False
        break
    else:
        print(f"{'#' * 20}")
        print("!!invalid!!".upper())
        print(f"{'#' * 20}")
    Display(False)
