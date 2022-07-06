def check_password(password):
    patterns = {
        'upper_letters': ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', False],
        'lower_letters': ['abcdefghijklmnopqrstuvwxyz', False],
        'digits': ['1234567890', False],
        'vowels_letters': ['euioayEUIOAY', False],
        'consonant_letters': ['bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ', False]
    }

    isValid = True
    for key, value in patterns.items():
        value[1] = all(char not in value[0] for char in password)
        isValid = min(isValid, value[1])

    if isValid:
        print(password)
        return

    if patterns['digits'][1]:
        password += '1'
        patterns['digits'][1] = False

    if patterns['upper_letters'][1]:
        if patterns['vowels_letters'][1]:
            patterns['vowels_letters'][1] = False
            password += 'E'
        else:
            patterns['consonant_letters'][1] = False
            password += 'B'
        patterns['upper_letters'][1] = False

    if patterns['lower_letters'][1]:
        if patterns['vowels_letters'][1]:
            patterns['vowels_letters'][1] = False
            password += 'e'
        else:
            patterns['consonant_letters'][1] = False
            password += 'b'
        patterns['lower_letters'][1] = False

    if patterns['vowels_letters'][1]:
        patterns['vowels_letters'][1] = False
        password += 'e'

    if patterns['consonant_letters'][1]:
        patterns['consonant_letters'][1] = False
        password += 'b'

    print(password)


if __name__ == '__main__':
    for _ in range(int(input())):
        check_password(input())
