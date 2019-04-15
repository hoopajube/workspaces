seen = set()
unique = []

for x in workspaceid_list:
    if x not in seen:
        unique.append(x)
        seen.add(x)
