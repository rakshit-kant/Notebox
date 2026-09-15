from dataclasses import dataclass, asdict
import json


# Similar to a struct in C: defines a data structure for a note
@dataclass
class Note:
    title: str
    content: str


FILE_NAME = "note_list.json"


def print_ascii():
    print("""


▓   ▓  ▓▓▓  ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓   ▓▓▓  ▓   ▓
▓▓  ▓░▓ ░░▓  ░▓░░░▓░░░░░▓░░░▓ ▓ ░░▓  ▓ ▓ ░
▓░▓ ▓░▓░ ░▓░  ▓░░░▓▓▓▓░░▓▓▓▓░░▓░ ░▓░  ▓ ░ ░
▓░░▓▓░▓░░ ▓░░ ▓░░ ▓░░░░ ▓░░░▓ ▓░░ ▓░░▓ ▓ ░
▓░░ ▓░░▓▓▓ ░░ ▓░░ ▓▓▓▓▓░▓▓▓▓░░ ▓▓▓ ░▓ ░ ▓
 ░░  ░░ ░░░ ░  ░░  ░░░░░ ░░░░ ░ ░░░ ░░ ░ ░
  ░   ░  ░░░    ░   ░░░░░ ░░░░   ░░░  ░   ░


""")


def load_notes():
    """Load notes from the JSON file."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("The notes file contains invalid JSON.")
        return []


def save_notes(note_list):
    """Save the current notes to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(note_list, f, indent=4)


def main_menu():
    while True:
        print("""
0. Exit the Program
1. Create a Note
2. See all Notes
3. Search a Note
4. Delete a Note
5. Edit a Note
""")

        while True:
            try:
                choice = int(input("Enter a Number: "))
                break
            except ValueError:
                print("The Given Value was not a Number")

        match choice:
            case 0:
                print("Goodbye!")
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

            case _:
                print("Invalid Choice. Please select a number from 0 to 5.")


def create_new_note():
    """Create a new note and save it."""
    print("\n--- Create a New Note ---")

    title = input("Enter the Title of the Note: ").strip()
    content = input("Enter the Content of the Note: ").strip()

    # Don't allow completely empty notes
    if not title and not content:
        print("A note cannot be completely empty.")
        return

    new_note = Note(title=title, content=content)

    note_list = load_notes()

    # Convert the Note dataclass to a dictionary
    # and add it to the list
    note_list.append(asdict(new_note))

    save_notes(note_list)

    print("Note Created Successfully!")


def preview_notes():
    """Display all notes."""
    note_list = load_notes()

    if not note_list:
        print("\nThere are Currently No Notes.")

        choice = input("Want to create a note? [Y/n]: ").strip().lower()

        if choice in ("y", "yes", ""):
            create_new_note()
        else:
            print("Okay, Be Productive!")

        return

    print("\n--- All Notes ---")

    for index, note in enumerate(note_list, start=1):
        print(f"""
Note {index}
Title: {note["title"]}
Content: {note["content"]}
""")


def search_note():
    """Search notes by title or content and return matching indexes."""
    note_list = load_notes()

    if not note_list:
        print("\nThere are Currently No Notes.")
        return []

    query = input("Enter Something to Search for: ").strip().lower()

    if not query:
        print("Search cannot be empty.")
        return []

    found_notes = []

    # Search through every note
    for index, note in enumerate(note_list):
        title = note["title"].lower()
        content = note["content"].lower()

        if query in title or query in content:
            found_notes.append(index)

    if not found_notes:
        print(f"No Notes Found containing: {query}")
        return []

    print(f"\nFound {len(found_notes)} note(s):")

    for index in found_notes:
        note = note_list[index]

        print(f"""
Note {index + 1}
Title: {note["title"]}
Content: {note["content"]}
""")

    return found_notes


def choose_note(note_indexes, action):
    """
    Ask the user which note they want to perform an action on.
    Returns the actual index in note_list.
    """

    if len(note_indexes) == 1:
        return note_indexes[0]

    while True:
        try:
            choice = int(input(f"Enter the Note Number you want to {action}: ")) - 1

            if choice in note_indexes:
                return choice

            print("Please select one of the displayed note numbers.")

        except ValueError:
            print("The Given Value was not a Number")


def delete_note():
    """Search for and delete a note."""
    print("\n--- Delete a Note ---")

    found_notes = search_note()

    if not found_notes:
        return

    note_list = load_notes()

    index = choose_note(found_notes, "delete")

    deleted_note = note_list.pop(index)

    save_notes(note_list)

    print(f'\nNote "{deleted_note["title"]}" deleted successfully!')


def edit_note():
    """Search for and edit a note."""
    print("\n--- Edit a Note ---")

    found_notes = search_note()

    if not found_notes:
        return

    note_list = load_notes()

    index = choose_note(found_notes, "edit")

    note = note_list[index]

    print("\n--- Current Note ---")
    print(f"Title: {note['title']}")
    print(f"Content: {note['content']}")

    print("\nPress Enter without typing anything to keep the current value.")

    new_title = input(f"New Title [{note['title']}]: ").strip()

    new_content = input(f"New Content [{note['content']}]: ").strip()

    # Keep old values if the user presses Enter
    if new_title:
        note["title"] = new_title

    if new_content:
        note["content"] = new_content

    save_notes(note_list)

    print("\nNote Edited Successfully!")


def main():
    print_ascii()
    main_menu()


if __name__ == "__main__":
    main()
