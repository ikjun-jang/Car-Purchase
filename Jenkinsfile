pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install -r ./backend/requirements.txt'
                sh 'sudo systemctl start postgresql'
                sh 'sudo -u postgres createdb car'
                sh 'source ./backend/setup.sh'
                sh '${WORKSPACE}/frontend/npm install'
            }
        }
        stage('test') {
            steps {
                sh 'sudo -u postgres createdb car_test'
                sh 'python3 ${WORKSPACE}/backend/test_app.py'
            }
        }
        stage('run') {
            steps {
                sh 'nohup python3 ${WORKSPACE}/backend/app.py &'
                sh '${WORKSPACE}/frontend/nohup npm start'
            }
        }
    }
    post {
        cleanup {
            //sh 'sudo -u postgres dropdb car'
            sh 'sudo -u postgres dropdb car_test'
        }
    }
}