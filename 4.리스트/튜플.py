# 튜플은 리스트와 비슷하나 리스트와는 다르게 변경이나 추가를 할 수 없다. 하지만 속도가 리스트보다 빠르다. 변경되지 않는 목록을 활용할 때 튜플 활용가능

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = "김종국", 20, "코딩" # 튜플을 이용해 한 번에 변수에 다른 값 선언 가능
print(name, age, hobby)