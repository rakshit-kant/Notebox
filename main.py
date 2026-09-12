from dataclasses import dataclass, asdict
import json


# Similar to a struct in C: defines a data structure for a note
@dataclass
class Note:
    title: str
    content: str


def print_ascii():
    print("""\n\n▓   ▓  ▓▓▓  ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓   ▓▓▓  ▓   ▓   
▓▓  ▓░▓ ░░▓  ░▓░░░▓░░░░░▓░░░▓ ▓ ░░▓  ▓ ▓ ░  
▓░▓ ▓░▓░ ░▓░  ▓░░░▓▓▓▓░░▓▓▓▓░░▓░ ░▓░  ▓ ░ ░ 
▓░░▓▓░▓░░ ▓░░ ▓░░ ▓░░░░ ▓░░░▓ ▓░░ ▓░░▓ ▓ ░  
▓░░ ▓░░▓▓▓ ░░ ▓░░ ▓▓▓▓▓░▓▓▓▓░░ ▓▓▓ ░▓ ░ ▓   
 ░░  ░░ ░░░ ░  ░░  ░░░░░ ░░░░ ░ ░░░ ░░ ░ ░  
  ░   ░  ░░░    ░   ░░░░░ ░░░░   ░░░  ░   ░ \n\n\n""")


def main_menu():
    print("""0. Exit the Program
1. Create a Note
2. See all Notes
3. Search a Note
4. Delete a Note
5. Edit a Note""")
    while True:
        try:
            choice = int(input("Enter a Number: "))
            break
        except ValueError:
            print("The Given Value was not a Number")

    match choice:
        case 0:
            return
        case 1:
            create_new_note()
        case 2:
            preview_notes()
        case 3:
            search_note()
        case 4:
            delete_note()
        case 5:
            edit_note()


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


def preview_notes():
    try:
        # Open the existing json file for reading existing notes without overwriting it
        with open("note_list.json", "r", encoding="utf-8") as f:
            note_list = json.load(f)

        # Cycle through each note and Print it
        for index, note in enumerate(note_list, start=1):
            print(f"\nNote {index}")
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")

    except FileNotFoundError:
        print("There are Currently No Notes")
        choice = input("Want to create notes [Y/n]: ").lower()

        if choice == "y" or choice == "yes":
            create_new_note()
        else:
            print("Okay, Be Productive!")


def search_note():
    try:
        # Open the existing json file for reading existing notes without overwriting it
        with open("note_list.json", "r", encoding="utf-8") as f:
            note_list = json.load(f)

        query = input("Enter Something to Search for: ").strip().lower()
        found = False

        for index, note in enumerate(note_list, start=1):
            title = note["title"].lower()
            content = note["content"].lower()

            if query in title or query in content:
                print(f"\nNote {index}")
                print(f"Title: {note['title']}")
                print(f"Content: {note['content']}")
                found = True

            if not found:
                print(f"No Notes Found containing: {query}")
    except FileNotFoundError:
        print("There are Currently No Notes")
        choice = input("Want to create notes [Y/n]: ").lower()

        if choice == "y" or choice == "yes":
            create_new_note()
        else:
            print("Okay, Be Productive!")


def main():
    print_ascii()
    main_menu()


if __name__ == "__main__":
    main()
