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
                sh 'npm --prefix ./frontend install'
            }
        }
        stage('test') {
            steps {
                sh 'sudo -u postgres createdb car_test'
                sh 'python3 ./backend/test_app.py'
            }
        }
        stage('run') {
            steps {
                sh 'nohup python3 ./backend/app.py &'
                sh 'nohup npm --prefix ./frontend start &'
            }
        }
    }
    post {
        cleanup {
            sh 'sudo -u postgres dropdb car_test'
        }
    }
}