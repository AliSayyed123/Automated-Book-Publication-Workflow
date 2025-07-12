# human_loop/edit_interface.py

def present_for_editing(spun_text: str):
    print("\n--- AI-Generated Chapter ---")
    print(spun_text)
    print("\nWould you like to (a)ccept, (e)dit or (r)eject this version?")
    choice = input("Choice: ").strip().lower()
    if choice == "e":
        print("Enter your revised version (end with '///'):")
        revised = []
        while True:
            line = input()
            if line.strip() == "///":
                break
            revised.append(line)
        return "\n".join(revised)
    elif choice == "r":
        return None
    return spun_text
