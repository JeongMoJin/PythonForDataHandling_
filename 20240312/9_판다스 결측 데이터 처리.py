# pandas는 누락된 데이터를 표시할 때 NaN(Not a Number)으로 표기하며, 연산에는 포함되지 않음
import pandas as pd
df = pd.read_csv('./input/weather.csv')
print(df.head())
#          date  temp  max_wind  mean_wind
# 0  2010-08-01  28.7       8.3        3.4
# 1  2010-08-02  25.2       8.7        3.8
# 2  2010-08-03  22.1       6.3        2.9
# 3  2010-08-04  25.3       6.6        4.2
# 4  2010-08-05  27.2       9.1        5.6

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


#isnull은 결측 데이터라면 True 반환. 유효한 데이터가 존재한다면 False반환
# ina(), isnumm()은 기능적으로 동일

# 결측 에이터

# 2) 결측 데이터 삭제하기
# 결측 데이터를 다루는 가장 간단한 방법은 결측 데이터를 가진 해잉나 열을 삭제
# DataFrame.dropna(axis, how, thresh, subset, inplace)
# axis : 축을 행 또는 열로 결정
# 0 또는 'index'이면 누락된 값이 포함된 행을 삭제
# 1 또는 'columns'이면 누락된 값이 포함된 열을 삭제
# 기본적으로 값은 0
# how : any는 null 값이 있는 경우 행 또는 열을 삭제
# all은 모든 값이 누락된 경우 행 또는 열을 삭제
# 기본값은 any
# inplace : 데이터프레임에 나온 값을 저장할 것인지를 설정하는 변수로 기본적으로 값은 False

# 결측 데이터가 있는 행 삭제 후 확인
df2 = df.dropna() # 옵션을 지정하지 않아서 행기준, NoN가 하나라도 있은 경우에 삭제
print(df2.isnull().sum())
# temp         0
# max_wind     0
# mean_wind    0
# dtype: int64

# 행 데이터 중 어느 한 변수에도 결측치가 있는 경우 삭제되므로
# 향후 제거한 데이터프레임을 사용하려면 다른 이름으로 저장해야 함
print(df.isnull().sum())
# temp         0
# max_wind     4
# mean_wind    6
# dtype: int64

# 3) 결측 데이터 대체하기
# 결측 데이터 대체하기 : 평균값으로 대체

df['max_wind'].fillna(df['max_wind'].mean(), inplace=True)
df['mean_wind'].fillna(df['mean_wind'].mean(), inplace=True)
# fillna() 같은 데이터를 특정 값으로 채움. inplace를 True로 설정해 원본 데이터를 수정

# 결측 데이터 대체 후 확인
print(df.isna().sum())
# temp         0
# max_wind     0
# mean_wind    0
# dtype: int64