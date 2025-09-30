
## Black 이란? 

공식문서: https://black.readthedocs.io/en/stable/#
Source Code: https://github.com/psf/black


- code formatter
- 코드 스타일을 자동으로 통일시켜줌 
- 코드의 들여쓰기, 줄 바꿈, 공백 등 스타일을 자동으로 맞춰줌
- 코드 리뷰가 쉬워짐 
- Uncompromising code formatter 라서 대부분의 옵션이 고정되어 있음. 팀워크로 작업을 할 경우 팀 전체가 같은 코드 스타일을 써야 함. 

## 기초 사용법 

- 코드 파일 자동으로 정리 
```
black my_script.py
```

- 프로젝트 폴더 전체 포매팅
```
black . 
```

- 코드 바뀜 미리보기 
```
black --diff my_script.py
```

- 코드 스타일 준수 점검 
``` 
black --check .
```


