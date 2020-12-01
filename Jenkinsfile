pipeline {
    agent { docker { image 'armysoldier93/flaskexample:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('test') {
            steps {
                sh 'python3 test.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
        
    }
}