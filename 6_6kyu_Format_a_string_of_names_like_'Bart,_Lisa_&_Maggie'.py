def namelist(names):
    if len(names) == 0:
        return ""
    if len(names) == 1:
        return names[0]["name"]
    if len(names) == 2:
        return names[0]["name"] + " & " + names[1]["name"]
    result = ""
    for i in names:
        if i["name"] == names[-2]["name"]:
            return result + names[-2]["name"] + " & " + names[-1]["name"]
        result += i["name"] + ", "
    return result


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))
