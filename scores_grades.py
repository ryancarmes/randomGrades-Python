def random_number (number_scores):
    import random
    for x in range (0, number_scores):
        random_number = random.randint(60, 100)
        if random_number <= 59:
            print "Score: " + str(random_number) + "; Your grade is F"
        elif random_number > 59 and random_number < 70:
            print "Score: " + str(random_number) + "; Your grade is D"
        elif random_number > 69 and  random_number < 80:
            print "Score: " + str(random_number) + "; Your grade is C"
        elif random_number > 79 and  random_number < 90:
            print "Score: " + str(random_number) + "; Your grade is B"
        elif random_number > 89 and  random_number < 101:
            print "Score: " + str(random_number) + "; Your grade is A"
    print "End of the program. Bye!"
random_number(10)
