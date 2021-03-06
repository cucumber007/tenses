import json
import random

sample_data = json.loads('{"gender_male":true,"i"'
                         ':["я","ты","мы","вы","они","он","она","оно"],"will":["буду","будешь","будем","будете","будут","будет"],"future":["буду","будете","будет"],"words":[[{"мы,вы,они":"ходили","она":"ходила","он":"ходил","оно":"ходило"},["хожу","ходишь","ходим","ходите","ходят","ходит"],["ходить"]],[{"я,он,ты":"летал","мы,вы,они":"летали","она":"летала","оно":"летало"},["летаю","летаешь","летаем","летаете","летают","летает"],["летать"]]]}')

try:
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
except FileNotFoundError as e:
    print("data.json not found, creating form sample...\n")
    data = sample_data
    with open("data.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
        f.close()

i = data["i"]
will = data["will"]
future = data["future"]
words = data["words"]
gender_male = data["gender_male"]


def gen():
    res = ""
    iv = random.choice(i)
    # iv = random.choice(["я", "ты"])
    inn = i.index(iv)
    res += str(iv)
    tense = random.randint(0, 2)
    # tense = 0
    w = random.choice(words)[tense]

    nnot = bool(random.randint(0,1))
    if nnot:
        n = " не "
    else:
        n = " "

    q = bool(random.randint(0,1))
    if q:
        qv = "?"
    else:
        qv = ""

    if tense == 0:  # past
        wz = None
        for k, v in w.items():
            if iv in k.split(","):
                wz = v
        if wz is None:
            if iv == "я":
                if gender_male:
                    wz = w["он"]
                else:
                    wz = w["она"]
            elif iv ==  "ты":
                wz = w[random.choice(["он", "она"])]


        res += f"{n}{wz}{qv}"
    if tense == 1:  # present
        if inn < len(w):
            res += f"{n}{w[inn]}"
        else:
            res += f"{n}{w[-1]}{qv}"
    if tense == 2:  # future
        if inn < len(will):
            wl = will[inn]
        else:
            wl = will[-1]
        res += f"{n}{wl} {w[0]}{qv}"

    return res


last = ""
while True:
    g = gen()
    if g == last:
        continue
    last = g
    print(g)
    input()

