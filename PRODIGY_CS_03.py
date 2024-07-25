import re

class PasswordStrengthAssessor:
    def __init__(self, password):
        self.password = password
        self.strength_criteria = {
            'length': self.check_length,
            'uppercase': self.check_uppercase,
            'lowercase': self.check_lowercase,
            'numbers': self.check_numbers,
            'special_chars': self.check_special_chars
        }
        self.strength_score = 0
        self.feedback = ""

    def assess_password_strength(self):
        for criterion, check_func in self.strength_criteria.items():
            if check_func():
                self.strength_score += 1
        self.determine_feedback()

    def check_length(self):
        return len(self.password) >= 12

    def check_uppercase(self):
        return re.search(r"[A-Z]", self.password) is not None

    def check_lowercase(self):
        return re.search(r"[a-z]", self.password) is not None

    def check_numbers(self):
        return re.search(r"\d", self.password) is not None

    def check_special_chars(self):
        return re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", self.password) is not None

    def determine_feedback(self):
        if self.strength_score == 5:
            self.feedback = "Strong password!"
        elif self.strength_score >= 3:
            self.feedback = "Medium password. Consider adding more complexity."
        else:
            self.feedback = "Weak password. Please use a stronger password."

    def get_assessment_results(self):
        return {
            'strength_score': self.strength_score,
            'feedback': self.feedback
        }

def main():
    password = input("Enter a password: ")
    assessor = PasswordStrengthAssessor(password)
    assessor.assess_password_strength()
    results = assessor.get_assessment_results()
    print("Password Strength Assessment:")
    print(f"  Strength Score: {results['strength_score']}/5")
    print(f"  Feedback: {results['feedback']}")

if __name__ == "__main__":
    main()