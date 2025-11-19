# AI HelpyChat QA Project


HelpyChat QA 프로젝트는 HelpyChat 서비스의 **핵심 기능 품질을 보증(QA)**하고

**테스트 자동화 기반 CI/CD 프로세스 구축**을 목표로 합니다.

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
<summary><strong>Allure 리포트 미리보기</strong></summary>

<img src="/uploads/55f9f3f73cca07ceaa629f89be7bc801/스크린샷_2025-11-18_171355.png" width="70%"/>

<br><br>

<img src="/uploads/4b68467f304729396accf9231a022cc5/스크린샷_2025-11-18_171342.png" width="70%"/>

</details>
<br>

## ▪️ 테스트 케이스 설계

### 설계 기준

테스트 케이스(TC)는 HelpyChat의 핵심 기능 품질을 보증하고,  **정상 동작 검증, 예외 처리, UI/권한/성능 테스트**를 모두 고려하였습니다.

<details>
<summary><strong>📌 상세보기</strong></summary>

#### 1️⃣ 자동화 가능 여부 3단계

- **자동화 가능 (Yes)**
  - UI 조작 가능 & 결과 검증 가능
  - 예시: 로그인, 버튼 클릭 후 결과 표시, 파일 생성 후 다운로드
  - 처리: 바로 자동화 대상

- **조건부 가능 (Later)**
  - UI 자동화 가능하지만 난이도/환경 의존/비동기 등으로 우선순위 낮음
  - 예시: PDF 업로드 후 AI 분석 결과 비교, 이미지 생성 픽셀 비교
  - 처리: 1차 자동화 제외 → 나중에 고려

- **자동화 어려움 (No)**
  - 사람이 눈으로 판단해야 하거나 UI 요소 없음, 랜덤성 높음
  - 예시: 생성 PPT 내용 품질 평가, 이미지 퀄리티, 디자인/문장 표현 평가
  - 처리: 수동 테스트 유지

---

#### 2️⃣ 자동화 가능 여부 체크 기준

> 체크 항목 5개 중 3개 이상 Yes → 자동화 가능  
> 1~2개 Yes → 조건부(Later)  
> 0개 Yes → 수동(No)

- ✅ ① 테스트 결과가 객관적으로 비교 가능한가?  
  - 텍스트, 숫자, HTTP 응답, 특정 UI 요소 존재 여부 등

- ✅ ② 테스트 흐름이 사용자 UI 조작으로 재현 가능한가?  
  - 클릭/입력/선택 등

- ✅ ③ 실행할 때마다 결과가 일관되는가?  
  - 랜덤성, AI 생성물 평가 제외

- ✅ ④ 테스트 수행에 사람이 판단할 일이 없는가?  
  - “문장이 자연스럽다” 등 주관적 평가는 No

- ✅ ⑤ 자동화로 얻는 이득이 있는가?  
  - 반복 테스트, 회귀 테스트, 매번 실행되는 기능 등

</details>
<br>

### 대표 테스트 케이스 미리보기

다음은 HelpyChat QA 프로젝트에서 작성한 **대표 테스트 케이스**입니다.

