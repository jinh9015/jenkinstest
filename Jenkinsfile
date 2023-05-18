pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Build and Push") {
            steps {
                script {
                    def imageName = "jinh9015/jenkinstest"
                    def imageTag = env.BUILD_NUMBER

                    // Docker Compose 실행을 위해 필요한 환경 변수 설정
                    env.IMAGE_NAME = "${imageName}:${imageTag}"
                    env.COMPOSE_PROJECT_NAME = "jenkinstest"

                    // Docker Compose를 사용하여 이미지 빌드 및 푸시
                    sh "docker-compose -f docker-compose.yaml build"
                    sh "docker-compose -f docker-compose.yaml push"
                }
            }
        }
    }
}

