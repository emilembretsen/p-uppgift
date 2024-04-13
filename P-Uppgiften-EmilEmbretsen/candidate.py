class Candidate:
    """
    Class for the candidates with their attributes.
    """
    def __init__(self, name, age, gender, beauty, intelligence, humor, wealth, education):
        """
        Initializes a Candidate object with their specified attributes.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.beauty = beauty
        self.intelligence = intelligence
        self.humor = humor
        self.wealth = wealth
        self.education = education
        self.grade = 0

    def __str__(self):
        """
        Return a string representing the candidate and their attributes.
        """
        return (
            f"Name: {self.name}\n"
            f"Grade: {self.grade}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Beauty: {self.beauty}\n"
            f"Intelligence: IQ of {self.intelligence}\n"
            f"Humor: {self.humor}\n"
            f"Wealth: {self.wealth}kr\n"
            f"Education: {self.education}"
        )
