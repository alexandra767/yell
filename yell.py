def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    #uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
