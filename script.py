import openai, os

while True:
    user = input('Say "Go" to commit!: ')

    if user.lower() == "go":
        os.system("ls")