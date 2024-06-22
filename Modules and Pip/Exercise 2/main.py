import os
def shutdown30():
    os.system("shutdown /s /t 1800")

def shutdown1h():
    os.system("shutdown /s /t 3600")

def cancel_shutdown():
    os.system("shutdown /a")


shutdown1h()
cancel_shutdown()