# DataFrame을 이용해 데이터를 생성하는 방법
# df = pd.DataFrame(data [, index = index_data, columns = columns_data])
# data 인자에는 리스트와 형태가 유사한 데이터 타입은 모두 사용 가능
# 즉 리스트, 딕셔너리, numpy의 배열 데이터, Series나 DataFrame 타입의 데이터 입력 가능
# 세로축 라벨ㅇ르 index라 하고, 가로축 라벨을 columns라고 함
# index와 columns를 제외한 부분을 values라고 하고 values가 관심있는 데이터

import pandas as pd

d1 = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]])
print(d1)
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9


# values 부분에는 입력한 data가 순서대로 입력돼 있고
# 가장 좌측의 열과 가장 윗줄의 행에는 각각 숫자가 자동으로 생성되어 index, columns를 구성
# 명시적으로 index와 columns를 입력하지 않더라도 자동으로 index, columns가 생성

# numpy의 배열 데이터를 입력해 생성한 DataFrame 데이터의 예
import numpy as np
data_list = np.array([[10,20,30], [40,50,60], [70,80,90]])
print(data_list)
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

d2 = pd.DataFrame(data_list)
print(d2)
#     0   1   2
# 0  10  20  30
# 1  40  50  60
# 2  70  80  90

# data뿐만 아니라 index와 columns도 지정한 예
data = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]) # values
index_data = pd.date_range('2019-09-01', periods=4)
columns_list = ['A', 'B', 'C']
d3 = pd.DataFrame(data=data, index=index_data, columns=columns_list)
print(d3)
#              A   B   C
# 2019-09-01   1   2   3
# 2019-09-02   4   5   6
# 2019-09-03   7   8   9
# 2019-09-04  10  11  12

# 딕셔너리 타입으로 2차원 데이터를 입력한 예
table_data = {'연도': [2015, 2016, 2016, 2017, 2017],
              '지사': ['한국', '한국', '미국', '한국','미국'],
              '고객 수': [200, 250, 450, 300, 500]}
d4 = pd.DataFrame(table_data)
print(d4)
#      연도  지사  고객 수
# 0  2015  한국   200
# 1  2016  한국   250
# 2  2016  미국   450
# 3  2017  한국   300
# 4  2017  미국   500

# 리스트나 넘파이 배열은 행 단위로 입력이 되고, 딕셔너리는 열 단위로 입력됨

# 입력시 키의 순서를 지정할 수도 있음
d5 = pd.DataFrame(table_data, columns=['지사', '고객 수', '연도'])
print(d5)
#    지사  고객 수    연도
# 0  한국   200  2015
# 1  한국   250  2016
# 2  미국   450  2016
# 3  한국   300  2017
# 4  미국   500  2017

# DataFrame 데이터에서 index, columns, values을 각각 구한 예
print(d5.index) # RangeIndex(start=0, stop=5, step=1)
print(d5.columns) # Index(['지사', '고객 수', '연도'], dtype='object')
print(d5.values)
# [['한국' 200 2015]
#  ['한국' 250 2016]
#  ['미국' 450 2016]
#  ['한국' 300 2017]
#  ['미국' 500 2017]]
















