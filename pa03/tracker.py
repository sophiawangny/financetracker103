# offers the user the following options and makes calls to the Transaction class to update the database.

from transaction import Transaction



def process_choice(choice):

    if choice=='0':
        return
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    else:
        print("choice",choice,"not yet implemented")

    choice = input("> ")
    return(choice)



def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')