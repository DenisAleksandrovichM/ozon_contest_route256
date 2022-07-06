def main():
    for _ in range(int(input())):
        _, tasks = input(), input().split()
        completed_tasks, report_is_correct = set(), True
        completed_tasks.add(tasks[0])
        for num_of_task in range(1, len(tasks)):
            if tasks[num_of_task - 1] == tasks[num_of_task]:
                continue
            if tasks[num_of_task] in completed_tasks:
                report_is_correct = False
                break
            completed_tasks.add(tasks[num_of_task])
        print('YES' if report_is_correct else 'NO')


if __name__ == '__main__':
    main()
