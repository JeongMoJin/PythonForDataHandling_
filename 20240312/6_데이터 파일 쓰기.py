import pandas as pd

# to_csv()을 이용하면 DataFrame 형식의 데이터를 텍스트 파일로 저장
# DataFrame_data.to_csv(file_name [, options])
# file_name은 텍스트 파일 이름으로 경로를 포함할 수 있음
# 선택사항인 options에는 구분자와 문자의 인코딩 방식 등을 지정할 수 있고, 지정하지 않으면 구분자는 콤마가 되고, 문자의 인코딩 방식은 'utf-8'이 됨

# 네 명의 몸무게 Weight와 키 Height 데이터를 DataFrame 형식으로 생성
df_WH = pd.DataFrame({'Weight': [62, 67, 55, 74],
                      'Height': [165, 177, 160, 180]},
                     index=['ID_1', 'ID_2', 'ID_3', 'ID_4'])
print(df_WH)
#       Weight  Height
# ID_1      62     165
# ID_2      67     177
# ID_3      55     160
# ID_4      74     180

df_WH.index.name = 'User'
print(df_WH)
#       Weight  Height
# User
# ID_1      62     165
# ID_2      67     177
# ID_3      55     160
# ID_4      74     180

# 파일로 저장하기 전에 몸무게와 키를 이용해 체질량 지수 BMI를 구해서 추가
# 체질량 지수 Body Mass Index는 몸무게 Kg
# BMI = W / H의 제곱

# 키의 경우 데이터가 cm단위여서 m 단위로 변경
bmi =df_WH['Weight'] / (df_WH['Height']/100) ** 2
print(bmi)
# User
# ID_1    22.773186
# ID_2    21.385936
# ID_3    21.484375
# ID_4    22.839506
# dtype: float64

# 체질량 지수를 df_WH에 추가.
df_WH['BMI'] = bmi
print(df_WH)
#       Weight  Height        BMI
# User
# ID_1      62     165  22.773186
# ID_2      67     177  21.385936
# ID_3      55     160  21.484375
# ID_4      74     180  22.839506

# csv 파일 저장
df_WH.to_csv('./output/save_dataFrame.csv')

# DataFrame 데이터를 파일로 저장할 때 옵션을 지정하는 예
# 한 회사의 제품별 판매 가격과 판매량 정보가 있는 DataFrame 데이터를 생성
df_pr = pd.DataFrame({'판매가격' : [2000, 3000, 5000, 10000],
                      '판매량' : [32, 53, 40, 25]},
                     index=['P1001', 'P1002', 'P1003', 'P1004'])
df_pr.index.name = '제품번호'
print(df_pr)
#         판매가격  판매량
# 제품번호
# P1001   2000   32
# P1002   3000   53
# P1003   5000   40
# P1004  10000   25

file_name = './output/save_DataFrame_cp949.txt'
df_pr.to_csv(file_name, sep=' ', encoding='cp949')