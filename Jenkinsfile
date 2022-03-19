pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                //sh 'sudo apt-get update'
                //sh 'sudo apt-get install python3.6'
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('run') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}