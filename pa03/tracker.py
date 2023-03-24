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

    if choice=='0': #quit
        return
    elif choice=='1': #show categories
        ctgries = transaction.select_all() 	 #calls the select_all method from Transaction 
        print("Categories:")
        for cat in ctgries:
            print(f"- {cat}")
    elif choice=='2': #add category
        name = input("name of category: ")
        desc = input("category description: ")
        ctgry = {'name':name, 'desc':desc}
        transaction.add(ctgry) 			#calls the add method from Transaction
    elif choice=='3': #modify category
        print("Modify Category:")
        id = int(input("id: "))
        name = input("new name of category: ")
        desc = input("new category description: ")
        ctgry = {'name':name, 'desc':desc}
<<<<<<< HEAD
        transaction.update(id,ctgry)		#calls the update method from Transaction 
    elif choice == '4': #show transactions 
    	transactions = transaction.get_transactions() 	#calls the get_transactions method from Transaction
        print("Transactions:")
        for transaction in transactions:
            print(f"- {transaction}")
    elif choice == "5": #add transaction 
        amount = input("Enter the amount: ")
        ctgry = input("Enter the category: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        description = input("Enter the transaction description: ")
        transaction.add_transaction(amount, ctgry, date, description)  #calls the add_transaction method from Transaction 
    elif choice == "6": #delete transaction
        item_num = input("Enter the item number to delete: ")
        transaction.delete_transaction(item_num)		#calls the delete_transaction method from Transaction
    elif choice=='7':      # summarize transactions by date
        date=input("Enter the date (MM-DD-YYYY):")
        summary = transaction.summarize_transactions_by_date(date) #Calls the summarize_transaction_by_date method from Transaction class 
        print(f"Transactions on {date}:")
        for ctgry, amount in summary.items():
            print(f"- {ctgry}: {amount}")
    elif choice == '8':
=======
        transaction.update(id,ctgry)


    elif choice=='7': #summarize transactions by date (MM-DD-YYYY)
        date=input("Enter the date (MM-DD-YYYY):")
        summary = transaction.summarize_transactions_by_date(date) #Calls the summarize_transaction_by_date method from Transaction class 
        print(f"Transactions on {date}:")
        for category, amount in summary.items():
            print(f"- {category}: {amount}")
    elif choice == '8': #summarize transactions by month (MM)
>>>>>>> 7731a0f4b4357a67b9a776c93e95926c11007c48
        month = input("Enter the month (YYYY-MM): ")
        summary = transaction.summarize_transactions_by_month(month) #Calls the summarize_transaction_by_month
        print(f"Transactions in {month}:")
        for category, amount in summary.items():
            print(f"- {category}: {amount}")
    elif choice == '9': #summarize transactions by year (YYYY)
        year = input("Enter the year (YYYY): ")
        summary = transaction.summarize_transactions_by_year(year) #Calls the summarize_transaction_by_year
        print(f"Transactions in {year}:")
        for category, amount in summary.items():
            print(f"- {category}: {amount}")
    elif choice == '10': #summarize transactions by category
        category = input("Enter the category: ")
        summary = transaction.summarize_transactions_by_category(category)
        print(f"Transactions in '{category}':")
        for date, amount in summary.items():
            print(f"- {date}: {amount}")
    elif choice=='11': #print this menu
        print(menu_options)

    else:
        print("Invalid choice, try again")



def toplevel():
    ''' take in user choice '''
    print(menu_options)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('Thanks!')


toplevel()


    




        