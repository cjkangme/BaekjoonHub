if __name__ == "__main__":
    formats = input()
    length = len(formats)
    format_dict = {"c": 26, "d": 10}
    answer = format_dict[formats[0]]
    for i in range(1, length):
        if formats[i] == formats[i-1]:
            answer *= format_dict[formats[i]] - 1
        else:
            answer *= format_dict[formats[i]]
    print(answer)