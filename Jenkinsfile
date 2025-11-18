pipeline {
    agent any

    environment {
        WORKDIR = "project_root"
        VENV = "venv"
        ALLURE_DIR = "reports/allure"
    }

    stages {

        /* --- 1. 프로젝트 체크아웃 --- */
        stage('준비') {
            steps {
                checkout scm
                echo "📌 HelpyChat QA Pipeline Started"
                dir("${WORKDIR}") {
                    echo "📁 Working directory: ${WORKDIR}"
                }
            }
        }

        /* --- 2. Python 가상환경 생성 + 패키지 설치 + 전체 테스트 실행 --- */
        stage('전체 테스트 실행') {
            steps {
                dir("${WORKDIR}") {
                    sh """
                        # venv 생성
                        python3 -m venv ${VENV}

                        # venv 안 Python으로 pip 설치
                        ${VENV}/bin/python -m pip install --upgrade pip
                        ${VENV}/bin/python -m pip install -r requirements.txt
                        ${VENV}/bin/python -m pip install --upgrade --force-reinstall allure-pytest allure-python-commons pytest-cov

                        # venv 안 Python으로 pytest 실행 (pytest.ini 반영)
                        ${VENV}/bin/python -m pytest \
                            --junit-xml=reports/all-results.xml \
                            --cov=src \
                            --cov-report=html:reports/htmlcov \
                            --cov-report=xml:reports/coverage.xml \
                            --alluredir=${ALLURE_DIR}
                    """
                }
            }
        }

        /* --- 3. 브랜치 조건부 배포 --- */
        stage('배포') {
            when { anyOf { branch 'develop'; branch 'main' } }
            steps {
                echo "🚀 배포 단계 (현재는 메시지만 출력)"
            }
        }
    }

    post {
        always {
            // JUnit XML 업로드
            junit "${WORKDIR}/reports/all-results.xml"

            // Coverage Report 업로드
            publishHTML([
                reportDir: "${WORKDIR}/reports/htmlcov",
                reportFiles: 'index.html',
                reportName: 'Coverage Report'
            ])

            // Allure Report 업로드
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: "${WORKDIR}/${ALLURE_DIR}"]]
            ])
        }

        success {
            echo "✅ HelpyChat QA Pipeline ALL PASSED!"
        }

        failure {
            echo "❌ Pipeline FAILED — 확인 필요"
        }
    }
}
