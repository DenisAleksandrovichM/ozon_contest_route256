def main():
    num_of_users, num_of_requests = map(int, input().split())
    notifications = {}
    request_number = 0
    for i in range(num_of_requests):
        request_type, user_id = input().split()
        if request_type == '1':
            request_number += 1
            notifications[user_id] = request_number
        else:
            print(max(notifications.get(user_id, 0), notifications.get('0', 0)))


if __name__ == '__main__':
    main()
