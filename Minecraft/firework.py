import sys
from random import randint

print(sys.argv)  

if len(sys.argv) == 5:
    max_colors = sys.argv[1]
    max_fade_colors = sys.argv[2]
    explosion_count = sys.argv[3]
    mcfunction_path = sys.argv[4]
else:
    max_colors = input("Max colors per explosion: ")
    max_fade_colors = input("Max fade colors per explosion: ")
    explosion_count = input("How many explosions should it have? ")
    mcfunction_path = input("McFunction Path: ")

command = "/give @p firework_rocket{Fireworks:{Flight:1b,Explosions:[<explosions>]}}"

# /give @p firework_rocket{Fireworks:{Flight:1b,Explosions:[$]}}

# {Type:1,Flicker:1b,Trail:1b,Colors:[I;<colors>],FadeColors:[I;<fadecolors>]}
# 16777215
def generate_random_explosion(color_count: int, fade_color_count: int) -> str:
    explosion = "{Type:<type>,Flicker:<flicker>b,Trail:<trail>b,Colors:[I;<colors>],FadeColors:[I;<fadecolors>]}"

    type = randint(0, 4)
    flicker = randint(0, 1)
    trail = randint(0, 1)
    colors = []
    fade_colors = []

    for i in range(color_count):
        colors.append(randint(0, 16777215))
    for i in range(fade_color_count):
        fade_colors.append(randint(0, 16777215))

    colors = str(colors)[1:-1]
    fade_colors = str(fade_colors)[1:-1]

    return explosion.replace("<type>", str(type)).replace("<flicker>", str(flicker)).replace("<trail>", str(trail)).replace("<colors>", colors).replace("<fadecolors>", fade_colors)

try:
    max_colors = int(max_colors)
    max_fade_colors = int(max_fade_colors)
    explosion_count = int(explosion_count)
except ValueError:
    print("Please enter numbers!")
    exit()

explosions = []

for i in range(explosion_count):
    explosions.append(generate_random_explosion(randint(1, max_colors), randint(1, max_fade_colors)))

explosions = str(explosions)[2:-2].replace("'", "")

command = command.replace("<explosions>", explosions)

with open(mcfunction_path, "w") as file:
    file.write(command[1:])
