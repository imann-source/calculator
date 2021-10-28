pipeline {
     agent any
     stages {
            stage('Create docker image') {
                 steps {
                     sh 'sudo docker build -t iimann/calculator .'
                 }
            }
          stage('Run python script') {
            steps {
                sh 'python3 ./calculator.py'
            }
          }

     }
}
