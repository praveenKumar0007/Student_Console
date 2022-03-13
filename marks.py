from valid_input import get_valid_input
def get_marks( subject ):
    while True:
        mark = get_valid_input(f"Enter {subject} marks :")
        try:
            if (mark >= 0 and mark <= 100):
                return mark
            else:
                raise IndexError
        except IndexError:
            print(f"Entered input for {subject} subject is not within range of 0 to 100...Please try again")
