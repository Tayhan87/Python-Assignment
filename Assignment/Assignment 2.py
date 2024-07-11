with open("input.txt","r") as f:

    search={"Python": 0 ,"C": 0, "OOP":0,"Hello":0,"Java": 0}

    for line in f:
        line = line.strip()
        line = line.lower()
        for search_key in search.keys():
            key=search_key
            key=key.lower()
            if key == line:
             search[search_key]+=1

for key,value in search.items():
    print("{key} -> {value}".format(key=key,value=value))
