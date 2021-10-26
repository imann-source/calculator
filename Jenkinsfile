pipeline {
     agent any
     stages {
          stage("Docker build") {
               steps {
                    sh "sudo docker build -t iimann/calculator ."
               }
          }
          stage("Docker push") {
               steps {
                    sh "sudo docker push iimann/calculator"
               }
          }
          stage("Compile") {
               steps {
                    sh "sudo docker run --name calculator --rm -d -p 80:80 iimann/calculator"
               }
          }

     }
}
