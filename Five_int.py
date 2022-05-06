def main():
    for counter1 in range(1000, 2001, 5):
        # Values / Process
        counter1 = counter1
        counter2 = counter1 + 1
        counter3 = counter2 + 1
        counter4 = counter3 + 1
        counter5 = counter4 + 1

        print(counter1, end=" ")

        if counter1 < 2000:
            print(counter2, end=" ")
            print(counter3, end=" ")
            print(counter4, end=" ")
            print(counter5, end=" ")
            print("")
            if counter1 == 2000:
                break


if __name__ == "__main__":
    main()
