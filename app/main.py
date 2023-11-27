from Class.Scanner import Scanner

if __name__ == '__main__':
    scanner = Scanner('eth0')
    scan  = scanner.scan()
    for packet in scan:
            print(packet)