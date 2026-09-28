location = input("Enter vacuum location (A/B): ").upper()
room_A = input("Enter Room A status (Dirty/Clean): ").capitalize()
room_B = input("Enter Room B status (Dirty/Clean): ").capitalize()


state = (location, room_A, room_B)

print("\nCurrent State:", state)

if state == ("A", "Dirty", "Dirty"):
    print("Action: Suck dirt from Room A")


elif state == ("A", "Dirty", "Clean"):
    print("Action: Suck dirt from Room A")

elif state == ("A", "Clean", "Dirty"):
    print("Action: Move Right to Room B")

elif state == ("A", "Clean", "Clean"):
    print("Action: Stop - Both rooms are clean")


elif state == ("B", "Dirty", "Dirty"):
    print("Action: Suck dirt from Room B")

elif state == ("B", "Dirty", "Clean"):
    print("Action: Move Left to Room A")

elif state == ("B", "Clean", "Dirty"):
    print("Action: Suck dirt from Room B")

elif state == ("B", "Clean", "Clean"):
    print("Action: Stop - Both rooms are clean")

else:
    print("Invalid input!")
