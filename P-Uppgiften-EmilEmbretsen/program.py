from candidate import Candidate


def read_candidates_from_file(file_name):
    """
    Reads all lines from file_name and creates a candidate for each candidate in the file.
    Returns a dictionary with the candidates.
    """
    candidates_dict = dict()
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(";")
            candidates_dict[parts[0]] = Candidate(parts[0], int(parts[1]), parts[2],
                                                  float(parts[3]), int(parts[4]), float(parts[5]),
                                                  int(parts[6]), float(parts[7]))
    return candidates_dict


def get_form_input(prompt_string):
    """
    The user's response is returned as an integer between 0 and 5,
    where the prompt string is used to communicate what the user inputs.
    """
    correct_input = False
    while not correct_input:
        try:
            answer = int(input(prompt_string).strip())
            if 0 <= answer <= 5:
                correct_input = True
                return answer
            else:
                print("Input must be a whole number between 0 and 5.")
        except ValueError:
            print("Input most be a whole number.")


def get_gender_input(prompt_string):
    """
    The user's response is returned as either 'M', 'F' or 'B',
    with the prompt string communicating what the user inputs.
    """
    correct_input = False
    while not correct_input:
        answer = str(input(prompt_string)).upper().strip()
        if answer == "M" or answer == "F" or answer == "B":
            return answer
        else:
            print("Answer only with 'M', 'F' or 'B'.")


def present_form():
    """
    Presents the form, takes user input, and returns a list of form responses.
    """
    gender = get_gender_input("What gender would you prefer? Male (M), Female (F) or Both (B):")
    print("Grade from 0 to 5 how much you value each of these attributes")
    beauty = get_form_input("Beauty:")
    intelligence = get_form_input("Intelligence:")
    humor = get_form_input("Humor:")
    wealth = get_form_input("Wealth:")
    education = get_form_input("Education:")

    form_answers = [gender, beauty, intelligence, humor, wealth, education]

    return form_answers


def remove_candidates_of_wrong_gender(form_answers, candidates_dict):
    """
    Removes all candidates of gender that do not adhere to the client's
    preference.
    """
    candidates_to_remove = []
    if form_answers[0] != "B":
        for candidate in candidates_dict:
            if candidates_dict[candidate].gender != form_answers[0]:
                candidates_to_remove.append(candidate)
    for candidate in candidates_to_remove:
        del candidates_dict[candidate]
    return candidates_dict


def grade_attribute(candidate, candidates_dict, attribute):
    """
    Calculates the normalized score for a specific attribute.
    """
    candidate_attribute = getattr(candidate, attribute)
    highest_score = candidate_attribute
    for person in candidates_dict:
        if getattr(candidates_dict[person], attribute) > highest_score:
            highest_score = getattr(candidates_dict[person], attribute)
    try:
        score = candidate_attribute / highest_score
    except ZeroDivisionError:
        score = 0
    return score


def grade_candidate(candidate, candidates_dict, form_answers):
    """
    Calculates the score for the candidate using form responses and returns the score.
    """
    beauty_score = grade_attribute(candidate, candidates_dict, "beauty") * form_answers[1]
    intelligence_score = grade_attribute(candidate, candidates_dict, "intelligence") * form_answers[2]
    humor_score = grade_attribute(candidate, candidates_dict, "humor") * form_answers[3]
    wealth_score = grade_attribute(candidate, candidates_dict, "wealth") * form_answers[4]
    education_score = grade_attribute(candidate, candidates_dict, "education") * form_answers[5]

    grade = round(beauty_score + intelligence_score + humor_score + wealth_score + education_score, 2)
    return grade


def grade_all_candidates(candidates_dict, form_answers):
    """
    Uses the 'grade_candidate' function to grade all candidates.
    Returns dictionary with all candidates graded.
    """
    for candidate in candidates_dict:
        candidates_dict[candidate].grade = grade_candidate(candidates_dict[candidate], candidates_dict, form_answers)
    return candidates_dict


def sort_candidates(candidates_dict):
    """
    Creates a sorted dictionary with the 10 highest rated candidates.
    This code was created using the same method as described in this FreeCodeCamp
    article: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
    """
    sorted_candidates_by_grade = sorted(candidates_dict.items(), key=lambda x: x[1].grade, reverse=True)
    while len(sorted_candidates_by_grade) > 10:
        sorted_candidates_by_grade.pop()
    converted_dict = dict(sorted_candidates_by_grade)

    return converted_dict


def present_top_10_candidates(top_10_candidates_dict):
    """
    Presents the 10 highest graded candidates.
    """
    print("___________________")
    print("Here are the 10 best candidates for you!")
    print()
    rank = 1
    for candidate in top_10_candidates_dict:
        print(f"{rank}.")
        print(str(top_10_candidates_dict[candidate]))
        print()
        rank += 1


def choose_candidate(top_10_candidates_dict):
    """
    Asks the client to choose a candidate and returns the chosen candidate.
    """
    successful_input = False
    while not successful_input:
        choice = input("Enter the name of the client you'd like to choose:").strip()
        for candidate in top_10_candidates_dict:
            if choice.lower() == candidate.lower():
                chosen_candidate = top_10_candidates_dict[candidate]
                return chosen_candidate
        if not successful_input:
            print("The candidate name you entered is not in the list of top candidates.")
            print("Please try again.")


def main():
    """
    Runs the program.
    """
    print("Welcome to the candidate-intermediation program!")
    print("After answering some questions about your preferences, "
          "you will be presented with a list of our top 10 candidates for you "
          "to choose from.")
    print("___________________")
    candidates_dict = read_candidates_from_file("candidates.txt")
    form_answers = present_form()
    candidates_dict = remove_candidates_of_wrong_gender(form_answers, candidates_dict)
    candidates_dict = grade_all_candidates(candidates_dict, form_answers)
    top_10_candidates_dict = sort_candidates(candidates_dict)
    present_top_10_candidates(top_10_candidates_dict)
    chosen_candidate = choose_candidate(top_10_candidates_dict)

    print("Congratulations! You have chosen " + chosen_candidate.name + "! Great choice!")


main()
