# # Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# # 예) http://naver.com
# # 규칙1 : http:// 부분은 제외 => naver.com
# # 규칙2 : 처음 만나는 점 (.) 이후 부분은 제외 => naver
# # 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                             (nav)        (5)             (1)         (!)
# 예) 생성된 비밀번호 : nav51!

site = "http://naver.com"
print(site)
three = site[7:10]
site = site[7:-4]
leg = str(len(site))
ecount = site.count("e")
print(f"생성된 비밀번호 : {three}{len}{ecount}!")

#정답

url = "http://naver.com"
print(url)
my_st=url.replace("http://","") #규칙1
my_st=my_st[:my_st.index(".")] #규칙2
three = my_st[0:3]
ecount = my_st.count("e")
print(f"생성된 비밀번호 : {three}{str(len(my_st))}{ecount}!")

password = my_st[:3] + str(len(my_st)) + str(my_st.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(url, password))
print(f"{url}의 비밀번호는 {password}입니다.")
