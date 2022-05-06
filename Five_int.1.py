def main(): 
    counter = 1000 
    counter1 = 0
    counter2 = 0 
    counter3 = 0 
    counter4 = 0 
    counter5 = 0 
    while counter < 2000: 
        counter1 = counter 
        counter2 = counter + 1 
        counter3 = counter2 + 1 
        counter4 = counter3 + 1 
        counter5 = counter4 + 1
        print("{} {} {} {} {}".format(counter1, counter2, counter3, counter4, counter5))

if __name__ == "__main__":
    main()
