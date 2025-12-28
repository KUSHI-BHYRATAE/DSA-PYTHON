shopping = []

while True:
    choice = input("Enter what you want to do (add, remove, show, quit): ")

    if choice == "add":
        item = input("Enter item name: ")
        shopping.append(item)

    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in shopping:
            shopping.remove(item)
        else:
            print("Item not found.")

    elif choice == "show":
        print(shopping)

    elif choice == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")

    
  
