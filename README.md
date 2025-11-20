# AI HelpyChat QA Project


HelpyChat QA 프로젝트는 HelpyChat 서비스의 **핵심 기능 품질을 보증(QA)** 하고

**테스트 자동화 기반 CI 프로세스 구축**을 목표로 합니다.

<br>

## ▪️**HelpyChat 핵심 기능**

**HelpyChat**은 엘리스 트랙에서 개발한 **통합형 AI 솔루션**입니다.

🔗[HelpyChat 사이트 살펴보기](https://qaproject.elice.io/ai-helpy-chat?utm_source=chatgpt.com)

| 구분 | 핵심 기능 |
| --- | --- |
| **계정 / 조직 관리** | SSO 로그인, 권한 기반 접근 제어, 조직 구성원 초대·관리 |
| **빌링 & 이용내역** | 크레딧 충전/자동충전, 결제수단 관리, 사용 이력 조회 |
| **채팅 & 히스토리** | AI 채팅, 멀티모달 입력(문서/이미지), 대화 검색·수정·히스토리 관리 |
| **AI 고급 기능** | 파일 분석, PPT 자동 생성, 이미지 생성, 퀴즈 생성, 구글 검색, 심층 조사, 차트 생성 |
| **커스텀 에이전트** | 에이전트 생성/편집/삭제, 규칙 및 기능 설정, 공개 범위 제어 |


<br>

## ▪️테스트 결과 요약

| **항목** | **결과** |
| --- | --- |
| **총 테스트 케이스** | **272개** |
| **자동화 성공 케이스** | **90개** |
| **Jenkins 성공률 평균** | **70.97%** |

<br>

<details>
<summary><strong>📌 Allure 리포트 미리보기</strong></summary>

<img src="/uploads/e81340c323d1980f7c2b22fe8c0a58ce/스크린샷_2025-11-18_171355.png" width="70%"/>

<br>

<img src="/uploads/406677cfd02704d2621180da8499888b/스크린샷_2025-11-18_171342.png" width="70%"/>


</details>

<br>

## ▪️ 테스트 케이스 설계

### 설계 기준

테스트 케이스(TC)는 HelpyChat의 핵심 기능 품질을 보증하고,  **정상 동작 검증, 예외 처리, UI/권한/성능 테스트**를 모두 고려하였습니다.

<details>
<summary><strong>📌 자동화 선정 기준 상세보기</strong></summary>

#### 1️⃣ 자동화 가능 여부 3단계

- **자동화 가능 (Yes)**
  - UI 조작 가능 & 결과 검증 가능
  - 예시: 로그인, 버튼 클릭 후 결과 표시, 파일 생성 후 다운로드
  - 처리: 바로 자동화 대상
<br>

- **조건부 가능 (Later)**
  - UI 자동화 가능하지만 난이도/환경 의존/비동기 등으로 우선순위 낮음
  - 예시: PDF 업로드 후 AI 분석 결과 비교, 이미지 생성 픽셀 비교
  - 처리: 1차 자동화 제외 → 나중에 고려
<br>

- **자동화 어려움 (No)**
  - 사람이 눈으로 판단해야 하거나 UI 요소 없음, 랜덤성 높음
  - 예시: 생성 PPT 내용 품질 평가, 이미지 퀄리티, 디자인/문장 표현 평가
  - 처리: 수동 테스트 유지

---

#### 2️⃣ 자동화 가능 여부 체크 기준

> 체크 항목 5개 중 3개 이상 Yes → 자동화 가능  
> 1~2개 Yes → 조건부(Later)  
> 0개 Yes → 수동(No)

- 테스트 결과가 객관적으로 비교 가능한가?  
  텍스트, 숫자, HTTP 응답, 특정 UI 요소 존재 여부 등

- 테스트 흐름이 사용자 UI 조작으로 재현 가능한가?  
  클릭/입력/선택 등

- 실행할 때마다 결과가 일관되는가?  
  랜덤성, AI 생성물 평가 제외

- 테스트 수행에 사람이 판단할 일이 없는가?  
  “문장이 자연스럽다” 등 주관적 평가는 No

- 자동화로 얻는 이득이 있는가?  
  반복 테스트, 회귀 테스트, 매번 실행되는 기능 등

</details>
<br>

### 대표 테스트 케이스 미리보기

다음은 HelpyChat QA 프로젝트에서 작성한 **대표 테스트 케이스**입니다.

스크린샷으로 확인하거나, 🔗[전체 TC 구글 시트 보기](https://docs.google.com/spreadsheets/d/1jvFSFtPDwgU6eHVqLnl6Cowe_rB_cDTxe5_iPNAvspA/edit?gid=136598138#gid=136598138)에서 자세히 확인할 수 있습니다.

<img src="/uploads/c3cec26bfad645f1eecb0dec4692ac25/tc_sc.png" width="70%"/>

<br><br>

## ▪️ **기능 완료 현황 (Feature Completion Status)**

| 기능 구분 | 완료 현황 | 담당자 |
| --- | --- | --- |
| 💬 **채팅 고급 기능** | **19 / 19 (100%)** | 강해리 |
| 💭 **채팅 기본 기능** | **28 / 28 (100%)** | 이선아 |
| 🗂 **채팅 히스토리 기능** | **11 / 11 (100%)** | 최고은 |
| 💳 **빌링 기능** | **1 / 1 (100%)** | 김설아 |
| 👥 **계정·조직 기능** | **12 / 12 (100%)** | 김설아 |
| 🎛 **맞춤화 기능** | **20 / 20 (100%)** | 김설아 & 최고은 |

<br>

## ▪️ 테스트 환경 및 필요 툴

테스트를 수행하기 위해 추가 아래 환경과 도구가 필요합니다.

- **Python**: 3.10 이상
- **Allure CLI**: 테스트 결과 리포트 시각화
- **Jenkins LTS**: 자동화 파이프라인
- 요구 라이브러리: `requirements.txt` 참조

<br>

## ▪️ 테스트 실행 방법 (로컬)

QAespa 테스트를 로컬 환경에서 실행하려면 다음 단계를 따르세요.

1. **테스트 실행 (master 브랜치)**

▪️window 버전

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
▪️mac 버전
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


2. **Allure 리포트 확인**

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

## ▪️ QAespa 프로젝트 핵심 성과 & 강점

### 주요 성과

- **병렬 실행**으로 테스트 시간 **40~60% 단축**
- **Allure Report 기반 시각화**로 테스트 품질 보고 체계 개선
- **Jenkins**를 활용한 자동화 테스트 파이프라인 구축
- **플러그인 기반 구조**로 재사용 가능한 테스트 자동화 설계
- 헬피챗 **누락 결함** 9개 발견

### 프로젝트 강점

- Allure 리포트 사용으로 **개발자와 기획자가 손쉽게 테스트 결과 확인**
- CI 자동화 적용으로 **QA 수동 실행 불필요**
- Flaky 테스트 자동 재시도 적용 (`rerun plugin`)으로 **테스트 안정성 확보**

<br>

## ▪️ 기술 스택

| 분야 | 기술 / 도구 |
|------|-------------|
| **Testing** | ![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white) ![Pytest](https://img.shields.io/badge/Pytest-Automation-green?logo=pytest&logoColor=white) ![Selenium](https://img.shields.io/badge/Selenium-UI%20Automation-red?logo=selenium&logoColor=white) ![Xdist](https://img.shields.io/badge/Pytest--xdist-Parallel-orange) ![Rerun](https://img.shields.io/badge/Pytest--rerunfailures-Flaky-blue) ![Allure](https://img.shields.io/badge/Allure-Report-important) |
| **DevOps** | ![Jenkins](https://img.shields.io/badge/Jenkins-CI-orange?logo=jenkins&logoColor=white) ![GitLab](https://img.shields.io/badge/GitLab-VCS-red?logo=gitlab&logoColor=white) ![Webhook](https://img.shields.io/badge/Webhook-Trigger-purple) |

<br>

## ▪️서비스 아키텍처

<img src="/uploads/cf6dcaf49bd8c9ad162c45c938097531/제목을_입력해주세요__1_.jpg" width="70%"/>


<br>

## ▪️ 트러블슈팅


- **테스트 중 TimeExecution 오류 발생**
  - **문제**: 전체 테스트를 실행시 간헐적으로 **`TimeExecution`** 에러 발생
  - **해결 방법**: **`pytest-rerunfailures`**를 적용, 실패한 테스트를 자동으로 재실행
  - **결과**: 테스트 실패율 **9.23%** 감소
  - [🔗 불안정 테스트, Rerun으로 안정화](https://kdt-gitlab.elice.io/kanghaelee/team2_project/-/wikis/%EB%B6%88%EC%95%88%EC%A0%95-%ED%85%8C%EC%8A%A4%ED%8A%B8,-Rerun%EC%9C%BC%EB%A1%9C-%EC%95%88%EC%A0%95%ED%99%94%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)
  <br>
- **Jenkins 에러 파일 발생**
  - **문제**: Jenkins 실행시 전체에서 Error 파일 28% 발생
  - **해결 방법**: conftest.py 파일에 **Headless** 옵션 추가
  - **결과**: Error 파일 전체 비율 **4.6%** 까지 감소
  - [🔗 Jenkins 에러 발생과 Headless 설정으로 해결한 과정](https://kdt-gitlab.elice.io/kanghaelee/team2_project/-/wikis/Jenkins-%EC%97%90%EB%9F%AC-%EB%B0%9C%EC%83%9D%EC%9D%84-Headless-%EC%84%A4%EC%A0%95%EC%9C%BC%EB%A1%9C-%ED%95%B4%EA%B2%B0%ED%95%9C-%EB%B0%A9%EB%B2%95)
  <br>
- **DOM 렌더링 타이밍에 따른 StaleElementReferenceException 발생**
  - **문제**: 검색 테스트 실행 시 `find_element()` 가 React 렌더링 완료 이전에 실행되어 `StaleElementReferenceException` 에러 발생
  - **해결 방법**: 요소 탐색 전에 대기를 배치하여 DOM 업데이트 시간 확보
  - **결과**: 오류 재현율 100% → 0%로 감소, 테스트 케이스 정상 통과
  - [🔗 적절한 대기 타이밍과 DOM 렌더링 지연 대응 방법](https://kdt-gitlab.elice.io/kanghaelee/team2_project/-/wikis/%EC%A0%81%EC%A0%88%ED%95%9C-%EB%8C%80%EA%B8%B0-%ED%83%80%EC%9D%B4%EB%B0%8D%EA%B3%BC-DOM-%EB%A0%8C%EB%8D%94%EB%A7%81-%EC%A7%80%EC%97%B0-%EB%8C%80%EC%9D%91-%EB%B0%A9%EB%B2%95)
  <br>
- **기존 pytest-html 리포트를 Allure 리포트로 변경**
  - **문제**: pytest-html 리포트의 낮은 시인성과 제한적인 기능으로 비효율적인 테스트 분석이 이루어짐
  - **해결 방법**: pytest-html 설정 제거 및 Allure 플러그인 적용으로 리포트 생성 방식 전면 전환
  - **결과**: 가독성과 분석 기능이 향상된 Allure 리포트를 안정적으로 생성
  - [🔗 리포트 생성 방식 전환 방법](https://kdt-gitlab.elice.io/kanghaelee/team2_project/-/wikis/%EB%A6%AC%ED%8F%AC%ED%8A%B8-%EC%83%9D%EC%84%B1-%EB%B0%A9%EC%8B%9D-%EC%A0%84%ED%99%98-%EB%B0%A9%EB%B2%95)
  <br>
- **Allure 리포트 폴더 내 결과 파일 누적 문제 해결**
  - **문제**: 테스트 실행 시 Allure 결과 파일 및 캐시 누적으로 리포트가 뒤섞이며 폴더의 복잡도가 증가함
  - **해결 방법**: 테스트 실행 전 기존 Allure 결과 디렉토리를 자동 삭제하는 방식으로 폴더를 초기화하도록 변경
  - **결과**: 매 실행마다 최신 상태의 Allure 리포트만 생성되어 구조 단순화 및 관리 용이성 향상
  - [🔗 리포트 폴더 파일 누적 문제 해결 방법](https://kdt-gitlab.elice.io/kanghaelee/team2_project/-/wikis/%EB%A6%AC%ED%8F%AC%ED%8A%B8-%ED%8F%B4%EB%8D%94-%ED%8C%8C%EC%9D%BC-%EB%88%84%EC%A0%81-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95)


