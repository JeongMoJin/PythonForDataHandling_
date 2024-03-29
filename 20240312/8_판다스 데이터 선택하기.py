# Pandas DataFrame으로 부터 데이터를 선택하는 다양한 방법

import pandas as pd

# 1) 열 선택하기
# DataFrame의 하나의 열을 선택하면 하나의 Series를 만듬
# df['컬럼명']는 df.컬럼명과 같음. 단, 이 방법을 사용하려면 열 이름이 숫자로 시작하지 않고 공백이나 특수 문자 등을 포함하지 않는 등의
# 조건을 만족해야함
# iloc() 및 loc() 메서드를 사용하여 려러 열을 선택할 수도 있음

# 단일 컬럼 선택하기
df = pd.read_csv('./input/weather.csv')
print(df['temp'])
# 0       28.7
# 1       25.2
# 2       22.1
# 3       25.3
# 4       27.2
#         ...
# 3648    22.1
# 3649    21.9
# 3650    21.6
# 3651    22.9
# 3652    25.7
# Name: temp, Length: 3653, dtype: float64

print(df.temp)
# 0       28.7
# 1       25.2
# 2       22.1
# 3       25.3
# 4       27.2
#         ...
# 3648    22.1
# 3649    21.9
# 3650    21.6
# 3651    22.9
# 3652    25.7
# Name: temp, Length: 3653, dtype: float64

# 여러 컬럼 선택하기
# 추출할 때 열 이름을 리스트에 저장한 다음 []에 전달하면 여러 열을 선택할 수 있음
print(df[['date', 'temp']])
#             date  temp
# 0     2010-08-01  28.7
# 1     2010-08-02  25.2
# 2     2010-08-03  22.1
# 3     2010-08-04  25.3
# 4     2010-08-05  27.2
# ...          ...   ...
# 3648  2020-07-27  22.1
# 3649  2020-07-28  21.9
# 3650  2020-07-29  21.6
# 3651  2020-07-30  22.9
# 3652  2020-07-31  25.7
#
# [3653 rows x 2 columns]

# 여러 컬럼 선택하기 : loc
# 열 이름을 사용하여 열을 선택하려는 경우 loc를 사용
# df.loc[행 인덱싱 값, 열 인덱싱 값]
df.loc[:, ['date', 'temp']]
#             date  temp
# 0     2010-08-01  28.7
# 1     2010-08-02  25.2
# 2     2010-08-03  22.1
# 3     2010-08-04  25.3
# 4     2010-08-05  27.2
# ...          ...   ...
# 3648  2020-07-27  22.1
# 3649  2020-07-28  21.9
# 3650  2020-07-29  21.6
# 3651  2020-07-30  22.9
# 3652  2020-07-31  25.7
#
# [3653 rows x 2 columns]


# 여러 컬럼 선택하기 : iloc

# 열 인덱스를 사용하여 추출
# df.iloc[행 인덱스, 열 인덱스]
print(df.iloc[:, [0,1]])
# date  temp
# 0     2010-08-01  28.7
# 1     2010-08-02  25.2
# 2     2010-08-03  22.1
# 3     2010-08-04  25.3
# 4     2010-08-05  27.2
# ...          ...   ...
# 3648  2020-07-27  22.1
# 3649  2020-07-28  21.9
# 3650  2020-07-29  21.6
# 3651  2020-07-30  22.9
# 3652  2020-07-31  25.7
#
# [3653 rows x 2 columns]


# 2) 행 선택하기
# 특정 행 범위 선택하기
# 인덱스 숫자를 사용하면 행을 슬라이싱할 수 있음
print(df[0:3])
#          date  temp  max_wind  mean_wind
# 0  2010-08-01  28.7       8.3        3.4
# 1  2010-08-02  25.2       8.7        3.8
# 2  2010-08-03  22.1       6.3        2.9


