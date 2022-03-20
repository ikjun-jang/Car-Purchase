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
                sh 'if [ "$( psql -tAc "SELECT 1 FROM pg_database WHERE datname='car'" )" = '1' ] then sudo -u postgres createdb car'
                sh 'source ./backend/setup.sh'
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