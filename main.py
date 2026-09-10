from dataclasses import dataclass, asdict
import json


# Similar to a struct in C: defines a data structure for a note
@dataclass
class Note:
    title: str
    content: str


def print_ascii():
    print("""▓   ▓  ▓▓▓  ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓   ▓▓▓  ▓   ▓   
▓▓  ▓░▓ ░░▓  ░▓░░░▓░░░░░▓░░░▓ ▓ ░░▓  ▓ ▓ ░  
▓░▓ ▓░▓░ ░▓░  ▓░░░▓▓▓▓░░▓▓▓▓░░▓░ ░▓░  ▓ ░ ░ 
▓░░▓▓░▓░░ ▓░░ ▓░░ ▓░░░░ ▓░░░▓ ▓░░ ▓░░▓ ▓ ░  
▓░░ ▓░░▓▓▓ ░░ ▓░░ ▓▓▓▓▓░▓▓▓▓░░ ▓▓▓ ░▓ ░ ▓   
 ░░  ░░ ░░░ ░  ░░  ░░░░░ ░░░░ ░ ░░░ ░░ ░ ░  
  ░   ░  ░░░    ░   ░░░░░ ░░░░   ░░░  ░   ░ \n\n""")


def main_menu():
    print("""1. Create a Note
2. See all Notes
3. Search a Note
4. Delete a Note
5. Edit a Note""")
    choice = int(input("Enter a Number: "))


def create_new_note():
    # Create a Note object using values entered by the user
    new_note = Note(
        title=input("Enter the Title of the Note: "),
        content=input("Enter the Content of the Note: "),
    )

    try:
        # open the existing json file for reading without overwriting it
        with open("note_list.json", "r", encoding="utf-8") as f:
            note_list = json.load(f)
    except FileNotFoundError:
        # if the json file doesn't exist, start with an empty list
        note_list = []

    # Convert the Note dataclass to a dictionary and append it to the list
    note_list.append(asdict(new_note))

    # write the updated list of notes back to the json file
    with open("note_list.json", "w", encoding="utf-8") as f:
        json.dump(note_list, f, indent=4)


def main():
    print_ascii()
    main_menu()
    create_new_note()


if __name__ == "__main__":
    main()
