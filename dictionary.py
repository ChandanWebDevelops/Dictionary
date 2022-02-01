from PyDictionary import PyDictionary
from pyfiglet import figlet_format

app_name = "Dictionary"

print(figlet_format(app_name))

dictionary = PyDictionary()

using_app = True
print("Make sure that your internet is connected")
while using_app:

    text = input("\nType any word to know the meaning: ")
    meaning = dictionary.meaning(text)
    print("\n")
    if meaning:
        try:
            for i in meaning:
                print(f"{i} : {meaning[i]}")
            
            asking = input("\nDo you want to use it again (yes/no)? ")
            
            asking = asking.lower()

            if asking == 'yes' or asking == 'y':
                continue
            elif asking == 'no' or asking == 'n':
                break

        except Exception as e:
            break
    else:
        print("Error has been catched")
    

print("\nThank you for using this app")

# meaning = dictionary.meaning(text)



    # print(meaning[i][0])
    


