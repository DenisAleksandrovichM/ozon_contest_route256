def main():
    for _ in range(int(input())):
        num_of_lines, num_of_chars = map(int, input().split())
        hexagon = [list(input()) for _ in range(num_of_lines)]
        used_letters, isValid = set(), True
        for line_index, line in enumerate(hexagon):
            for char_index, char in enumerate(line):
                if char in used_letters:
                    isValid = False
                    break
                if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    used_letters.add(char)
                    change_letter(hexagon, line_index, char_index, char, num_of_lines, num_of_chars)
            if not isValid:
                break
        print('YES' if isValid else 'NO')


def change_letter(hexagon, line_index, char_index, letter, num_of_lines, num_of_chars):
    if 0 <= line_index < num_of_lines and 0 <= char_index < num_of_chars and hexagon[line_index][char_index] == letter:
        hexagon[line_index][char_index] = '.'
        for pos in ((-1, -1), (-1, 1), (1, -1), (1, 1), (0, 2), (0, -2)):
            change_letter(hexagon, line_index + pos[0], char_index + pos[1], letter, num_of_lines, num_of_chars)


if __name__ == '__main__':
    main()