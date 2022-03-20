pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                //sh 'sudo apt-get update'
                //sh 'sudo apt-get install python3.6'
                sh 'pip3 install --upgrade pip'
                sh 'cd ${WORKSPACE}'
                sh 'ls'
                sh 'cd backend'
                sh 'ls'
                sh 'pip3 install -r requirements.txt'
                sh 'sudo -u postgres createdb car'
                sh 'source setup.sh'
                //sh 'psql -d car -U postgres -a -f car.psql'
            }
        }
        stage('run') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }
    }
}