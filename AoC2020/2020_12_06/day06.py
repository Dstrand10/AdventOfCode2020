class GroupAnsweringDeclarationQuestion:
    def __init__(self, group_input_data):

        self.persons_input_data = str(group_input_data).split("\n")
        self.people_in_group = len(self.persons_input_data)
        self.group_all_answered_questions = self.find_all_questions_answered()
        self.group_same_answered_questions = self.find_same_answered_questions_group()

    def find_all_questions_answered(self):
        yes_answered_questions = set()
        for person_data in self.persons_input_data:
            for question in person_data:
                yes_answered_questions.add(str(question))

        return yes_answered_questions

    def find_same_answered_questions_group(self):
        same_questions_answered = ''.join(list(self.group_all_answered_questions))
        for person_answered_question in self.persons_input_data:
            same_questions_answered = ''.join(set(same_questions_answered).intersection(person_answered_question))
        return same_questions_answered


def main():
    input_data = open("input.txt").read().split("\n\n")

    group_answerings = []
    for group_data in input_data:
        group_answerings.append(GroupAnsweringDeclarationQuestion(group_data))

    print("The sum of unique yes question for all groups: " +
          str(sum([len(group_answers.group_all_answered_questions) for group_answers in group_answerings])))
    print("The sum of yes to the same question within the group for all groups: " +
          str(sum([len(group_answers.group_same_answered_questions) for group_answers in group_answerings])))


if __name__ == "__main__":
    main()
