def tokenizador(whiles):
    file = open(whiles, "r")
    lines = [line.strip() for line in file.readlines() if line.strip() != ""]
    file.close()

    tokenArray = re.finditer(r"while|[(a-z0-9<>){}]|==", ''.join(lines))
    tokens = []

    for elem in tokenArray:
        token = elem.group()
        tokens.append(token)

    return tokens
