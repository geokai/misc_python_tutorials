"""
contacts02.py
This program allows me to manage my contacts.
"""

friends = []

def main():
    
    # friends = []

    for item in range(2):
        print("Contact manager")
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        friends.append([name, phone, email])

    # for i in range(len(friends)):
    #     print("Contact info")
    #     for j in range(len(friends[i])):
    #         print(friends[i][j])

    for i, _ in enumerate(friends):
        print("Contact info")
        for x, _ in enumerate(friends[i]):
            print(friends[i][x])


if __name__ == "__main__":
    main()
