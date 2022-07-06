def main():
    for _ in range(int(input())):
        num_of_devs, skill_level = int(input()), [(key + 1, int(value)) for key, value in enumerate(input().split())]
        for _ in range(num_of_devs // 2):
            first_dev = skill_level.pop(0)
            second_dev = min(skill_level, key=lambda dev: abs(first_dev[1] - dev[1]))
            skill_level.remove(second_dev)
            print(first_dev[0], second_dev[0])
        print()


if __name__ == '__main__':
    main()
