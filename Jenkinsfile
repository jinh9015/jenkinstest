pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Install Docker") {
            steps {
                script {
                    sh 'curl -fsSL https://get.docker.com -o get-docker.sh'
                    sh 'sh get-docker.sh'
                }
            }
        }

        stage("Build") {
            steps {
                script {
                    // Docker 빌드 실행
                    sh "docker build -t jinh9015/jenkinstest ."
                }
            }
        }

        stage("Tag and Push") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'jinh9015',
                    usernameVariable: 'DOCKER_USER_ID',
                    passwordVariable: 'DOCKER_USER_PASSWORD'
                )]) {
                    script {
                        sh "docker tag jinh9015/jenkinstest:latest ${DOCKER_USER_ID}/jenkinstest:${BUILD_NUMBER}"
                        sh "docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}"
                        sh "docker push ${DOCKER_USER_ID}/jenkinstest:${BUILD_NUMBER}"
                    }
                }
            }
        }
    }
}

