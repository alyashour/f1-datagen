from data_generator import generate_all

def main():
    data = generate_all()
    print(type(data))
    print(data)

if __name__ == '__main__':
    main()