
## pytest란? 

공식문서: https://docs.pytest.org/en/stable/
https://pypi.org/project/pytest/
Source Code: https://github.com/pytest-dev/pytest

- 파이썬 프로그램이 제대로 동작하는지 자동으로 확인해주는 테스트 도구 
- 함수가 2+5를 계산했을 때 5가 나오는지 체크 
- test_로 시작하는 파일이나 함수명을 자동으로 찾아서 검사 해줌 
- TestClient를 보내 응답이 정상적인지 확인 가능 

## 기초사용법 

- 설치 
```
pip install pytest
```

- 테스트 실행 
```
pytest
```

- 특정 테스트만 실행 
```
pytest -k "이름"
```

- 결과보기 
```
#자세하게 보기 
pytest -v 

#print 문 보기 
pytest -s 

#html 문서 받기 
pip install pytest-html
pytest --html=report.html 

```