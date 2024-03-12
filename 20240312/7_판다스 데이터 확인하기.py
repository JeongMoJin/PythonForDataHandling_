import pandas as pd

# 1) DataFrame 만들기
# csv 파일 불러오기
# csv 파일을 불러와서 데이터프레임을 생성

df = pd.read_csv('./input/weather.csv')
print(df) # 주피터 노트북에서 df만 기입 시 데이터를 모두 읽음

#             date  temp  max_wind  mean_wind
# 0     2010-08-01  28.7       8.3        3.4
# 1     2010-08-02  25.2       8.7        3.8
# 2     2010-08-03  22.1       6.3        2.9
# 3     2010-08-04  25.3       6.6        4.2
# 4     2010-08-05  27.2       9.1        5.6
# ...          ...   ...       ...        ...
# 3648  2020-07-27  22.1       4.2        1.7
# 3649  2020-07-28  21.9       4.5        1.6
# 3650  2020-07-29  21.6       3.2        1.0
# 3651  2020-07-30  22.9       9.7        2.4
# 3652  2020-07-31  25.7       4.8        2.5
#
# [3653 rows x 4 columns]


# 2) df.shape
# shape 속성을 이용하면 데이터의 (행, 열) 크기를 확인할 수 있음
# 행, 열 크기 확인하기
print(df.shape) # (3653, 4)
print(df.shape[0]) # 3653


# 3) df.info()
# info()메서드는 데이터에 대한 전반적인 정보를 나타냄
# df를 구성하는 행과 열의 크기, 컬럼명, 컬럼을 구성한느 값의 자료형을 출력해줌
df.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3653 entries, 0 to 3652
# Data columns (total 4 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   date       3653 non-null   object
#  1   temp       3653 non-null   float64
#  2   max_wind   3649 non-null   float64
#  3   mean_wind  3647 non-null   float64
# dtypes: float64(3), object(1)
# memory usage: 114.3+ KB

# -> 데이터 개수 n=3653 entry, 행 인덱스 번호 0 to 3652
# 열 변수 출력 형식 : 실수 float, 문자열 object
# 결측치 개수가 나타남 : max_wind, mean_wind 변수에 결측치가 있음


# 4) df.head(), df.tail()
# 데이터를 잘 불러 왔는지 확인하기 위해 앞 부분과 마지막 부분을 확인
# 상위 n행 살펴보기
print(df.head()) # 숫자 기입 시, 개수 행 출력. 기본 = 5
#          date  temp  max_wind  mean_wind
# 0  2010-08-01  28.7       8.3        3.4
# 1  2010-08-02  25.2       8.7        3.8
# 2  2010-08-03  22.1       6.3        2.9
# 3  2010-08-04  25.3       6.6        4.2
# 4  2010-08-05  27.2       9.1        5.6

# 하위 n행 살펴보기
print(df.tail())
#             date  temp  max_wind  mean_wind
# 3648  2020-07-27  22.1       4.2        1.7
# 3649  2020-07-28  21.9       4.5        1.6
# 3650  2020-07-29  21.6       3.2        1.0
# 3651  2020-07-30  22.9       9.7        2.4
# 3652  2020-07-31  25.7       4.8        2.5

# head()는 상위 5개 행을 출력하고, tail()은 하위 5개 행을 출력함
# 괄호() 안에 원하는 숫자를 넣으면 그 숫자만큼 행을 출력


# 5) df.index, df.columns
# 인덱스(행 이름)과 열의 레이블(칼럼 이름)을 출력할 때 사용
# 인덱스 출력
print(df.index) # RangeIndex(start=0, stop=3653, step=1)
# 데이터프레임의 인덱스(행 이름)을 반환. 인덱스를 따로 지정하지 않았기 때문에 0부터 시작하는 인덱스가 부여.

# 칼럼 출력
print(df.columns)
# Index(['date', 'temp', 'max_wind', 'mean_wind'], dtype='object')

# 해당 데이터프레임을 구성하는 컬럼명을 확인할 수 있음
# 컬럼명을 변경할 때도 유용하게 사용


# 6) df.describe()
# 데이터의 컬럼별 요약 통계량을 나타냄
# 또한 mean(), max() 등 개별 함수를 사용하여 통계량을 계산 할 수 있음
# 요약 통계량 확인하기
print(df.describe())
#               temp     max_wind    mean_wind
# count  3653.000000  3649.000000  3647.000000
# mean     12.942102     7.911099     3.936441
# std       8.538507     3.029862     1.888473
# min      -9.000000     2.000000     0.200000
# 25%       5.400000     5.700000     2.500000
# 50%      13.800000     7.600000     3.600000
# 75%      20.100000     9.700000     5.000000
# max      31.300000    26.000000    14.900000


