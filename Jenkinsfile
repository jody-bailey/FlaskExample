pipeline {
    agent { docker { image 'armysoldier93/flaskexample:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}