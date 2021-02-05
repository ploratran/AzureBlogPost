# Write-up Template

## Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

## Why App Service over Virtual Machine? 
I choose to deploy using App Service because it is a PaaS (Platform as a Service). It means that it is specialized for HTTP-based service for hosting web applications (for this project). App Service also supports Python language and Github, which are the dependencies used for this project. As App Service is a PaaS, it allows me as a developer to focus on the app development and not to worry about the infrastructure such as the deployment pipeline, host server, the underlying operating system, etc. Lastly, App Service is cost efficient than Virtual Machine as I only have to pay for I use. 

## Why Not Virtual Machine? 
I don't choose to deploy with Virtual Machine (VM) because it is a Infrastructure as a Service (IaaS). This project is a web applicaiton so I don't have to create and use virtual machine in the cloud. I don't need to access and control the VM, as well as other infrastructures such as memory, CPU, RAM, storage, etc. Furthermore, VMs are more expensive and more time consuming to develop for this project. 

