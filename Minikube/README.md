Minikube Setup on Windows with Docker Driver
This section documents my experience setting up Minikube on Windows 11 using the Docker driver, including troubleshooting and environment cleanup.

🐞 Initial Issue: Missing Configuration & Driver Mismatch
While checking Minikube status, I encountered the following error:
status error: open ...\config.json: The system cannot find the file specified.


Attempting to start Minikube with Docker resulted in:
GUEST_DRIVER_MISMATCH: The existing "minikube" cluster was created using the "hyperv" driver, which is incompatible with requested "docker" driver.



🔧 Resolution Steps
- Deleted old cluster and residual files
minikube delete --all --purge
- Started Minikube with Docker driver
minikube start --driver=docker --memory=2000 --cpus=2
- Verified cluster status
minikube status
- Confirmed Docker integration
minikube docker-env



✅ Outcome
Minikube successfully launched using Docker, avoiding VM overhead and simplifying local Kubernetes development. This setup is ideal for testing:
- Kubernetes manifests
- Helm charts
- CI/CD pipelines
- Containerized microservices

💡 DevOps Reflection
This experience reinforced key DevOps principles:
- Understanding system-level constraints (memory, permissions)
- Navigating driver-specific configurations
- Resetting environments cleanly for reproducible setups