# 3) 레이블로 선택하기 df.loc
# 특정 날짜에 해당하는 열 선택
df.index = df['date'] # 인덱스 값으로 df['date']을 설정
print(df)
#  date  temp  max_wind  mean_wind
# date
# 2010-08-01  2010-08-01  28.7       8.3        3.4
# 2010-08-02  2010-08-02  25.2       8.7        3.8
# 2010-08-03  2010-08-03  22.1       6.3        2.9
# 2010-08-04  2010-08-04  25.3       6.6        4.2
# 2010-08-05  2010-08-05  27.2       9.1        5.6
# ...                ...   ...       ...        ...
# 2020-07-27  2020-07-27  22.1       4.2        1.7
# 2020-07-28  2020-07-28  21.9       4.5        1.6
# 2020-07-29  2020-07-29  21.6       3.2        1.0
# 2020-07-30  2020-07-30  22.9       9.7        2.4
# 2020-07-31  2020-07-31  25.7       4.8        2.5
#
# [3653 rows x 4 columns]


print(df.loc['2010-08-01', ['temp', 'mean_wind']])
# temp         28.7
# mean_wind     3.4
# Name: 2010-08-01, dtype: object

# 4) 위치로 선택하기 df.iloc
# iloc[n]과 같이 정수를 입력하면 해당 행을 선택. iloc 이후에 붙은 숫자 3은
# (위에서 0부터 시작) 4번째 행이라는 뜻

# 특정 행 선택
print(df.iloc[3])
# date         2010-08-04
# temp               25.3
# max_wind            6.6
# mean_wind           4.2
# Name: 2010-08-04, dtype: object

# 특정 행과 열 선택 : 슬라이싱
print(df.iloc[1:3, 0:2])
#               date  temp
# date
# 2010-08-02  2010-08-02  25.2
# 2010-08-03  2010-08-03  22.1


# 5) 불 인덱싱
# 하나의 열의 값을 기준으로 데이터를 선택할 수 있음
# df[df.A > 0]은 df로 부터 A열이 0보다 큰 데이터를 보여줌.

# 조건에 맞는 데이터를 추출
w = df['temp'] > 30
print(w)
# date
# 2010-08-01    False
# 2010-08-02    False
# 2010-08-03    False
# 2010-08-04    False
# 2010-08-05    False
#               ...
# 2020-07-27    False
# 2020-07-28    False
# 2020-07-29    False
# 2020-07-30    False
# 2020-07-31    False
# Name: temp, Length: 3653, dtype: bool

print(df[w])
#                   date  temp  max_wind  mean_wind
# date
# 2013-08-08  2013-08-08  31.3       7.8        4.6
# 2013-08-09  2013-08-09  30.6       9.9        6.4
# 2013-08-10  2013-08-10  30.6       7.4        3.8
# 2018-07-23  2018-07-23  30.5       6.5        1.6
# 2018-08-04  2018-08-04  30.3       5.8        3.0

# 기온 temp이 30도 이상인 모든 데이터를 추출. 넘파이의 불 인덱싱과 동일한 문법
print(df[df['temp']>30])
#                   date  temp  max_wind  mean_wind
# date
# 2013-08-08  2013-08-08  31.3       7.8        4.6
# 2013-08-09  2013-08-09  30.6       9.9        6.4
# 2013-08-10  2013-08-10  30.6       7.4        3.8
# 2018-07-23  2018-07-23  30.5       6.5        1.6
# 2018-08-04  2018-08-04  30.3       5.8        3.0

# 최고로 더웠던 날의 모든 정보를 추출
w = df['temp'] == df['temp'].max()
print(df[w])
#                   date  temp  max_wind  mean_wind
# date
# 2013-08-08  2013-08-08  31.3       7.8        4.6

# 조건이 2개 이상인 겨우
# 기온이 30도 이상이고, 최대 풍속이 9이상인 데이터
w = (df['temp']>= 30) & (df['max_wind'] >= 9)
print(df[w])
#                   date  temp  max_wind  mean_wind
# date
# 2013-08-09  2013-08-09  30.6       9.9        6.4