# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

from random import *
# week = range(1,51)
# print(type(week))
# week = list(week)
# # print(type(week))
# print(week)
# report_file = open("{0}주차.txt".format(week), "w", encoding="utf8") 
# print(" - {0}주차 주간보고 - ".format(week), file=report_file)
# print("부서 : ", file=report_file)
# print("이름 : ", file=report_file)
# print("업무 요약 : ", file=report_file)
# report_file.close()

week = 1
while True :
    report_file = open("{0}주차.txt".format(week), "w", encoding="utf8") 
    print(" - {0}주차 주간보고 - ".format(week), file=report_file)
    print("부서 : ", file=report_file)
    print("이름 : ", file=report_file)
    print("업무 요약 : ", file=report_file)
    report_file.close()
    week += 1
    if week == 51 :
        break

# 정답
for i in range(1,51) :
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report__file:
        report__file.write("- {0} 주차 주간보고 -".format(i))
        report__file.write("\n부서 : ")
        report__file.write("\n이름 : ")
        report__file.write("\n업무 요약 : ")