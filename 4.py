from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.storage.jsonstore import JsonStore

class LearningApp(App):
    def build(self):
        self.categories = [
            {
                'name': 'Lernfeld 1',
                'questions': [
                    {
                        'question': 'Frage 1 zu Lernfeld 1?',
                        'choices': ['Antwort 1', 'Antwort 2', 'Antwort 3', 'Antwort 4'],
                        'correct_choice': 0
                    },
                    {
                        'question': 'Frage 2 zu Lernfeld 1?',
                        'choices': ['Antwort 1', 'Antwort 2', 'Antwort 3', 'Antwort 4'],
                        'correct_choice': 1
                    },
                    # Add more questions for Lernfeld 1
                ]
            },
            {
                'name': 'Lernfeld 2',
                'questions': [
                    {
                        'question': 'Frage 1 zu Lernfeld 2?',
                        'choices': ['Antwort 1', 'Antwort 2', 'Antwort 3', 'Antwort 4'],
                        'correct_choice': 2
                    },
                    {
                        'question': 'Frage 2 zu Lernfeld 2?',
                        'choices': ['Antwort 1', 'Antwort 2', 'Antwort 3', 'Antwort 4'],
                        'correct_choice': 3
                    },
                    # Add more questions for Lernfeld 2
                ]
            },
            # Add more categories here

            {
                'name': 'Lernfeld 3',
                'questions': [
                    {
                        'question': 'Frage 1 zu Lernfeld 2?',
                        'choices': ['Antwort 1', 'Antwort 2', 'Antwort 3', 'Antwort 4'],
                        'correct_choice': 2
                    },
                    {
                        'question': 'Frage 2 zu Lernfeld 2?',
                        'choices': ['Antwort 1', 'Antwort 2', 'Antwort 3', 'Antwort 4'],
                        'correct_choice': 3
                    },
                    # Add more questions for Lernfeld 2
                ]
            },
            # Add more categories here

            {
                'name': 'Lernfeld 4',
                'questions': [
                    {
                        'question': 'Frage 1 zu Lernfeld 2?',
                        'choices': ['Antwort 1', 'Antwort 2', 'Antwort 3', 'Antwort 4'],
                        'correct_choice': 2
                    },
                    {
                        'question': 'Frage 2 zu Lernfeld 2?',
                        'choices': ['Antwort 1', 'Antwort 2', 'Antwort 3', 'Antwort 4'],
                        'correct_choice': 3
                    },
                    # Add more questions for Lernfeld 2
                ]
            },
            # Add more categories here

            {
                'name': 'Lernfeld 5',
                'questions': [
                    {
                        'question': 'Frage 1 zu Lernfeld 2?',
                        'choices': ['Antwort 1', 'Antwort 2', 'Antwort 3', 'Antwort 4'],
                        'correct_choice': 2
                    },
                    {
                        'question': 'Frage 2 zu Lernfeld 2?',
                        'choices': ['Antwort 1', 'Antwort 2', 'Antwort 3', 'Antwort 4'],
                        'correct_choice': 3
                    },
                    # Add more questions for Lernfeld 2
                ]
            },
            # Add more categories here

        ]

        self.store = JsonStore('learning_app_store.json')
        if 'current_category_index' in self.store:
            self.current_category_index = self.store.get('current_category_index')['value']
        else:
            self.current_category_index = 0

        self.current_question_index = 0
        self.correct_answers = 0
        self.layout = BoxLayout(orientation='vertical')

        self.category_spinner = Spinner(text=self.categories[self.current_category_index]['name'], values=[category['name'] for category in self.categories], on_text=self.change_category)
        self.layout.add_widget(self.category_spinner)

        self.question_label = Label(text=self.categories[self.current_category_index]['questions'][self.current_question_index]['question'])
        self.layout.add_widget(self.question_label)

        self.choice_buttons = []
        for i, choice in enumerate(self.categories[self.current_category_index]['questions'][self.current_question_index]['choices']):
            button = Button(text=choice, on_release=self.check_answer)
            self.choice_buttons.append(button)
            self.layout.add_widget(button)

        return self.layout

    def change_category(self, spinner, text):
        self.current_category_index = self.categories.index(next(category for category in self.categories if category['name'] == text))
        self.current_question_index = 0
        self.update_question_ui()

    def update_question_ui(self):
        self.question_label.text = self.categories[self.current_category_index]['questions'][self.current_question_index]['question']
        for i, choice in enumerate(self.categories[self.current_category_index]['questions'][self.current_question_index]['choices']):
            self.choice_buttons[i].text = choice

    def check_answer(self, button):
        correct_choice = self.categories[self.current_category_index]['questions'][self.current_question_index]['correct_choice']
        chosen_choice = self.categories[self.current_category_index]['questions'][self.current_question_index]['choices'].index(button.text)

        if chosen_choice == correct_choice:
            self.correct_answers += 1
            self.question_label.text = "Correct!"
        else:
            self.question_label.text = "Incorrect. The correct answer is: " + self.categories[self.current_category_index]['questions'][self.current_question_index]['choices'][correct_choice]

        self.next_question()

    def next_question(self):
        self.current_question_index = (self.current_question_index + 1) % len(self.categories[self.current_category_index]['questions'])
        if self.current_question_index == 0:
            self.calculate_percentage()
        self.update_question_ui()

    def calculate_percentage(self):
        total_questions = len(self.categories[self.current_category_index]['questions'])
        percentage_correct = (self.correct_answers / total_questions) * 100
        print(f"You answered {self.correct_answers} out of {total_questions} questions correctly in {self.categories[self.current_category_index]['name']}.")
        print(f"Percentage: {percentage_correct}%")

if __name__ == '__main__':
    LearningApp().run()
