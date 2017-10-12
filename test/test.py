from dbtransfer import TestDB

def main():
    test = TestDB('dsn=test.db')
    test.insert()
    test.select(10)

if __name__ == '__main__':
    main()
