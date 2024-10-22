def find_short(string):
    length_list = []
    counter = 0
    for i in string:
        if i != " ":
            counter += 1
        else:
            length_list.append(counter)
            counter = 0
    if counter:
        length_list.append(counter)
    return min(length_list)
print(find_short("Me encanta el Ghost of Tsushima"))

# SOLUCION MAS EFICIENTE
# def find_short(s):
#     return min(len(x) for x in s.split())
# generador es mas eficiente ya que no crea una lista completa en memoria, va usando los datos sobre la marcha