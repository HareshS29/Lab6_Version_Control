# Haresh Subramanian
def encode(pasword):
    newpassword = ''
    for i in pasword:
        i = int(i) + 3
        i = str(i)
        if len(str(i)) == 2:
            i = i[1]
        newpassword += str(i)
    return newpassword


def decode(password):
    int_list = ''
    for i in password:
        if int(i) > 2:
            int_list += str(int(i) - 3)
        else:
            int_list += str(int(i) + 7)
    return int_list


def main():
    print('1. Encode Password')
    print('2. Decode Password')


if __name__ == '__main__':
    user_input = 0
    while True:
        main()
        user_input = input('Choose an option: ')

        if user_input == '1':
            password = input("Input password to encode: ")
            print(encode(password))

        elif user_input == '2':
            encoded_password = input('Input password to decode')
            print(decode(encoded_password))
