import winsound

launch = [n for n in range(10, -1, -1)]
for n in launch:
    if n == 0:
        winsound.Beep(2500, 500)
    else:
        print(n)
