pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                script {
                    dir('jenkinstest') {
                        // GitHub repository 클론
                        git url: 'https://github.com/jinh9015/jenkinstest.git'
                        // 디렉토리 내 파일 목록 확인
                        sh 'ls -la'
                    }
                }
            }
        }

        stage('Build and push Docker image') {
            steps {
                script {
                    dir('jenkinstest') {
                        // 도커 이미지 빌드 및 푸시를 위한 변수 설정
                        def dockerImageTag = "jinh9015/jenkinstest:${env.BUILD_NUMBER}"
                        def dockerHubCredentials = 'jinh9015'

                        // 도커 이미지 빌드
                        sh 'docker-compose -f docker-compose.yaml build'

                        // 빌드된 이미지 태그 변경
                        sh "docker tag jenh9015_jenkinstest:${env.BUILD_NUMBER} ${dockerImageTag}"

                        // 빌드된 이미지 푸시
                        docker.withRegistry('https://registry.hub.docker.com', dockerHubCredentials) {
                            sh "docker push ${dockerImageTag}"
                        }

                        // 빌드된 이미지 정보 출력
                        echo "Docker image pushed: ${dockerImageTag}"
                    }
                }
            }
        }
    }
}

