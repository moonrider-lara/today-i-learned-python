# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, complerion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.complerion_year = complerion_year
    #매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.complerion_year))

class Gangnam(House):
    def __init__(self):
        super().__init__("강남", "아파트", "매매", "10억", "2010년")
class Mapo(House):
    def __init__(self):
        House.__init__(self, "마포", "오피스텔", "전세", "5억", "2007년")
class Songpa(House):
    def __init__(self):
        House.__init__(self, "송파", "빌라", "월세", "500/50", "2000년")

Gangnam1 = Gangnam()
Gangnam1.show_detail()
Mapo1 = Mapo()
Mapo1.show_detail()
Songpa1 = Songpa()
Songpa1.show_detail()

#정답
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, complerion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.complerion_year = complerion_year
    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.complerion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()