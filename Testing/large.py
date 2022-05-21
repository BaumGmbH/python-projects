from tqdm import trange

def write_to_file(content):
    with open("./dump.txt", "a") as file:
        file.write(f"{content}\n")

for i in trange(int(input())):
    number = 10 ** i
    write_to_file(str((number ** 2)))

print("DONE")
