def get_valid_input(prompt):
    while True:
        person_input = input(prompt)
        try:
            person_input_valid = int(person_input)
            return person_input_valid
        except ValueError:
            print("Entered choice is NOT an integer...Please try again")