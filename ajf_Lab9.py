def encode(password):
    final = []
    for x in password:
        if x == "0":
            final.append("3")
        if x == "1":
            final.append("4")
        if x == "2":
            final.append("5")
        if x == "3":
            final.append("6")
        if x == "4":
            final.append("7")
        if x == "5":
            final.append("8")
        if x == "6":
            final.append("9")
        if x == "7":
            final.append("0")
        if x == "8":
            final.append("1")
        if x == "9":
            final.append("2")
    return "".join(final)
