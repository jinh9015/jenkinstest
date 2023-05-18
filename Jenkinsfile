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
                        // docker-compose.yaml 파일을 사용하여 이미지 빌드
                        sh "docker-compose -f docker-compose.yaml build"
                        
                        // 빌드된 이미지 태그 변경
                        sh "docker tag jinh9015_jenkinstest:${env.BUILD_NUMBER} ${dockerImageTag}"
                        
                        // 빌드된 이미지 푸시
                        sh "docker push ${dockerImageTag}"
                    }
                    
                    // 빌드된 이미지 정보 출력
                    echo "Docker image pushed: ${dockerImageTag}"
                }
            }
        }
    }
}

