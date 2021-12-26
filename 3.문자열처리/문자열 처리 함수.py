python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 대문자면 True 아니면 False 리턴
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # index 함수의 두 번째 인자는 startIndex
print(index)

print(python.find("Java"))  # 없으면 -1 return
print(python.index("Java")) # 없으면 에러
print("hi")

print(python.count("n")) # 문자열 안에 n 이 몇개 있는지 return