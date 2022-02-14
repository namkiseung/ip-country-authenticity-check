import csv
import datetime
import time
import logging
import re

class ip_identity(object):
    def __init__(self,country):
        self.country = country

    def __str__(self):
        return self.country

    def __repr__(self):
        return "'"+self.country+"'"

#global variable init
fields = ['event_name', 'ip', 'timestamp']
ip_cnt = 0
result_global_ip_cnt = 0 #not using
ip_list = list()
ip_list_global = list() 
ip_list_write = dict()

country_code_translate ={
"GH" : "가나",
"GA" : "가봉",
"GY" : "가이아나",
"GM" : "감비아",
"GP" : "프랑스",
"GT" : "과테말라",
"GU" : "미국",
"GD" : "그레나다",
"GE" : "그루지야",
"GR" : "그리스",
"GL" : "덴마크",
"GW" : "기니비소",
"GN" : "기니",
"NA" : "나미비아",
"NG" : "나이지리아",
"ZA" : "남아프리카공화국",
"NL" : "네덜란드",
"AN" : "네덜란드",
"NP" : "네팔",
"NO" : "노르웨이",
"NF" : "오스트레일리아",
"NZ" : "뉴질랜드",
"NC" : "프랑스",
"NE" : "니제르",
"NI" : "니카라과",
"TW" : "타이완",
"DK" : "덴마크",
"DM" : "도미니카연방",
"DO" : "도미니카공화국",
"DE" : "독일",
"LA" : "라오스",
"LV" : "라트비아",
"RU" : "러시아",
"LB" : "레바논",
"LS" : "레소토",
"RO" : "루마니아",
"RW" : "르완다",
"LU" : "룩셈부르크",
"LR" : "라이베리아",
"LY" : "리비아",
"RE" : "프랑스",
"LT" : "리투아니아",
"LI" : "리첸쉬테인",
"MG" : "마다가스카르",
"MH" : "미국",
"FM" : "미크로네시아",
"MK" : "마케도니아",
"MW" : "말라위",
"MY" : "말레이지아",
"ML" : "말리",
"MT" : "몰타",
"MQ" : "프랑스",
"MX" : "멕시코",
"MC" : "모나코",
"MA" : "모로코",
"MU" : "모리셔스",
"MR" : "모리타니",
"MZ" : "모잠비크",
"MS" : "영국",
"MD" : "몰도바",
"MV" : "몰디브",
"MN" : "몽고",
"US" : "미국",
"VI" : "미국",
"AS" : "미국",
"MM" : "미얀마",
"VU" : "바누아투",
"BH" : "바레인",
"BB" : "바베이도스",
"BS" : "바하마",
"BD" : "방글라데시",
"BY" : "벨라루스",
"BM" : "영국",
"VE" : "베네수엘라",
"BJ" : "베넹",
"VN" : "베트남",
"BE" : "벨기에",
"BZ" : "벨리세",
"BA" : "보스니아헤르체코비나",
"BW" : "보츠와나",
"BO" : "볼리비아",
"BF" : "부르키나파소",
"BT" : "부탄",
"MP" : "미국",
"BG" : "불가리아",
"BR" : "브라질",
"BN" : "브루네이",
"BI" : "브룬디",
"WS" : "미국(사모아,",
"SA" : "사우디아라비아",
"CY" : "사이프러스",
"SM" : "산마리노",
"SN" : "세네갈",
"SC" : "세이셸",
"LC" : "세인트루시아",
"VC" : "세인트빈센트그레나딘",
"KN" : "세인트키츠네비스",
"SB" : "솔로몬아일란드",
"SR" : "수리남",
"LK" : "스리랑카",
"SZ" : "스와질랜드",
"SE" : "스웨덴",
"CH" : "스위스",
"ES" : "스페인",
"SK" : "슬로바키아",
"SI" : "슬로베니아",
"SL" : "시에라리온",
"SG" : "싱가포르",
"AE" : "아랍에미레이트연합국",
"AW" : "네덜란드",
"AM" : "아르메니아",
"AR" : "아르헨티나",
"IS" : "아이슬란드",
"HT" : "아이티",
"IE" : "아일란드",
"AZ" : "아제르바이잔",
"AF" : "아프가니스탄",
"AI" : "영국",
"AD" : "안도라",
"AG" : "앤티과바부다",
"AL" : "알바니아",
"DZ" : "알제리",
"AO" : "앙골라",
"ER" : "에리트리아",
"EE" : "에스토니아",
"EC" : "에콰도르",
"SV" : "엘살바도르",
"GB" : "영국",
"VG" : "영국",
"YE" : "예멘",
"OM" : "오만",
"AU" : "오스트레일리아",
"AT" : "오스트리아",
"HN" : "온두라스",
"JO" : "요르단",
"UG" : "우간다",
"UY" : "우루과이",
"UZ" : "우즈베크",
"UA" : "우크라이나",
"ET" : "이디오피아",
"IQ" : "이라크",
"IR" : "이란",
"IL" : "이스라엘",
"EG" : "이집트",
"IT" : "이탈리아",
"IN" : "인도",
"ID" : "인도네시아",
"JP" : "일본",
"JM" : "자메이카",
"ZM" : "잠비아",
"CN" : "중국",
"MO" : "중국",
"HK" : "중국",
"CF" : "중앙아프리카",
"DJ" : "지부티",
"GI" : "영국",
"ZW" : "짐바브웨",
"TD" : "차드",
"CZ" : "체코",
"CS" : "체코슬로바키아",
"CL" : "칠레",
"CA" : "캐나다",
"CM" : "카메룬",
"CV" : "카보베르데",
"KY" : "영국",
"KZ" : "카자흐",
"QA" : "카타르",
"KH" : "캄보디아",
"KE" : "케냐",
"CR" : "코스타리카",
"CI" : "코트디봐르",
"CO" : "콜롬비아",
"CG" : "콩고",
"CU" : "쿠바",
"KW" : "쿠웨이트",
"HR" : "크로아티아",
"KG" : "키르키즈스탄",
"KI" : "키리바티",
"TJ" : "타지키스탄",
"TZ" : "탄자니아",
"TH" : "타이",
"TC" : "영국",
"TR" : "터키",
"TG" : "토고",
"TO" : "통가",
"TV" : "투발루",
"TN" : "튀니지",
"TT" : "트리니다드토바고",
"PA" : "파나마",
"PY" : "파라과이",
"PK" : "파키스탄",
"PG" : "파푸아뉴기니",
"PW" : "미국",
"FO" : "덴마크",
"PE" : "페루",
"PT" : "포르투갈",
"PL" : "폴란드",
"PR" : "미국",
"FR" : "프랑스",
"GF" : "프랑스",
"PF" : "프랑스",
"FJ" : "피지",
"FI" : "필란드",
"PH" : "필리핀",
"HU" : "헝가리",
"KR" : "한국",
"EU" : "유럽",
"SY" : "시리아",
"A1" : "Anonymous Proxy",
"A2" : "인공위성IP",
"PS" : "팔레스타인",
"RS" : "세르비아",
"JE" : "저지"
}

