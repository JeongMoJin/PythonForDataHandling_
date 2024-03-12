# pd.date_range(start=None, end=None, periods=None, freq='0')
# start는 시작날짜
# end는 끝날짜
# periods는 날짜 데이터 생성 기간 -> 생성 갯수
# freq는 날짜 데이터 생성 주기
# start는 필수이고, end나 periods는 둘 중 하나만 있어도 됨
# freq는 입력하지 않으면 'D' 옵션이 설정돼 달력날짜 기준으로 하루씩 증가.

# * pandas date_range() 함수의 freq 옵션.
# 약어	설명	사용 예
# D	: 달력 날짜 기준 하루 주기 ex) 하루 주기: freq = 'D', 이틀 주기: freq = '2D'
# B	: 업무 날짜 기준 하루 주기 ex) 업무일(월~금) 기준으로 생성, freq = 'B', freq = '3B'
# W	: 일요일 시작 기준 일주일 주기 ex) 월요일: W-MON, 화요일: W-TUE, freq = 'W', freq = 'W-MON'
# M	: 월말 날짜 기준 주기 ex) 한 달 주기: freq = 'M', 네 달 주기: freq = '4M'
# BM : 업무 월말 날짜 기준 주기	ex) freq = 'BM' , freq = '2BM'
# MS : 월초 날짜 기준 주기 ex) freq = 'MS' , freq = '2MS'
# BMS :	업무 월초 날짜 기준 주기	 ex) freq = 'BMS' , freq = '2BMS'
# Q	: 분기 끝 날짜 기준 주기	 ex) freq = 'Q' , freq = '2Q'
# BQ : 업무 분기 끝 날짜 기준 주기 ex) freq = 'BQ' , freq = '2BQ'
# QS : 분기 시작 날짜 기준 주기	ex) freq = 'QS' , freq = '2QS'
# BQS : 업무 분기 시작 날짜 기준 주기 ex) freq = 'BQS' , freq = '2BQS'
# A	: 일년 끝 날짜 기준 주기	ex) freq = 'A' , freq = '2A'
# BA : 업무 일년 끝 날짜 기준 주기 ex) freq = 'BA' , freq = '2BA'
# AS : 일년 시작 날짜 기준 주기 ex) freq = 'AS' , freq = '2AS'
# BAS : 업무 일년 시작 날짜 기준 주기 ex) freq = 'BAS' , freq = '2BAS'
# H	: 시간 기준 주기 ex) 1시간 주기: freq = 'H' , 2시간 주기: freq = '2H'
# BH : 업무 시간 기준 주기 ex) 업무 시간(09:00 ~ 17:00) 기준으로 생성
# T, min : 분 주기	ex) 10분 주기: freq = '10T' , 30분 주기: freq = '30min'
# S	: 초 주기 ex) 1초 주기: freq = 'S' , 10초 주기: freq = '10S'

import pandas as pd

# 시작 날짜와 끝 날짜를 지정해 날짜 데이터를 생성. 하루씩 증가한 날짜 데이터가 생성
print(pd.date_range(start='2019-01-01', end='2019-01-07'))
# DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
#                '2019-01-05', '2019-01-06', '2019-01-07'],
#               dtype='datetime64[ns]', freq='D')


# 날짜 데이터를 입력할 때 yyyy-mm-dd 형식이 아니라
# yyyy/mm/dd, yyyy.mm.dd, mm-dd-yyyy, mm/dd/yyyy, mm.dd.yyyy 같은 형식도 사용가능하고
# 대신 출력은 yyyy-mm-dd 형식으로 생성

print(pd.date_range(start='2019/01/01', end='2019.01.07'))
# DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
#                '2019-01-05', '2019-01-06', '2019-01-07'],
#               dtype='datetime64[ns]', freq='D')

print(pd.date_range(start='01-01-2019', end='01/07/2019'))
# DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
#                '2019-01-05', '2019-01-06', '2019-01-07'],
#               dtype='datetime64[ns]', freq='D')

print(pd.date_range(start='2019-01-01', end='01.07.2019'))
# DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
#                '2019-01-05', '2019-01-06', '2019-01-07'],
#               dtype='datetime64[ns]', freq='D')

# 끝 날짜를 지정하지 않고 periods만 입력해서 날짜 생성
print(pd.date_range(start='2019-01-01', periods=7))
# DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
#                '2019-01-05', '2019-01-06', '2019-01-07'],
#               dtype='datetime64[ns]', freq='D')

# 2일씩 증가하는 날짜를 생성
print(pd.date_range(start='2019-01-01', periods=4, freq='2D'))
# DatetimeIndex(['2019-01-01', '2019-01-03', '2019-01-05', '2019-01-07'], dtype='datetime64[ns]', freq='2D')

#달력의 요일을 기준으로 일주일씩 증가하는 날짜를 생성
print(pd.date_range(start='2019-01-01', periods=4, freq='W'))
# DatetimeIndex(['2019-01-06', '2019-01-13', '2019-01-20', '2019-01-27'], dtype='datetime64[ns]', freq='W-SUN')

# 업무일 기준 2개월 월말 주기로 12개 날짜를 생성
print(pd.date_range(start='2019-01-01', periods=12, freq='2BM'))
# DatetimeIndex(['2019-01-31', '2019-03-29', '2019-05-31', '2019-07-31',
#                '2019-09-30', '2019-11-29', '2020-01-31', '2020-03-31',
#                '2020-05-29', '2020-07-31', '2020-09-30', '2020-11-30'],
#               dtype='datetime64[ns]', freq='2BM')

# 분기 시작일을 기준으로 4개의 날짜를 생성
print(pd.date_range(start='2019-01-01', periods=4, freq='QS'))
# DatetimeIndex(['2019-01-01', '2019-04-01', '2019-07-01', '2019-10-01'], dtype='datetime64[ns]', freq='QS-JAN')

# 1시간 주기로 10개의 시간을 생성한 예
print(pd.date_range(start='2019-01-01 08:00', periods=10, freq='H'))
# DatetimeIndex(['2019-01-01 08:00:00', '2019-01-01 09:00:00',
#                '2019-01-01 10:00:00', '2019-01-01 11:00:00',
#                '2019-01-01 12:00:00', '2019-01-01 13:00:00',
#                '2019-01-01 14:00:00', '2019-01-01 15:00:00',
#                '2019-01-01 16:00:00', '2019-01-01 17:00:00'],
#               dtype='datetime64[ns]', freq='H')

# 업무 시간을 기준으로 1시간 주기로 10개의 시간을 생성하는 예
# 업무 시간은 9시 부터 17시까지이므로 start시간을 9시 이전으로 설정해도 9시부터 표시
print(pd.date_range(start='2019-01-01 08:00', periods=10, freq='BH'))
# DatetimeIndex(['2019-01-01 09:00:00', '2019-01-01 10:00:00',
#                '2019-01-01 11:00:00', '2019-01-01 12:00:00',
#                '2019-01-01 13:00:00', '2019-01-01 14:00:00',
#                '2019-01-01 15:00:00', '2019-01-01 16:00:00',
#                '2019-01-02 09:00:00', '2019-01-02 10:00:00'],
#               dtype='datetime64[ns]', freq='BH')

# date_range()를 이용해 Series의 index를 지정한 예.
index_date = pd.date_range(start='2019-03-01', periods=5, freq='D')
s = pd.Series([51, 62, 55, 49, 58], index=index_date)
print(s)
# 2019-03-01    51
# 2019-03-02    62
# 2019-03-03    55
# 2019-03-04    49
# 2019-03-05    58
# Freq: D, dtype: int64










