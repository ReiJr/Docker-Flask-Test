node {

    checkout scm

    // Pega o commit id para ser usado de tag (versionamento) na imagem
    sh "echo Começo"
    sh "git rev-parse --short HEAD > commit-id"
    tag = sh "cat commit-id"
    
    
    // configura o nome da aplicação, o endereço do repositório e o nome da imagem com a versão
    appName = "app"
    registryHost = sh "curl ifconfig.me"
    imageName = "${registryHost}${appName}:${tag}"
    
    // Configuramos os estágios
    
    stage "Build"
        echo ${imageName}
        def customImage = docker.build("${imageName}")

    stage "Push"

        customImage.push()


    stage "Deploy PROD"

        input "Deploy to PROD?"
        customImage.push('latest')
        sh "kubectl apply -f https://raw.githubusercontent.com/cirolini/Docker-Flask-uWSGI/master/k8s_app.yaml"
        //sh "kubectl set image deployment app app=${imageName} --record"
        //sh "kubectl rollout status deployment/app"
}