''' 
    >>Sample dataset
        sample_dict = [
        {'ID': 1, 'Date in': datetime.date.today(), 'ipName': 'global Name 1', 'Quantity': 5, 'isCont': 'N','Total': 'normal'},
        {'ID': 2, 'Date in': datetime.date.today(), 'ipName': 'global Name 2', 'Quantity': 10, 'isCont': 'Y','Total': 'normal'},
        {'ID': 3, 'Date in': datetime.date.today(), 'ipName': 'global Name 3', 'Quantity': 3, 'isCont': 'Y', 'Total': 'normal'}
        ]
        
    >>dummy dataset
    ['carrier_kr_false_2001:e60:9240:a3ce:958b:1749:ae66:1ebe', '118.235.4.162', '2022-02-14 14:50']
    ['carrier_kr_false_172.30.1.23', '125.141.29.79', '2022-02-14 14:50']
    ['carrier_kr_false_10.91.25.120', '106.101.128.82', '2022-02-14 14:50']
    ['carrier_kr_false_192.0.0.4_LGU+_kr_LG U+_false', '106.101.67.74', '2022-02-14 14:50']
    ['carrier_kr_false_192.0.0.4_LGU+_kr_LG U+_false', '117.111.28.8', '2022-02-14 14:50']
    ['carrier_kr_false_26.156.220.37_LGU+_kr_LG U+_false', '106.102.11.1', '2022-02-14 14:50']
    ['carrier_kr_false_192.0.0.4_KT_kr_KT_false', '118.235.13.165', '2022-02-14 14:50']
    ['carrier_kr_false_192.0.0.4_SK Telecom_kr_SKTelecom_false', '223.38.10.231', '2022-02-14 14:50']
    ['carrier_kr_false_fe80::10cb:5533:13c9:c1b7%en0', '223.38.87.95', '2022-02-14 14:50']
    ['carrier_kr_false_100.95.87.158', '223.39.212.56', '2022-02-14 14:50']
'''

