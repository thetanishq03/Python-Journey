#MINIPROJECT: SHOPPING CART SYSTEM
list = []
while True:
    option = int(input("""1.Add Item\n2.Remove Item\n3.View Cart\n4.Exit\nEnter your choice: """))
    if option == 1:
        add_item = str(input("""Add item which you wish.\nEnter item: """))
        list.append(add_item)
    elif option == 2:
        remove_item = str(input("""Remove item which you wish.\nEnter item: """))
        list.remove(remove_item)
    elif option == 3:
        print(f"""List you made:\nList: {list}""")
    elif option == 4:
        print("You exiting!")
        break