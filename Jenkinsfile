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
    //registryHost = sh "curl ifconfig.me"
    imageName1 = "${host}${appName}:${tag}"
    imageName = "3.89.20.116:30400/app:8e392ec"
    echo "$imageName"
    echo "$imageName1"

   
    // Configuramos os estágios
     
    stage "Build"
        //echo "${imageName}"
        //def dockerfile = 'Dockerfile'
        def customImage = docker.build("3.89.20.116:30400/app:8e392ec")

    stage "Push"

        customImage.push()


    stage "Deploy PROD"

        input "Deploy to PROD?"
        customImage.push('latest')
        sh "kubectl apply -f https://raw.githubusercontent.com/ReiJr/Docker-Flask-uWSGI/master/k8s_app.yaml"
        //sh "kubectl set image deployment app app=${imageName} --record"
        //sh "kubectl rollout status deployment/app"
}
