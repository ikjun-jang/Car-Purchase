pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                //sh 'sudo apt-get update'
                //sh 'sudo apt-get install python3.6'
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install -r ./backend/requirements.txt'
                sh 'sudo systemctl start postgresql'
                sh 'sudo -u postgres createdb car'
                sh 'source ./backend/setup.sh'
                //sh 'psql -d car -U postgres -a -f car.psql'
            }
        }
        stage('test') {
            steps {
                sh 'sudo -u postgres createdb car_test'
                sh 'python3 ./backend/test_app.py'
                sh 'sudo -u postgres dropdb car_test'
            }
        }
        stage('run') {
            steps {
                sh 'nohup python3 ./backend/app.py &'
            }
        }
    }
    post {
        sh 'sudo -u postgres createdb car'
    }
}