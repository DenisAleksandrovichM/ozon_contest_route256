def main():
    dictionary = [input()[::-1] for _ in range(int(input()))]
    dictionary.sort()
    for _ in range(int(input())):
        request = input()[::-1]
        dictionary.append(request)
        request_index = dictionary.index(request)
        dictionary.sort()
        # neighbors =

        # rhyme = ''
        # for char in request:

        # for end_index in (None, -1):
        #     isFound, rhyme = find_rhyme(request, dictionary, end_index)
        #     if isFound:
        #         break

        print(rhyme)

#
# def find_rhyme(request, dictionary, end_index):
#     res = {}.fromkeys(dictionary)
#     for word in dictionary:
#         if word == request:
#             continue
#         for




def find_rhyme(request, dictionary, end_index):
    i, isFound, rhyme = 0, False, ''
    while not isFound and i < len(request):
        suffix = request[i:]
        for word in dictionary:
            rhyme = word
            if request == word:
                continue
            if word.endswith(suffix, 0, end_index):
                isFound = True
                break
        i += 1
    return isFound, rhyme


if __name__ == '__main__':
    main()