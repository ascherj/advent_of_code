def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    list_1 = []
    list_2 = []

    for line in data:
        parts = line.split()
        list_1.append(int(parts[0]))
        list_2.append(int(parts[1]))

    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    distances = 0

    for i in range(len(sorted_list_1)):
        distances += abs(sorted_list_1[i] - sorted_list_2[i])

    print(distances)

if __name__ == "__main__":
    main()
