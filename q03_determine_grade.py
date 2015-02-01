x = 1
while x != 0:

    score = (input("Enter score: "))

    if score.isdigit():
        score = int(score)
        if 70 <= score <= 100:
            print("A")
        elif 60 <= score < 70:
            print("B")
        elif 55 <= score < 60:
            print("C")
        elif 50 <= score < 55:
            print("D")
        elif 45 <= score < 50:
            print("E")
        elif 35 <= score < 45:
            print("S")
        elif 0 <= score < 35:
            print("U")

    else:
        print("key in positive integer")
