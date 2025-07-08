
def manage_contact_book():
    
    contact_book ={}
    
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Retrieve Contact")
        print("4. View All Contacts")
        print("5. Exit")
        
        user_choice = int(input("Enter your choice : "))
        
        if user_choice == 1:
            name = input("Enter your name : ").strip().title()
            
            if name in contact_book:
                print(f"Contact {name} is already exists.")
                continue
            
            phone_no = input("Enter your phone number : ")
            email = input("Enter your email : ")
                
            if '@' not in email or '.' not in email:
                print('Invalid email format.')
                continue


            contact_book[name] = {'phone number': phone_no, 'email':email}
            print(f"Contact {name} is added.")
    
            
        elif user_choice == 2:
            
            update_name = input("Input the name that you want to update ").strip().title()
            
            if update_name not in contact_book:
                print(f"Contact {update_name} not exist in contact book.")
                continue
            
            update_phone_no = input("Enter the new phone number : ")
            update_email = input("Enter the new email : ")
            
            if '@' not in update_email or '.' not in update_email:
                print("Invalid email fromat.")
                continue
            
            contact_book[update_name] = {'phone number' : update_phone_no, "email" : update_email }
            print(f"Contact {update_name} is updated.")
        
        elif user_choice == 3:
            retrieve_contact_name = input("Enter the name that you want to retreive : ").strip().title()
            
            if retrieve_contact_name not in contact_book:
                print(f"Contact {retrieve_contact_name} not exist in contact book.")
                continue
            info = contact_book[retrieve_contact_name]
            
            
            print(f"Name : {retrieve_contact_name}")
            print(f"Phone number : {info['phone number']}")
            print(f"Email : {info['email']}")
        
        elif user_choice == 4:
            
            if not contact_book:
                print("Notebook is empty.")
                continue
            
            for name, info in contact_book.items():
                print(f"Name : {name}")
                print(f"Phone number : {info['phone number']}")
                print(f"Email : {info['email']}")
        
        elif user_choice == 5:
            break

manage_contact_book()