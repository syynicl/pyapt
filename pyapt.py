try:
    # Import modules
    import os

    # Define variables
    inLoop = True
    
    # Choose an operation
    while inLoop:
        print('1: Update packages')
        print('2: Remove unused packages')
        print('3: Clean package cache')
        print('4: Remove a package(s)')
        print('5: Search for a package')
        print('6: View package details')
        inp = int(input('>>> '))
        # Update packages
        if inp == 1:
            print('Updating packages...')
            os.system('sudo apt update && sudo apt dist-upgrade')
            print('Done.')
        # Remove unused packages
        elif inp == 2:
            print('Removing unused packages...')
            os.system('sudo apt autoremove')
            print('Done.')
        # Clean package cache
        elif inp == 3:
            print('Cleaning package cache...')
            os.system('sudo apt autoclean')
            print('Done.')
        # Remove a package(s)
        elif inp == 4:
            print('Enter the name of the package(s) you want to remove.')
            inp = input('>>> ')
            os.system('sudo apt remove {}'.format(inp))
            print('Done.')
        # Search for a package
        elif inp == 5:
            print('Enter the name of the package(s) you want to search for.')
            inp = input('>>> ')
            os.system('apt search {}'.format(inp))
            print('Done.')
        # View details of a package
        elif inp == 6:
            print('Enter the name of the package(s) you want to view the details of.')
            inp = input('>>> ')
            os.system('apt show {}'.format(inp))
            print('Done.')

# Custom KeyboardInterrupt message
except KeyboardInterrupt:
    print('\nProgram stopped using Ctrl+C.')