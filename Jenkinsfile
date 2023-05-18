pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                script {
                    // GitHub repository 클론
                    git url: 'https://github.com/jinh9015/jenkinstest.git'
                }
            }
        }
        
        stage('Build and push Docker image') {
            steps {
                script {
                    // 도커 이미지 빌드 및 푸시를 위한 변수 설정
                    def dockerImageTag = "jinh9015/jenkinstest:${env.BUILD_NUMBER}"
                    def dockerHubCredentials = 'jinh9015'
                    
                    // 도커 이미지 빌드
                    docker.withRegistry('https://registry.hub.docker.com', dockerHubCredentials) {
                        def dockerImage = docker.build(dockerImageTag, '.')
                        dockerImage.push()
                    }
                    
                    // 빌드된 이미지 정보 출력
                    echo "Docker image pushed: ${dockerImageTag}"
                }
            }
        }
    }
}

