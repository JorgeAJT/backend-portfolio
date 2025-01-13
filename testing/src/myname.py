
def myname(name: str) -> str:
    if name:
        new_name = ""
        for letter in name:
            if letter != " " and letter != "-" and letter != "_":
                new_name += letter
        return new_name
    else:
        return "Not a valid name"