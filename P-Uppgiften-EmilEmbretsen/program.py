from candidate import Candidate

def read_candidates_from_file(file_name):
    """
    Reads all lines from file_name and creates a candidate for each candidate in the file. Returns a dictionary with the candidates.
    """
    candidates_dict = dict()
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(";")
            candidates_dict[parts[0]] = Candidate(parts[0], int(parts[1]), parts[2],
                                        float(parts[3]), float(parts[4]), float(parts[5]),
                                        float(parts[6]), float(parts[7]))
    return candidates_dict

def get_form_input(prompt_string):
    """
    The user's response is returned as an integer, where the prompt string is used to communicate what the user inputs.
    """
    correct_input = False;
    while not correct_input:
        try:
            answer = int(input(prompt_string).strip())
            if answer >= 0 and answer <= 5:
                correct_input = True
            else:
                print("Input must be a whole number between 0 and 5.")
        except ValueError:
            print("Input most be a whole number.")
    return answer

def get_gender_input(prompt_string):
    correct_input = False;
    while not correct_input:
        answer = str(input(prompt_string)).upper().strip()
        if answer == "M" or answer == "F" or answer == "B":
            correct_input = True
        else:
            "Svara endast med 'M', 'F' eller 'B'."
    return answer

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

    form_answers = [gender,beauty,intelligence,humor,wealth,education]

    return form_answers

def remove_candidates_of_wrong_gender(form_answers, candidates_dict):
    candidates_to_remove = []
    if form_answers[0] != "B":
        for candidate in candidates_dict:
            if candidates_dict[candidate].gender != form_answers[0]:
                candidates_to_remove.append(candidate)
    for candidate in candidates_to_remove:
        del candidates_dict[candidate]
    return candidates_dict

def grade_attribute(candidate, candicates_dict, attribute):
    """
    Calculates the normalized score for a specific attribute.
    """
    candidate_attribute = getattr(candidate,attribute)
    highest_score = candidate_attribute
    for person in candicates_dict:
        if getattr(candicates_dict[person], attribute) > highest_score:
            highest_score = getattr(candicates_dict[person], attribute)
    score = candidate_attribute / highest_score
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

    grade = round(beauty_score+intelligence_score+humor_score+wealth_score+education_score, 2)
    return grade

def grade_all_candidates(candidates_dict, form_answers):
    for candidate in candidates_dict:
        candidates_dict[candidate].grade = grade_candidate(candidates_dict[candidate],candidates_dict,form_answers)
    return candidates_dict

def main():
    candidates_dict = read_candidates_from_file("candidates.txt") #reads in all the candidates
    form_answers = present_form() #presents the form and gets form answers
    candidates_dict = remove_candidates_of_wrong_gender(form_answers,candidates_dict) #removes all candidates of unwanted gender
    candidates_dict = grade_all_candidates(candidates_dict,form_answers) #grades the candidates


main()