# docker

## centos

 - 安装所需的软件包yum-utils提供yum-config-manager实用程序，devicemapper-storage-driver驱动程序需要device-mapper-persistent-data和lvm2。
    $ sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2

 - 使用以下命令来设置稳定的存储库。即使您想从边缘或测试存储库安装构建，也总是需要稳定的存储库。
    $ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

 - 可选：启用边缘和测试存储库。这些存储库包含在上面的docker.repo文件中，但默认情况下是禁用的。 您可以将它们与稳定的存储库一起启用。
    $ sudo yum-config-manager --enable docker-ce-edge

    $ sudo yum-config-manager --enable docker-ce-test
    
    **Note:** Starting with Docker 17.06, stable releases are also pushed to the edge and test repositories.
    
### INSTALL DOCKER CE

 - 安装最新版本的Docker CE，或者转到下一步安装特定版本。

    $ sudo yum install docker-ce
    
    **Warning:** 如果启用了多个Docker存储库，则在yum install或yum update命令中安装或更新，而不指定版本将始终安装尽可能高的版本，这可能不适合您的稳定性需求。
    
    如果这是您第一次从最近添加的存储库安装软件包，系统将提示您接受GPG密钥，并显示密钥的指纹。 验证指纹是否正确，如果是，请接受密钥。 指纹应该匹配060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35。

    Docker已安装，但未启动。 docker组已创建，但没有用户添加到组中。

 - 在生产系统上，您应该安装特定版本的DockerCE，而不是始终使用最新版本。 列出可用的版本。 此示例使用sort -r命令按版本号排序结果，从最高到最低，并被截断。

    $ yum list docker-ce --showduplicates | sort -r

        docker-ce.x86_64           
        17.09.ce-1.el7.centos                 
        docker-ce-stable

    列表的内容取决于启用了哪些存储库，并且将特定于您的CentOS版本（在本例中，由版本中的.el7后缀指示）。 选择一个特定的版本进行安装。 第二列是版本字符串。 您可以使用整个版本字符串，但是您至少需要包含第一个连字符。 第三列是存储库名称，它指明了软件包来自哪个存储库，并且通过扩展其稳定性级别。 要安装特定的版本，请将版本字符串附加到包名称，并用连字符（ - ）分隔。
    **注意**：版本字符串是软件包名称加上第一个连字符的版本。 在上面的示例中，完全限定的软件包名称是docker-ce-17.06.1.ce。
    $ sudo yum install 'FULLY-QUALIFIED-PACKAGE-NAME'

 - Start Docker.

    $ sudo systemctl start docker

 - 通过运行hello-world映像来验证docker是否正确安装。
 
    $ sudo docker run hello-world
    
