from datetime import datetime


def main():
    for _ in range(int(input())):
        res = True
        segments = set()
        for _ in range(int(input())):
            if not res:
                input()
                continue

            segment = input().split('-')
            try:
                first_date, second_date = date_from_segment(segment)
            except ValueError:
                res = False
                continue

            if first_date > second_date:
                res = False
                continue

            res = all(check_segment(first_date, second_date, item) for item in segments)
            segments.add((first_date, second_date))
        print('YES' if res else 'NO')


def date_from_segment(segment):
    return datetime.strptime(segment[0], '%H:%M:%S'), datetime.strptime(segment[1], '%H:%M:%S')


def check_segment(d1, d2, item):
    return not (item[0] <= d1 <= item[1] or item[0] <= d2 <= item[1] or d1 <= item[0] <= d2 or d1 <= item[1] <= d2)


if __name__ == '__main__':
    main()
