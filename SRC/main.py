from SRC.util import PrintableDict
from data_generator import generate_all
from data_writer.db import populate as push_to_db

def main():
    data: PrintableDict = generate_all()
    push_to_db(data)
    print('done')

if __name__ == '__main__':
    main()