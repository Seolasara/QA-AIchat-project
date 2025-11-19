# --- 1. 베이스 이미지 ---
FROM eclipse-temurin:17-jdk-jammy

ENV WORKDIR=/app
ENV ALLURE_DIR=/app/reports/allure

RUN mkdir -p ${WORKDIR} ${ALLURE_DIR}
WORKDIR ${WORKDIR}

RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip curl unzip git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -o /tmp/allure.zip -L https://github.com/allure-framework/allure2/releases/download/2.27.1/allure-2.27.1.zip && \
    unzip /tmp/allure.zip -d /opt/ && \
    ln -s /opt/allure-2.27.1/bin/allure /usr/bin/allure && \
    rm /tmp/allure.zip

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY project_root/ ./project_root/

CMD ["pytest", "project_root/tests", "--alluredir=reports/allure", "--capture=tee-sys", "--junit-xml=reports/all-results.xml"]
