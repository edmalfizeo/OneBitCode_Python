from Blog import show_menu, create_user, create_post, show_all

while True:
    choice = show_menu()
    if choice == 1:
        create_user()
    elif choice == 2:
        create_post()
    elif choice == 3:
        show_all()
    elif choice == 4:
        break
    else:
        print('Invalid choice!')