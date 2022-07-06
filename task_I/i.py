import heapq


def main():
    _, number_of_tasks = map(int, input().split())

    processors = {}
    free_processors = []
    for power_usage in input().split():
        processors[int(power_usage)] = 0
        free_processors.append(int(power_usage))

    total_power_usage = 0
    heapq.heapify(free_processors)
    queue = [list(map(int, input().split())) for _ in range(number_of_tasks)]

    sec = 0
    for task in queue:
        if not sec == 0:
            for key, value in processors.items():
                if value == 0:
                    continue
                new_value = max(value - (task[0] - sec), 0)
                if new_value == 0:
                    heapq.heappush(free_processors, key)
                processors[key] = new_value

        if len(free_processors) == 0:
            continue

        sec = task[0]
        free_processor = heapq.heappop(free_processors)
        processors[free_processor] = task[1]
        total_power_usage += (task[1] * free_processor)

    print(total_power_usage)


if __name__ == '__main__':
    main()
