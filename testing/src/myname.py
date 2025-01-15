def myname(name: str) -> str:
    if isinstance(name, str):
        new_name = ""
        for letter in name:
            if letter != " " and letter != "-" and letter != "_":
                new_name += letter
        return new_name
    else:
        return "Not a valid name"
