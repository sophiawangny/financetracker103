"""offers the user the following options 
and makes calls to the Transaction class to update the database"""

from transaction import Transaction

MENU_OPTIONS = '''Please select the number to the command you would like:
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

"""takes in the user input"""
#sophia 
def process_choice(choice):
    transaction=Transaction()
    if choice=='0': #quit
        return
    if choice=='1': #show categories
        ctgries = transaction.select_all()
        for cat in ctgries:
            print(f"- {cat}")
    elif choice=='2': #add category
        name = input("name of category: ")
        desc = input("category description: ")
        ctgry = {'name':name, 'desc':desc}
        transaction.add_category(ctgry)
    elif choice=='3': #modify category
        print("Modify Category:")
        id_num = int(input("id: "))
        name = input("new name of category: ")
        desc = input("new category description: ")
        ctgry = {'name':name, 'desc':desc}
        transaction.update_category(id_num,ctgry)
    elif choice == '4': #show transactions
        transactions = transaction.get_transactions()
        print("Transactions:")
        for trans in transactions:
            print(f"- {trans['itemid']}: {trans['amount']} "
                    f"- {trans['category']} - {trans['date']} "
                    f"- {trans['description']}")
    elif choice == '5': #add transaction
        itemid = input("itemid: ")
        amount = input("Enter the amount: ")
        ctgry = input("Enter the category: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        description = input("Enter the transaction description: ")
        transaction.add_transaction(itemid, amount, ctgry, date, description)
    elif choice == '6': #delete transaction
        item_num = input("Enter the item number to delete: ")
        transaction.delete_transaction(item_num)
    elif choice=='7': #summarize transactions by date #sophia 
        date=input("Enter the date (MM-DD-YYYY):")
        summary = transaction.get_transactions_by_date(date)
        print(f"Transactions on {date}:")
        for ctgry, amount in summary.items():
            print(f"- {ctgry}: {amount}")
    elif choice == '8': #summarize transactions by month (MM)
        month = input("Enter the month (MM): ")
        summary = transaction.summarize_transactions_by_month(month)
        print(f"Transactions in {month}:")
        for ctgry, amount in summary.items():
            print(f"- {ctgry}: {amount}")
    elif choice == '9': #summarize transactions by year (YYYY)
        year = input("Enter the year (YYYY): ")
        summary = transaction.summarize_transactions_by_year(year)
        print(f"Transactions in {year}:")
        for ctgry, amount in summary.items():
            print(f"- {ctgry}: {amount}")
    elif choice == '10': #summarize transactions by category #sophia 
        ctgry = input("Enter the category: ")
        summary = transaction.get_transactions_by_category(ctgry)
        print(f"Transactions in '{ctgry}':")
        for date, amount in summary.items():
            print(f"- {date}: {amount}")
    elif choice=='11': #print this menu 
        print(MENU_OPTIONS)
    else:
        print("Invalid choice, try again")

#yalda 
def toplevel():
    ''' take in user choice '''
    print(MENU_OPTIONS)
    choice = input("> ")
    while choice !='0' :
        process_choice(choice)
    print('Thanks!')

toplevel()
        