keywords = input("What do you want to search? (use comma for multiple keywords) ")

keywords = keywords.strip()
keywords = keywords.replace(", ", ",")
keywords = keywords.replace("，", ",")
keywords = keywords.replace("/", ",")
keywords = keywords.replace("\\", ",")

keywords = keywords.split(",")

for keyword in keywords:
    keyword = keyword.strip()
    print(keyword)