스크린샷으로 확인하거나, 🔗[전체 TC 구글 시트 보기](https://www.notion.so/%EA%B5%AC%EA%B8%80%EC%8B%9C%ED%8A%B8%EB%A7%81%ED%81%AC)에서 자세히 확인할 수 있습니다.

<img src="/uploads/f039be3218cc351b8f615aba72e44d8a/tc_sc.png" width="70%"/>

<br><br>

## ▪️ **기능 완료 현황 (Feature Completion Status)**

| 기능 구분 | 완료 현황 | 담당자 |
| --- | --- | --- |
| 💬 **채팅 고급 기능** | **19 / 19 (100%)** | 강해리 |
| 💭 **채팅 기본 기능** | **28 / 28 (100%)** | 이선아 |
| 🗂 **채팅 히스토리 기능** | **11 / 11 (100%)** | 최고은 |
| 💳 **빌링 기능** | **1 / 1 (100%)** | 김설아 |
| 👥 **계정·조직 기능** | **12 / 12 (100%)** | 김설아 |
| 🎛 **맞춤화 기능** | 20 / 20 (100%) | 김설아 & 최고은 |

<br>

## ▪️ 테스트 환경 및 필요 툴

테스트를 수행하기 위해 추가 아래 환경과 도구가 필요합니다.

- **Python**: 3.10 이상
- **Allure CLI**: 테스트 결과 리포트 시각화
- **Docker**: Jenkins CI/CD 환경 구성
- **Jenkins LTS**: 자동화 파이프라인
- 요구 라이브러리: `requirements.txt` 참조

<br>

## ▪️ 테스트 실행 방법 (로컬)

QAespa 테스트를 로컬 환경에서 실행하려면 다음 단계를 따르세요.

1. **테스트 실행 (master 브랜치)**

```bash
# project_root 이동
cd project_root

# 3개의 프로세스로 병렬 실행 (자신의 cpu 스펙의 맞게 갯수를 설정)
pytest -n 3 

# 병렬 실행 없이 전체 실행
pytest -v
```

1. **Allure 리포트 확인**

```bash
# 테스트 결과를 시각화하여 브라우저에서 확인
allure serve reports/allure/results
```

<br>

## ▪️ QAespa 프로젝트 핵심 성과 & 강점

### 주요 성과

- **병렬 실행**으로 테스트 시간 **40~60% 단축**
- **Allure Report 기반 시각화**로 테스트 품질 보고 체계 개선
- **Jenkins + Docker**를 활용한 자동화 테스트 파이프라인 구축
- **플러그인 기반 구조**로 재사용 가능한 테스트 자동화 설계
- 헬피챗 **누락 결함** 10개 발견

### 프로젝트 강점

- Allure 리포트 사용으로 **개발자와 기획자가 손쉽게 테스트 결과 확인**
- CI/CD 자동화 적용으로 **QA 수동 실행 불필요**
- Flaky 테스트 자동 재시도 적용 (`rerun plugin`)으로 **테스트 안정성 확보**

<br>

## ▪️ 기술 스택

| 분야 | 기술 / 도구 |
|------|-------------|
| **Testing** | ![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white) ![Pytest](https://img.shields.io/badge/Pytest-Automation-green?logo=pytest&logoColor=white) ![Selenium](https://img.shields.io/badge/Selenium-UI%20Automation-red?logo=selenium&logoColor=white) ![Xdist](https://img.shields.io/badge/Pytest--xdist-Parallel-orange) ![Rerun](https://img.shields.io/badge/Pytest--rerunfailures-Flaky-blue) ![Allure](https://img.shields.io/badge/Allure-Report-important) |
| **DevOps** | ![Jenkins](https://img.shields.io/badge/Jenkins-CI-orange?logo=jenkins&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker&logoColor=white) ![GitLab](https://img.shields.io/badge/GitLab-VCS-red?logo=gitlab&logoColor=white) ![Webhook](https://img.shields.io/badge/Webhook-Trigger-purple) |

<br>

## ▪️서비스 아키텍처

<br>

## ▪️ 트러블슈팅


- **테스트 중 TimeExecution 오류 발생**
  - **문제**: 전체 테스트를 실행시 간헐적으로 **`TimeExecution`** 에러 발생
  - **해결방법**: **`pytest-rerunfailures`**를 적용, 실패한 테스트를 자동으로 재실행
  - **결과**: 테스트 실패율 **9.23%** 감소
  - [🔗 불안정 테스트, Rerun으로 안정화](#)
  <br>
- **Jenkins 에러 파일 발생**
  - **문제**: Jenkins 실행시 전체에서 Error 파일 28% 발생
  - **해결방법**: conftest.py 파일에 **Headless** 옵션 추가
  - **결과**: Error 파일 전체 비율 **4.6%**까지 감소
  - [🔗 Jenkins 에러 발생과 Headless 설정으로 해결한 과정](#)
  <br>
- **DOM 렌더링 타이밍에 따른 StaleElementReferenceException 발생**
  - **문제**: 검색 테스트 실행 시 `find_element()` 가 React 렌더링 완료 이전에 실행되어 `StaleElementReferenceException` 에러 발생
  - **해결방법**: 요소 탐색 전에 대기를 배치하여 DOM 업데이트 시간 확보
  - **결과**: 오류 재현율 100% → 0%로 감소, 테스트 케이스 정상 통과
  - [🔗 적절한 대기 타이밍과 DOM 렌더링 지연 대응 방법](https://www.notion.so/DOM-2b0990eaa28f80f581f6f4fea2a35a3b?pvs=21)


