pipeline {
     agent any
     stages {
          stage("Compile") {
               steps {
                    sh "python3 calculator.py"
               }
          }
               }
          }
          stage("Package") {
               steps {
                    sh "python3 build"
               }
          }

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
     }
}