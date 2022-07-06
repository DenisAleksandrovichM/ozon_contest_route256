from collections import Counter


def main():
    num_of_users, pair_of_friends = map(int, input().split())
    users = {}.fromkeys(range(1, num_of_users + 1))

    for _ in range(pair_of_friends):
        pair = list(map(int, input().split()))
        for friend_index, friend in enumerate(pair):
            user_friends = [] if users[friend] is None else users[friend]
            user_friends.append(pair[friend_index - 1])
            users[friend] = user_friends

    for user_index in range(1, num_of_users + 1):
        if users[user_index] is None:
            print(0)
            continue

        friends = []
        for friend in users[user_index]:
            for friend_of_a_friend in users[friend]:
                if not (friend_of_a_friend == user_index or friend_of_a_friend in users[user_index]):
                    friends.append(friend_of_a_friend)
        if len(friends):
            print(*sorted(set(filter(lambda f: friends.count(f) == max(list(Counter(friends).values())), friends))))
        else:
            print(0)


if __name__ == '__main__':
    main()
