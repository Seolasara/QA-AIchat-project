# AI HelpyChat QA Project


HelpyChat은 AI 기반 멀티모달 챗봇 서비스이며, 본 프로젝트는 해당 서비스의 품질을 보증하기 위해 **272개 테스트 케이스 설계 및 자동화 구축**을 목표로 수행되었습니다.


**QA 프로세스, 자동화 코드, CI 파이프라인, 테스트 리포트**까지 실제 서비스 환경에 맞춰 구성했습니다.


<br>

## ▪️**HelpyChat 핵심 기능 요약**

HelpyChat 기능명세서를 기반으로 테스트 범위를 정의하였으며 주요 기능은 다음과 같습니다.
<br><br>

| 구분 | 핵심 기능 |
| --- | --- |
| **계정 / 조직 관리** | SSO 로그인, 언어 설정 |
| **빌링 & 이용내역** | 크레딧 조회 |
| **채팅 & 히스토리** | AI 채팅, 멀티모달 입력(문서/이미지), 대화 검색·수정·히스토리 관리 |
| **AI 고급 기능** | 파일 분석, PPT 자동 생성, 이미지 생성, 퀴즈 생성, 구글 검색, 심층 조사, 차트 생성 |
| **커스텀 에이전트** | 에이전트 생성/편집/삭제, 규칙 및 기능 설정, 공개 범위 |


<br>

## ▪️테스트 결과 요약

| **항목** | **결과** |
| --- | --- |
| **총 테스트 케이스** | **272개** |
| **자동화 성공 케이스** | **90개** |
| **Jenkins 성공률 평균** | **83.7%** |

<br>

<details>
<summary><strong>📌 Allure 리포트 미리보기</strong></summary>

<img width="2552" height="1351" alt="readme용 allure 리포트1" src="https://github.com/user-attachments/assets/0ae7a926-7d87-4c9d-accd-c99ea1b61a92" />


<br>

<img width="2559" height="1363" alt="readme용 allure 리포트2" src="https://github.com/user-attachments/assets/41e5e405-e8b9-4926-9b46-b26ad72f9ad9" />



</details>

<br>

## ▪️ 테스트 케이스 설계

### 설계 기준

HelpyChat의 핵심 기능 품질을 보증하기 위해 다음을 고려해 TC를 설계했습니다.  

* 기능 정상동작 검증  
* 예외 처리  
* UI 요소 확인  
* 반복 테스트 및 회귀 테스트 가능성
  
<br>

<details>
<summary><strong>📌 우선순위 선정 기준 상세보기</strong></summary>

#### 1️⃣ **High**

  - 핵심 기능
  - 비즈니스 영향 큼
  - 사용자 사용 빈도 매우 높음
  - 자동화 효율 높음

#### 2️⃣ **Medium**

  - 중요한 기능
  - 부분 장애 시 우회 가능
  - 사용자 사용 빈도 보통

#### 3️⃣ **Low**

  - 부가 기능
  - 장애 발생해도 영향 적음
  - 단순 시각적 요소
  
<br>    
    
</details>

<details>
<summary><strong>📌 자동화 선정 기준 상세보기</strong></summary>

#### 1️⃣ **자동화 가능 여부 구분**

  - Yes: UI 조작 가능 & 결과 검증 가능
  - Later: 가능하지만 난이도/환경 의존 높음
  - No: 주관적 판단 필요, 랜덤성 높음

#### 2️⃣ **자동화 판단 체크리스트**

  - 결과 비교 객관성
  - UI 기반으로 재현성 가능 여부
  - 실행 시 결과 일관성 여부
  - 사람 판단 필요 여부
  - 자동화 효율성 여부

</details>
<br>

### - 대표 테스트 케이스 미리보기

<img width="2650" height="1076" alt="readme용 tc미리보기" src="https://github.com/user-attachments/assets/b51927cf-5dcc-45f1-86a1-3388e1a9d5fa" />

<br>
<br>

