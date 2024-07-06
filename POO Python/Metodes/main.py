class Movie:
    def __init__(self, title, year, includedPlan, note, duration):
        self.title = title
        self.year = year
        self.includedPlan = includedPlan
        self.note = note
        self.duration = duration

    def __str__(self):
        return f'Title: ({self.title})'

    def technical_sheet(self):
        print(f'##Movie Information##')
        print(f'Title: {self.title}')
        print(f'Year: {self.year}')
        print(f'Included Plan: {self.includedPlan}')
        print(f'Note: {self.note}')
        print(f'Duration: {self.duration}\n')
    

mario = Movie('Super Mario Bros', 1993, False, 2.5, 104)
top_gun = Movie('Top Gun', 1986, True, 4.5, 110)
mario.technical_sheet()
top_gun.technical_sheet()

