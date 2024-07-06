class Movie:
    def __init__(self, title, year, includedPlan, note, duration):
        self.title = title
        self.year = year
        self.includedPlan = includedPlan
        self.note = note
        self.duration = duration

    def __str__(self):
        return f'Title: ({self.title})\nYear: ({self.year})\nIncluded Plan: ({self.includedPlan})\nNote: ({self.note})\nDuration: ({self.duration})\n'


movie1 = Movie("The Shawshank Redemption", 1994, "Netflix", 9.3, 142)
movie2 = Movie("The Godfather", 1972, "Amazon Prime", 9.2, 175)
print(f'Movie 1:\n{movie1}')
print(f'Movie 2:\n{movie2}')

