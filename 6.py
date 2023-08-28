from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.storage.jsonstore import JsonStore
from kivy.uix.popup import Popup

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
        self.load_saved_progress()

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

        self.correct_answers = 0

        return self.layout

    def load_saved_progress(self):
        if 'current_category_index' in self.store:
            self.current_category_index = self.store.get('current_category_index')['value']
        else:
            self.current_category_index = 0

        if 'current_question_index' in self.store:
            self.current_question_index = self.store.get('current_question_index')['value']
        else:
            self.current_question_index = 0


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

    def on_start(self):
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text='Möchten Sie fortfahren oder von vorne beginnen?'))

        continue_button = Button(text='Fortfahren', on_release=self.continue_learning)
        restart_button = Button(text='Von vorne beginnen', on_release=self.restart_learning)

        popup_content.add_widget(continue_button)
        popup_content.add_widget(restart_button)

        self.popup = Popup(title='Lernfortschritt', content=popup_content, auto_dismiss=False)
        self.popup.open()

    def continue_learning(self, *args):
        self.popup.dismiss()
        self.save_progress()  # Speichern Sie den Fortschritt, bevor Sie ihn aktualisieren
        self.load_saved_progress()
        self.update_question_ui()

    def restart_learning(self, *args):
        self.popup.dismiss()
        self.current_category_index = 0
        self.current_question_index = 0
        self.correct_answers = 0
        self.update_question_ui()

    def load_all_progress(self):
        for category_index, category in enumerate(self.categories):
            for question_index, question in enumerate(category['questions']):
                progress_key = f'progress_{category_index}_{question_index}'
                if progress_key in self.store:
                    progress_data = self.store.get(progress_key)
                    self.progress[progress_key] = progress_data['value']
                else:
                    self.progress[progress_key] = {
                    'current_category_index': 0,
                    'current_question_index': 0,
                    'correct_answers': 0
                }


    def save_all_progress(self):
        for category_index, category in enumerate(self.categories):
            for question_index, question in enumerate(category['questions']):
                progress_key = f'progress_{category_index}_{question_index}'
                self.store.put(progress_key, value={
                'current_category_index': category_index,
                'current_question_index': question_index,
                'correct_answers': self.correct_answers
            })




if __name__ == '__main__':
    LearningApp().run()