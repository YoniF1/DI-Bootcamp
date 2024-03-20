from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print('View an Item (V)')
    print('Add an Item (A)')
    print('Delete an Item (D)')
    print('Update an Item (U)')
    print('Show the Menu (S)')
    print('Type exit to stop program')

    choice = ''
    while choice != 'exit':
        choice = input('Choose: ')

        if choice == 'A':
            add_item_to_menu()
        elif choice == 'V':
            view_item()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        else:
            show_restaurant_menu()
    
    show_restaurant_menu()
        
def view_item():
    item_name = input('What is the item you would like to view?')

    item = MenuManager.get_by_name(item_name)
    print(f"The item is {item.name} and it costs {item.price}")

def add_item_to_menu():
    item_name = input('What is the new item?')
    item_price = int(input('What is the new item\'s price'))

    item = MenuItem(item_name, item_price)
    item.save()
    print("Item was added successfully")

def remove_item_from_menu():
    item_name = input('What is the item you want to remove?')
    item_price = int(input('What is the item\'s price'))

    try:
        item = MenuItem(item_name, item_price)
        item.delete()
        print("Item deleted")
    except:
        print("Error, item not deleted")

def update_item_from_menu():
    item_name = input('What is the item you want to update?')
    item_price = int(input('What is the item\'s price you want to update?'))

    new_item_name = input('What is the new name you want?')
    new_item_price = int(input('What is the new price for the item?'))

    try:
        item = MenuItem(item_name, item_price)
        item.update(new_item_name, new_item_price)
        print('Item updated')
    except:
        print("Error, item not updated")

def show_restaurant_menu():
    all_items = MenuManager.all()
    for item in all_items:
        print(f"{item[1]} costs {item[2]}")
    
show_user_menu()

    