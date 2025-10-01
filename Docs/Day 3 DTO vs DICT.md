
## DTO (Data Transfer Object)란?

DTO는 데이터 전송 객체로, API 요청/응답에서 사용되는 데이터 구조를 정의함. 

### 왜 DTO를 사용하는가?

1. 타입 안전성: Pydantic으로 데이터 검증
2. API 문서화: 자동으로 OpenAPI 스키마 생성
3. 코드 가독성: 명확한 데이터 구조 정의
4. 유지보수성: 데이터 구조 변경 시 한 곳에서 관리

## 장점 

### 1. 타입 안전성

- 잘못된 타입 전달 시 에러 발생
response = CreateMeetingResponse(url_code=123)  # int -> str 에러

### 2. 자동 문서화

- FastAPI가 자동으로 OpenAPI 스키마 생성
- API 문서에서 필드 설명 확인 가능

### 3. 데이터 검증
필수 필드 누락 시 에러
response = CreateMeetingResponse()  # url_code 누락 에러