🔗[전체 TC 구글 시트 보기](https://docs.google.com/spreadsheets/d/1jvFSFtPDwgU6eHVqLnl6Cowe_rB_cDTxe5_iPNAvspA/edit?gid=136598138#gid=136598138)에서 자세히 확인할 수 있습니다.

<br>


## ▪️ 테스트 환경 및 필요 툴

- **Python**: 3.10+
- **Pytest / Selenium / Xdist / Rerun**
- **Allure CLI**: 테스트 결과 리포트 시각화
- **Jenkins LTS**: CI 파이프라인
- `requirements.txt` 참조

<br>

## ▪️ 테스트 실행 방법 (로컬)

#### ▪️**Window**

```bash
# 가상환경 설정 
 python -m venv venv 
 venv\Scripts\activate

 pip install --upgrade pip

 # requirement 설치
 pip install -r requirements.txt

# project_root 이동
 cd project_root

# 3개의 프로세스로 병렬 실행 (자신의 cpu 스펙의 맞게 갯수를 설정)
 pytest -n 3 

# 병렬 실행 없이 전체 실행
 pytest -v
```
#### ▪️**Mac**
```bash
# 가상환경 설정 
  python3 -m venv venv 
  source venv/bin/activate

  pip install --upgrade pip

 # requirement 설치
  pip install -r requirements.txt

# project_root 이동
 cd project_root

# 3개의 프로세스로 병렬 실행 (자신의 cpu 스펙의 맞게 갯수를 설정)
 pytest -n 3 

# 병렬 실행 없이 전체 실행
 pytest -v
```


#### **Allure 리포트 확인**

```bash
# 테스트 결과를 시각화하여 브라우저에서 확인
allure serve reports/allure/results
```

<br>

<details> <summary><strong>▪️Allure 설치 가이드</strong></summary> <br>
1️⃣ Python 패키지 설치 (공통)
pip install pytest allure-pytest

2️⃣ Allure CLI 설치

▪️macOS
```bash
brew install allure
```

설치 확인
```bash
allure --version
```

▪️Windows

최신 Allure ZIP 다운로드
👉 https://github.com/allure-framework/allure2/releases

압축 해제

bin 폴더를 환경 변수 PATH에 추가
예시:
```bash
C:\allure-2.27.0\bin
```

설치 확인
```bash
allure --version
```

<br> </details>
<br>


## ▪️ 프로젝트 핵심 성과 & 강점

### 주요 성과

- **병렬 실행(Xdist)** 으로 테스트 시간 **40~60% 단축**
- **Allure Report 기반 시각화**로 보고 체계 개선
- **Jenkins CI**로 자동 테스트 파이프라인 구축
- **플러그인 기반 구조**로 재사용성 높은 테스트 프레임워크 설계
- 헬피챗 **누락 결함** 9개 발견

### 강점

- Allure 리포트 사용으로 **개발자와 기획자가 손쉽게 테스트 결과 확인**
- CI 자동화로 **QA 수동 실행 부담 감소**
- Flaky 테스트에 대해 (`rerun plugin`) 적용으로 **테스트 안정성 개선**

<br>

## ▪️ 기술 스택

| 분야 | 기술 / 도구 |
|------|-------------|
| **Testing** | ![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white) ![Pytest](https://img.shields.io/badge/Pytest-Automation-green?logo=pytest&logoColor=white) ![Selenium](https://img.shields.io/badge/Selenium-UI%20Automation-red?logo=selenium&logoColor=white) ![Xdist](https://img.shields.io/badge/Pytest--xdist-Parallel-orange) ![Rerun](https://img.shields.io/badge/Pytest--rerunfailures-Flaky-blue) ![Allure](https://img.shields.io/badge/Allure-Report-important) |
| **DevOps** | ![Jenkins](https://img.shields.io/badge/Jenkins-CI-orange?logo=jenkins&logoColor=white) ![GitLab](https://img.shields.io/badge/GitLab-VCS-red?logo=gitlab&logoColor=white) ![Webhook](https://img.shields.io/badge/Webhook-Trigger-purple) |

<br>

## ▪️서비스 아키텍처


![readme용 아키텍처](https://github.com/user-attachments/assets/7480517f-df53-4e91-ac3a-2ae7acb5610b)


<br>

## ▪️ 트러블슈팅

  - **Jenkins 에러 파일 발생**
  - **문제**: Jenkins 실행시 전체에서 Error 파일 28% 발생
  - **해결 방법**: conftest.py 파일에 **Headless** 옵션 추가
  - **결과**: Error 파일 전체 비율 **4.6%** 까지 감소
  - [🔗 Jenkins 에러 발생과 Headless 설정으로 해결한 과정](https://github.com/Seolasara/qa-project1/wiki/Jenkins-%EC%97%90%EB%9F%AC-%EB%B0%9C%EC%83%9D%EC%9D%84-Headless-%EC%84%A4%EC%A0%95%EC%9C%BC%EB%A1%9C-%ED%95%B4%EA%B2%B0%ED%95%9C-%EB%B0%A9%EB%B2%95)

<br>


