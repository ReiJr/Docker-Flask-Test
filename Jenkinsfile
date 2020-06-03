
node {
    checkout scm

    // Pega o commit id para ser usado de tag (versionamento) na imagem
    sh "echo Começo"
    sh "git rev-parse --short HEAD > commit-id"
    def tag = sh returnStdout: true, script: 'cat commit-id'
    
    // configura o nome da aplicação, o endereço do repositório e o nome da imagem com a versão
    appName = 'app'
    def registryHost = sh returnStdout: true, script: 'curl ifconfig.me'
    host = "${registryHost}:30400/"
    url = "${host}${appName}:${tag}"
    image = url.replaceAll("\\s","")
    
    
    stage('Build') {
                def customImage = docker.build("$image")
            }
    stage('Push') {
            
                customImage.push()
            
            }
    stage('Deploy') {
                echo 'Deploying....'
                input "Deploy to PROD?"
                customImage.push('latest')
                sh "kubectl apply -f https://raw.githubusercontent.com/ReiJr/Docker-Flask-uWSGI/master/k8s_app.yaml"
                sh "kubectl set image deployment app app=${image} --record"
                sh "kubectl rollout status deployment/app"
            
        }
    }

/*
node {

    checkout scm

    // Pega o commit id para ser usado de tag (versionamento) na imagem
    sh "echo Começo"
    sh "git rev-parse --short HEAD > commit-id"
    def tag = sh returnStdout: true, script: 'cat commit-id'
    
    
    
    // configura o nome da aplicação, o endereço do repositório e o nome da imagem com a versão
    appName = 'app'
    def registryHost = sh returnStdout: true, script: 'curl ifconfig.me'
    host = "${registryHost}:30400/"
    url = "${host}${appName}:${tag}"
    image = url.replaceAll("\\s","")
       
    // Configuramos os estágios
     
    stage "Build"
        //echo "${imageName}"
        //def dockerfile = 'Dockerfile'
        def customImage = docker.build("$image")

    stage "Push"

        customImage.push()


    stage "Deploy PROD"

        input "Deploy to PROD?"
        customImage.push('latest')
        sh "kubectl apply -f https://raw.githubusercontent.com/ReiJr/Docker-Flask-uWSGI/master/k8s_app.yaml"
        sh "kubectl set image deployment app app=${image} --record"
        sh "kubectl rollout status deployment/app"
}
*/
