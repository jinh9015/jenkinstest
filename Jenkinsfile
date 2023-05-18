pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                checkout scm
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
                    credentialsId: 'DockerHub',
                    usernameVariable: 'DOCKER_USER_ID',
                    passwordVariable: 'DOCKER_USER_PASSWORD'
                )]) {
                    script {
                        sh "docker tag jinh9015/jenkinstest:latest ${env.DOCKER_USER_ID}/jenkinstest:${env.BUILD_NUMBER}"
                        sh "docker login -u ${env.DOCKER_USER_ID} -p ${env.DOCKER_USER_PASSWORD}"
                        sh "docker push ${env.DOCKER_USER_ID}/jenkinstest:${env.BUILD_NUMBER}"
                    }
                }
            }
        }
    }
}

