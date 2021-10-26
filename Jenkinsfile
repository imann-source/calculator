pipeline {
     agent any
     stages {
          stage("Docker build") {
               steps {
                    sh "docker build -t iimann/calculator ."
               }
          }
          stage("Docker push") {
               steps {
                    sh "docker push iimann/calculator"
               }
          }
          stage("Compile") {
               steps {
                    sh "python3 calculator.py"
               }
          }

     }
}
