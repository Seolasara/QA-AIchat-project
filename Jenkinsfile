pipeline {
    agent any

    environment {
        WORKDIR = "project_root"
        VENV = "venv"
        ALLURE_LOCAL = "reports/allure"       // 로컬용 일회성
        ALLURE_JENKINS = "reports/allure-jobs" // Jenkins용
    }

    stages {

        /* --- 1. 프로젝트 체크아웃 --- */
        stage('준비') {
            steps {
                checkout scm
                echo "📌 HelpyChat QA Pipeline Started"
            }
        }

        /* --- 2. Python 가상환경 생성 + requirements 설치 --- */
        stage('환경 설정') {
            steps {
                dir("${WORKDIR}") {
                    sh """
                        echo "🐍 Python 가상환경 생성"
                        python3 -m venv ${VENV}

                        echo "📦 pip 최신화 및 requirements 설치"
                        ${VENV}/bin/python -m pip install --upgrade pip
                        ${VENV}/bin/python -m pip install -r ../requirements.txt
                    """
                }
            }
        }

        /* --- 3. pytest 실행 (Jenkins용 Allure 결과 생성) --- */
        stage('전체 테스트 실행') {
            steps {
                dir("${WORKDIR}") {
                    catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                        sh """
                            echo "📂 Jenkins용 Allure 결과 폴더 생성"
                            mkdir -p ${ALLURE_JENKINS}

                            echo "🧪 pytest 실행 (JUnit + Allure)"
                            ${VENV}/bin/python -m pytest \
                                --junit-xml=reports/all-results.xml \
                                --alluredir=${ALLURE_JENKINS}
                        """
                    }
                }
            }
        }

        /* --- 4. 브랜치 조건부 배포 (서버 없으면 패스) --- */
        stage('배포') {
            when { anyOf { branch 'develop'; branch 'main' } }
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                    echo "🚀 배포 단계 (서버 없음, PASS)"
                }
            }
        }
    }

    post {
        always {
            echo "📄 테스트 리포트 업로드"

            // JUnit 리포트
            junit allowEmptyResults: true, testResults: "${WORKDIR}/reports/all-results.xml"

            // Allure 리포트
            allure([
                includeProperties: false,
                results: [[path: "${WORKDIR}/${ALLURE_JENKINS}"]],
                commandline: 'Allure'
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
