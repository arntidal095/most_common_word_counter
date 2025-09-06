import string
dic ={}
high = 0
with open("stress.txt", "r", encoding="utf_8") as file:
    for line in file:
        for word in line.split():
            word = word.lower()
            word = word.strip(string.punctuation)
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1

value_list = list(dic.values())
high = max(dic.values())

for word, values in dic.items():
    if values == high:
        print("this word appeared the most is: ",word,"which appeared " +str(high) +" times")

