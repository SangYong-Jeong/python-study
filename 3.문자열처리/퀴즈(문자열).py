site = "http://naver.com"

# 규칙 1
site = site[-9:]
print(site)

# 규칙 2
site = site[:5]
print(site)

# 규칙 3
print(site[:3] + str(len(site)) + str(site.count("e")) + "!")

# url = "http://naver.com"
# url = "http://daum.net"
# url = "http://google.com"
url = "http://youtube.com"
my_str = url.replace("http://", "") # 규칙 1
# print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙 2 # my_str[0:5] -> 0 ~ 5직전까지 (0, 1, 2, 3, 4)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) +  "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))