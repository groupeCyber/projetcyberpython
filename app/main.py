import logging
from Class.Analyzer import Analyzer
from logging.handlers import RotatingFileHandler

if __name__ == '__main__':
    active = True
    my_handler = RotatingFileHandler('./logs/logs.log', mode='a', maxBytes=10000000, backupCount=5, encoding=None, delay=0)
    my_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
    my_handler.setLevel(logging.INFO)
    logger = logging.getLogger('global')
    logger.setLevel(logging.INFO)
    logger.addHandler(my_handler)
    while active:
        logger.info('Starting IDS')
        print('Choose an option : \n 1. Scan network \n 2. Display logs \n 3. Quit\n')
        choice = input()
        if choice == '1':
            interface = input('\nEnter the interface to use : ')
            range = input('\nEnter the number of requests to analyze : ')
            token = input('\nEnter your Brevo (Sendinblue) API token : ')
            email = input('\nEnter the email address to send alerts to : ')
            active = False
            logger.info(f'Starting IDS on {interface} with interval of {range} packet')
            analyzer = Analyzer(interface, token, email)
            analyzer.get_packet_data(int(range))
        elif choice == '2':
            with open('logs/logs.log', 'r') as logs_file:
                print(logs_file.read())
            active = False
        elif choice == '3':
            break
        else:
            print('Invalid choice')