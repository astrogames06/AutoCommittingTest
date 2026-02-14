import openai, os, random, math

while True:
    user = input('Say "Go" to commit!: ')

    if user.lower() == "go":
        n = random.randint(0, 10000000000000000)
        print(n)

        with open("file.txt", "w") as f:
            f.write(str(n))

        os.system("git add .")
        os.system(f'git commit -m "My Lucky Number is {n}!"')
        os.system("git push")