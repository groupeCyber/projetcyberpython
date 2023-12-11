from Class.Analyzer import Analyzer

if __name__ == '__main__':
    active = True
    while active:
        print('Choose an option : \n 1. Scan network \n 2. Display logs \n 3. Quit\n')
        choice = input()
        if choice == '1':
            interface = input('\nEnter the interface to use : ')
            range = input('\nEnter the number of requests to analyze : ')
            active = False
            analyzer = Analyzer(interface)
            analyzer.get_packet_data(int(range))
        elif choice == '2':
            with open('logs/logs.log', 'r') as logs_file:
                print(logs_file.read())
            active = False
        elif choice == '3':
            break
        else:
            print('Invalid choice')