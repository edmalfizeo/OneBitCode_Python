class Movie:
    platform = 'OneBitMovies'
    
    def __init__(self, title, year, includedPlan, duration):
        self.title = title
        self.year = year
        self.includedPlan = includedPlan
        self.duration = duration
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f'Title: ({self.title})'

    def technical_sheet(self):
        print(f'##Movie Information##')
        print(f'Platform: {Movie.platform}')
        print(f'Title: {self.title}')
        print(f'Year: {self.year}')
        print(f'Included Plan: {self.includedPlan}')
        print(f'Duration: {self.duration}\n')

    def note_movie(self):
        given_note = float(input('Give a note to the movie: '))
        self.totalEvaluation += given_note
        self.evaluators += 1

    def avarage(self):
        print(f'\nThe avarage note of the movie {self.title} is {self.totalEvaluation/self.evaluators}')


mario = Movie('Super Mario Bros', 1993, 'Basic', 104)
avatar = Movie('Avatar', 2009, 'Premium', 162)
mario.technical_sheet()
mario.note_movie()
mario.avarage()        
# Modify Platform
Movie.platform = 'OneBitPlus'
avatar.technical_sheet()