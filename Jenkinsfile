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
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub')
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t lloydmatereke/jenkins-docker-hub .'
      }
    }
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Push') {
      steps {
        sh 'docker push lloydmatereke/jenkins-docker-hub'
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
