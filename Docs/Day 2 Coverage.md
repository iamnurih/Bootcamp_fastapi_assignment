## Coverage 란? 

공식문서: https://coverage.readthedocs.io/en/7.10.7/
Source Code: https://github.com/nedbat/coveragepy

- 내 코드 테스트가 전체 코드의 몇 퍼센티지를 확인했는지 알려줌 
- 테스크가 되지 않은 부분을 찾아서 꼼꼼히 검사 가능 
- 테스트 누락된 부분을 쉽게 확인 할 수 있음 


## 기초 사용법 

- 설치 
``` 
pip install coverage
```

- 커버리지 체크 후 실행

```
coverage run -m pytest
```

- 결과 요약 
```
coverage html 
```