#This functill will read from the user entered text file and try to decode the message based off the given
#"Answer Key" which is the Key.txt file. Then it will print out the decoded message.
def DecodeMessage(msg):
    print("\nDecode the message\n")

    #Read from the text file:
    with open("Key.txt", "r") as f:
        lines = f.readlines()

    #Create a dictionary to store the letter/symbol pair
    keys = {}

    #loop through the key.txt file and split based on the identifier to store the information as a key,value pair
    for l in lines:
        symbol, letter = l.strip(). split(" = ")
        keys[symbol] = letter

    #Read the coded message
    with open(msg, "r") as file:
        for line in file:
            code = line.split()

            for codes in code:
                if codes in keys:
                    print(keys[codes], end="")
                else:
                    print(codes, end="")

            print()


#This function will take what the unser entered, a tect file they want to encode, and compare it to the "answer key"  and then
# print out the uncoded message.        
def EncodeMessage(msg):
    print("\nEncode a message\n")

    #Read from the text file:
    with open("Key.txt", "r") as file:
        content = file.readlines()

    #Dictionary
    keys = {}

    #loop through the key.txt file and split based on the identifier to store the information as a key,value pair
    for line in content:
        if not line.strip() or " = " not in line:
            print("Error reading 'Key.txt' file")
            continue
        else:
            symbol, letter = line.strip().split(" = ")
            keys[letter] = symbol

    #Encode the message
    with open(msg, "r") as file:
        for line in file:
            codes = line.split()

            for code in codes:
                if code in keys:
                    print(keys[code], end="")    
                else:
                    print(code, end="")

            print()



def main():

    menu = "\n1.Decode\n2.Encode\n3.Exit"

    print("Welcome\n You can encode or decode a message here using text files!")
    print(menu)
    choice = int(input("\nEnter in a choice based off the menu:"))

    if choice == 1:
        print("You selected 'Encode Message'")

        textFile = input("\nEnter the name of the text file:")
        textFile = textFile + ".txt"

        DecodeMessage(textFile)

    elif choice == 2:

        print("You selected 'Decode Message'")

        textFile = input("\nEnter the text file you want to encode:")
        textFile = textFile + ".txt"

        EncodeMessage(textFile)





main()