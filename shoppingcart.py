shop_list = {}

def display_instructions():
    print('Welcome to your shopping list')
    print("To add an item to your list type 'Add Item'")
    print("To delete an item from your list type 'Remove Item'")
    print("To view your current list type 'View List'")
    print("To quit and view your completed list, type 'Quit'")
    response = input("What would you like to do? ")
    return response

def addItem(item):
    shop_list[item] = "food"

def deleteItem(item):
    del shop_list[item]

def showCurrentList(shop_list):
    if shop_list == {}:
        print('There is no list. Only Zuul')
    else:
        for k in shop_list.items():
            print('{}'.format(k))


while True:
    response = display_instructions()
    if response == 'Add Item':
        item = input('Which item? ')
        addItem(item)

    elif response == "Remove Item":
        item = input('Which item? ')
        try:
            deleteItem(item)
        except:
            print("That's not a thing. Stop it.")

    elif response == 'View List':
        showCurrentList(shop_list)



    else:
        response == 'Quit'
        showCurrentList(shop_list)
        break
