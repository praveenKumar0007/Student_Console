def get_marks( subject ):
    while True:
        mark = input(f"Enter {subject} marks:")
        try:
            mark = int(mark)
            if (mark >= 0 and mark <= 100):
                return mark
            else:
                raise ValueError
        except ValueError:
            print(f"Input entered for {subject} subject is not within range of 0 to 100 or it is not an integer...Please try again")
