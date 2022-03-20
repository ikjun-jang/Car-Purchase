pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                //sh 'sudo apt-get update'
                //sh 'sudo apt-get install python3.6'
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
                sh 'source setup.sh'
            }
        }
        stage('run') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }
    }
}