def Find_Country(ip):    
    raw_sips, raw_dips, raw_countries = [], [], []
    with open('C:/Users/ks.nam/Downloads/info.csv', 'rt') as fd:
        info = fd.read()
    raw_sips, raw_dips, raw_countries = info.split('\n')
    sips = raw_sips.split(',')
    dips = raw_dips.split(',')
    countries = raw_countries.split(',')

    ip = list(map(lambda x: int(x), ip.split('.')))

    for sip, dip, country in zip(sips, dips, countries): 
        sip = list(map(lambda x: int(x), sip.split('.'))) 
        dip = list(map(lambda x: int(x), dip.split('.')))
        # 대역대별 section을 4개 나누어 비교
        if sip[0] <= ip[0] <= dip[0]:
            if sip[1] <= ip[1] <= dip[1]:
                if sip[2] <= ip[2] <= dip[2]:                                        
                    # KR이 아닐경우
                    if int(country.find("KR")) == -1:                            
                        ip_list_global.append('{}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))                                                
                        ip_list_write[ip_identity(country)]='{}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3])
                    else:                        
                        print(' [+] {}.{}.{}.{}({})'.format(ip[0], ip[1], ip[2], ip[3], country))                         
                        ip_list_write[ip_identity(country)]='{}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3])
                    break
    
def write_to_file_from_list(filepath, dataset):
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        f.write('ip, country, country_name \n')
        for key, value in dataset.items():            
            f.write('{},{},{} \n'.format(value, key, country_code_translate[str(key)]))
            #print('ip{}의 국가코드는 {}입니다.'.format(value, key))

def read_dataset(filepath):
    #raw data -> storage
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for c in reader:
            print(c)
    #main sub-thread
    with open(filepath, 'r', encoding='euc-kr') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        for field in fields:
            print('{:>15}'.format(field), end='')           
        print()
        for row in reader:
            for field in fields:
                ip_list.append(row[field])
                print('{:>15}'.format(row[field]), end='')
            print()

def print_fomatting(ip_cnt, len_ip_list_global, ip_list_global):
    print("[result] 검증 IP는 총 {}개 입니다".format(ip_cnt))
    print("[result] 그중 해외 IP는 총 {}개가 발견 되었습니다".format(len_ip_list_global))
    print(ip_list_global)

if __name__ == '__main__':    
    #점검시작
    read_dataset('C:/Users/ks.nam/Downloads/connect(dummy).csv')
    #검증시작
    for x in ip_list:
        verify_cnt = len(re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", x))        
        if verify_cnt > 0:
            ip_cnt=ip_cnt+1
            result_global_ip_cnt=Find_Country(x)            
    print_fomatting(ip_cnt, len(ip_list_global), ip_list_global)
    
    #결과파일 생성
    write_to_file_from_list('C:/Users/ks.nam/Downloads/result_{}.csv'.format(datetime.date.today()), ip_list_write)
    
    
'''
(unit test 1) IP type 식별
for x in ip_list:        
        if(len(x) <= 15):
        #if(ord(x[0]) >= 48 and ord(x[0]) <= 57):
            print(x)

(unit test 2) 수집된 정보를 국가코드 정보를 CSV 파일에 쓰기
def write_to_file_from_list(filepath):
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(sample_list)
'''
