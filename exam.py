def is_vowel(message):
    if (message=='A' or message=='a' or message=='E' or message=='e' or message=='I' or message=='i' or message=='O' or message=='o' or message=='U' or message=='u'):
        print('True')
    elif (message!='A' or message!='a' or message!='E' or message!='e' or message!='I' or message!='i' or message!='O' or message!='o' or message!='U' or message!='u'):
        print('False')

print("Enter a single character and I determine if it is a vowel.")
message=input()
if len(message)>1:
    print("None")
else:
    is_vowel(message)
