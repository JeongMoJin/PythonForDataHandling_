import pandas as pd
import numpy as np

s2 = pd.Series(['a','b','c',5,6,7,8]) # 넘파이 였다면 모두를 문자열로 변경
print(s2)

# 데이터가 없으면 numpy를 임포트한 후에 np.nan으로 데이터가 없음을 표시할 수 있음
# 데이터를 위한 자리 index는 있지만 실제 값이 없음
s3 = pd.Series([np.nan, 10, 30])
print(s3)

# Series 데이터를 생성할 때 다음과 같이 인자로 index 추가 가능
# s = pd.Series(seq_data, index = index_seq)
# 인자로 index를 명시적으로 입력하면 Series 변수(s)의 index에는 자동생성되는 index 대신 index_seq가 들어가게 됨
# index_seq도 리스트와 튜플 타입의 데이터를 모두 사용가능하지만 주로 리스트를 사용
# 주의할 점은 seq_data의 항목 개수와 index_seq의 항목개수가 같아야 함

# 어느 가게의 날짜별 판매량을 pandas의 Series형식으로 입력. 하루는 데이터가 없어서 np.nan을 입력
index_data = ['2018-10-07', '2018-10-08', '2018-10-09', '2018-10-10']
s4 = pd.Series([200, 195, np.nan, 205], index=index_data)
print(s4)
# 2018-10-07    200.0
# 2018-10-08    195.0
# 2018-10-09      NaN
# 2018-10-10    205.0
# dtype: float64


print(s4.index)
# Index(['2018-10-07', '2018-10-08', '2018-10-09', '2018-10-10'], dtype='object')

# 파이썬의 딕셔너리를 사용하면 데이터와 index를 함께 입력할 수 있음
# s = pd.Series(dict_data)
# 입력 인자로 딕셔너리 데이터를 입력하면 딕셔너리 데이터의 키 key와 값 value이 각각
# Series 데이터의 index와 value로 들어감
s5 = pd.Series({'국어' : 100, '영어':95, '수학':90})
print(s5)
# 국어    100
# 영어     95
# 수학     90
# dtype: int64

















