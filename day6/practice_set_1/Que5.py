
def secret(data):
    ls1 = data.split(".")
    ls2 = ls1[0]
    ls3 = " ".join(ls1[1:])

    if ls3:
        return (f"<{ls2} class='{ls3}' ></p>")
    else:
        return (f"<{ls2} ")


# data = "p.one.two.three"
# data = "p.one"
data = "p.four.five"

print(secret(data))