# 7) df.sort_values()
# 데이터를 크기 순으로 정렬
# 형식
# DataFrame.sort_values(by=['정렬변수1', '정렬변수2'...], ascending=True, inplace=False)
# by=[] : by=을 사용하지 않아도 됨
# ascending=True : True가 기본 값이고 오름차순 정렬. 내림차순 정렬일 경우에는 False 사용.
# inplace=False : True 이면 정렬 결과가 동일 데이터프레임 이름으로 저장. 기본 값을 False.

# 최대 풍속 max_wind 컬럼의 값의 크기에 따라 오름차순 정렬
# 값이 같을 경우 인덱스값이 큰 순서대로 정렬
print(df.sort_values(['max_wind']))

#             date  temp  max_wind  mean_wind
# 1514  2014-09-23  20.7       2.0        1.0
# 1134  2013-09-08  20.4       2.1        0.8
# 421   2011-09-26  18.7       2.1        0.3
# 1512  2014-09-21  20.4       2.2        1.2
# 1005  2013-05-02   7.1       2.2        0.8
# ...          ...   ...       ...        ...
# 2988  2018-10-06  19.4      26.0        7.0
# 559   2012-02-11  -0.7       NaN        NaN
# 560   2012-02-12   0.4       NaN        NaN
# 561   2012-02-13   4.0       NaN        NaN
# 3183  2019-04-19   7.8       NaN        2.3
# 
# [3653 rows x 4 columns]


# 최대 풍속 max wind 컬럼의 값의 크기에 따라 내림차순 정렬
print(df.sort_values(by=['max_wind'], ascending=False))
#             date  temp  max_wind  mean_wind
# 2988  2018-10-06  19.4      26.0        7.0
# 3340  2019-09-23  15.0      25.8       11.0
# 1850  2015-08-25  20.1      25.3       14.9
# 3339  2019-09-22  15.7      23.1       11.9
# 1851  2015-08-26  17.4      22.6        8.1
# ...          ...   ...       ...        ...
# 1514  2014-09-23  20.7       2.0        1.0
# 559   2012-02-11  -0.7       NaN        NaN
# 560   2012-02-12   0.4       NaN        NaN
# 561   2012-02-13   4.0       NaN        NaN
# 3183  2019-04-19   7.8       NaN        2.3
#
# [3653 rows x 4 columns]


# 8) df.value_count()
# 범주형 변수의 빈도분석 결과를 출력. 즉 어떤 컬럼의 unique value(고유값)들의 개수를 구함
bank = pd.read_csv('./input/bank.csv')
print(bank.head())
#            job  education  balance  duration   y
# 0   management   tertiary     2143       261  no
# 1   technician  secondary      265       348  no
# 2  blue-collar  secondary       -7       365  no
# 3   technician  secondary       -3      1666  no
# 4   technician  secondary     -103       145  no

# 빈도 분석 출력하기
print(bank['job'].value_counts())
# job
# management       1560
# blue-collar      1499
# technician       1206
# admin.            834
# services          661
# retired           351
# self-employed     256
# entrepreneur      239
# unemployed        223
# housemaid         208
# student           153
# Name: count, dtype: int64

print(bank['education'].value_counts())
# education
# secondary    3745
# tertiary     2178
# primary      1038
# Name: count, dtype: int64

print(bank['job'].value_counts(ascending=True)) # 오름차순 정렬
# job
# student           153
# housemaid         208
# unemployed        223
# entrepreneur      239
# self-employed     256
# retired           351
# services          661
# admin.            834
# technician       1206
# blue-collar      1499
# management       1560
# Name: count, dtype: int64


# 9) df.unique()
# 데이터가 무엇으로 구성되어 있는지 보고싶을 때 사용. 열의 고유값을 볼 수 있음
# column의 고유값 출력하기
print(bank['job'].unique())
# ['management' 'technician' 'blue-collar' 'retired' 'services' 'admin.'
#  'entrepreneur' 'self-employed' 'unemployed' 'student' nan 'housemaid']


# 음식적이 많은 음식골목명을 순서대로 출력
daegu_food = pd.read_csv('./input/daegufood_street.csv')
daegu_food_summary = daegu_food['음식골목명'].value_counts()
daegu_food_summary.to_csv('./output/daegufood_steet_summary.csv')

sangga_info_kb = pd.read_csv('./input/소상공인시장진흥공단_상가(상권)정보/소상공인시장진흥공단_상가(상권)정보_경북_202312.csv')
sangga_info_kb['시군구명'].value_counts().to_csv('./output/gk_store_01.csv')
sangga_info_kb['시군구명'].value_counts(ascending=True).head().to_csv('./output/gk_store_02.csv')
sangga_info_kb['상권업종대분류명'].value_counts(ascending=True).head(3).to_csv('./output/gk_store_03.csv')