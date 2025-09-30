
## Poetry 란? 

공식문서: https://python-poetry.org/docs/
source code: https://github.com/python-poetry/poetry

- 파이썬에서 종속성 관리와 패키지를 위한 도구이다. 
- 프로젝트가 종속되어 있는 라이브러리를 선언하고, 설치 및 업데이트 등 관리를 해준다. 
- 반복적인 설치가 가능하도록 lockfile을 제공한다.  그래서 매번 pip freeze -> requirements.txt를 할 필요가 없어진다. 
- 프로젝트의 python 버전과, 필요한 라이브러리를 pyproject.toml로 관리해줌 
- poetry install 명령으로 모든 의존성을 자동으로 설치한다 
- 별도의 가상 환경을 만들어서 프로젝트별로 독립적인 환경을 보장한다 


##  기초 사용법

- 새로운 프로젝트 만들기: 
	 ``` poetry new 프로젝트이름```

- 기존 프로젝트에 환경 초기화:
	```poetry init```
	
- 필요한 라이브러리 추가:
	```  poetry add 라이브러리명 ```	```

- 가상환경 접속/종료:
``` 
poetry shell (가상환경 진입)
poetry exit (종료)
```


