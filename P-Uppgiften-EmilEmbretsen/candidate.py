class Candidate:

    def __init__(self, name, age, gender, beauty, intelligence, humor, wealth, education):
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
        return ("Name: " + self.name + ", Age: " + str(self.age) + ", Gender: " + self.gender +
                ", Beauty: " + str(self.beauty) + ", Intelligence: IQ of " + str(self.intelligence) +
                ", Humor: " + str(self.humor) + ", Wealth: " + str(self.wealth) +
                "kr, Education: " + str(self.education))


