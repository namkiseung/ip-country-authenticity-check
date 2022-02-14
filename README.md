[해외 IP 진위확인 프로그램 제작]

파일 리스트

	connect.csv : 핀트앱을 이용하는 고객의 NAT IP 정보가 들어있는 파익
	info.csv : 국가별 IP현황을 참고한 대역리스트를 정리한 파일 (referrer. KRNIC( https://krnic.or.kr ))
	verify_global_ip.py : 자체 제작된 해외IP진위확인 프로그램
	result_{datetime}.csv : 생성된 결과파일 (해외 ip로 식별된 데이터 포함)

실행명령어 

	커맨드쉘을 이용해 아래 명령어 입력.
	$ python verify_global_ip.py

프로그램 동작과정

	KISA(KRNIC)를 통해 국내/해외 IP를 구별할 수 있는 데이터셋 생성
	info.csv 파일을 통해 해외 IP 대역 식별 및 국가코드 매칭
	개발자에게 단말기 정보수집 내용 요청 → connect.csv 파일
	검증스크립트(verify_global.ip)를 실행
	개발실로부터 전달받은 csv 파일의 nat ip를 수집
	수집된 nat ip를 info.csv 의 데이터와 비교
	해외/국내 여부
	국가코드
	결과를 csv에 쓴다. (이때 국가코드와 이름을 매칭해여 같이 insert) 
	결과도출