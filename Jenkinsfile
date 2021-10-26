pipeline {
     agent any
     stages {
          stage('Run python script') {
            steps {
                sh 'python3 calculator.py'
            }
        }
        stage('Create docker image') {
            steps {
                sh 'docker build -t iimann/calculator .'
            }
        }

     }
}
