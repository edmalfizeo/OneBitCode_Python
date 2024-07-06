class Movie:
    name = ""
    yearLauncher = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

# First Movie
movie1 = Movie()
movie1.name = "The Lord of the Rings: The Fellowship of the Ring"
movie1.yearLauncher = 2001
movie1.includedPlan = True
movie1.note = 8.8
movie1.durationMinutes = 178

print(f'Movie: {movie1.name}\nYear: {movie1.yearLauncher}\nIncluded in the plan: {movie1.includedPlan}\nNote: {movie1.note}\nDuration: {movie1.durationMinutes} minutes')