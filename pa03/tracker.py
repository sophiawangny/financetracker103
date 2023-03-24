# offers the user the following options and makes calls to the Transaction class to update the database.

from transaction import Transaction

menu_options = '''Please select the number corresponding the command:
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date (MM-DD-YYYY)
8. summarize transactions by month (MM)
9. summarize transactions by year (YYYY)
10. summarize transactions by category
11. print this menu
'''

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
    print(menu_options)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('THE END')