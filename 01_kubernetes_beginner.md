# Kubernetes for Absolute Beginners: Deploying Your First App on Amazon EKS with OpenLens

---

## Quick Start Checklist

- A computer with **macOS, Windows, or Linux** (8GB+ RAM, 10GB+ free disk space)
- Internet connection
- Credit card for AWS signup (Free Tier covers most, but AWS requires a card)
- No prior Kubernetes or AWS experience needed!

---

## Glossary (Key Terms)

- **Cloud:** Someone else's computer you rent on demand (like AWS).
- **Cluster:** A group of computers (nodes) managed as one.
- **Node:** A single computer (virtual or physical) in your cluster.
- **Pod:** The smallest deployable unit in Kubernetes (usually one app container).
- **Deployment:** A way to manage and update Pods.
- **Service:** A stable way to access Pods.
- **kubeconfig:** A file that stores cluster connection info for `kubectl` and OpenLens.

---

## Table of Contents

1. [Introduction: What Are Containers & Kubernetes?](#1-introduction-what-are-containers--kubernetes)
2. [Core Kubernetes Concepts (Simple Analogies)](#2-core-kubernetes-concepts-simple-analogies)
3. [Getting Started with AWS](#3-getting-started-with-aws)
4. [Setting Up Your Local Machine (System Requirements & Tools)](#4-setting-up-your-local-machine-system-requirements--tools)
5. [Provisioning an EKS Cluster with eksctl](#5-provisioning-an-eks-cluster-with-eksctl)
6. [Deploying Your First Application (Nginx) to EKS](#6-deploying-your-first-application-nginx-to-eks)
7. [Exposing Your Application to the Internet](#7-exposing-your-application-to-the-internet)
8. [Visualizing & Managing with OpenLens](#8-visualizing--managing-with-openlens)
9. [Basic Troubleshooting & Next Steps](#9-basic-troubleshooting--next-steps)
10. [Cleaning Up AWS Resources (Avoid Charges)](#10-cleaning-up-aws-resources-avoid-charges)

---

## 1. Introduction: What Are Containers & Kubernetes?

### What Are Containers?

- **Analogy:** Think of containers like shipping containers for software. They package everything an app needs (code, libraries, settings) so it runs the same anywhere.
- **Why use them?** Consistency, portability, and efficiency.

### Why Kubernetes?

- **Problem:** Managing lots of containers is hard (imagine tracking thousands of shipping containers!).
- **Kubernetes:** An orchestrator that automates deploying, scaling, and managing containers.

### High-Level Kubernetes Architecture

- **Control Plane (Master):** The brains—decides what runs where.
- **Worker Nodes:** The muscle—actually run your apps (containers).

---

## 2. Core Kubernetes Concepts (Simple Analogies)

- **Pod:** The smallest deployable unit. Like a single shipping container.
- **Deployment:** A blueprint for running and updating Pods. Like a shipping schedule.
- **Service:** A stable way to access Pods. Like a port where containers are delivered.
- **Namespace:** Logical separation. Like different shipping companies using the same port.
- **Node:** A machine (VM or physical) that runs Pods. Like a dock at the port.
- **Cluster:** All the nodes and control plane together. Like the whole shipping yard.

---

## 3. Getting Started with AWS

### Step 1: Create an AWS Account

1. Go to [aws.amazon.com](https://aws.amazon.com/) and click **Create an AWS Account**.
2. Follow the prompts (email, password, payment info—AWS Free Tier covers most beginner needs, but a credit card is required).
3. **Important:** You may need to verify your identity and payment method.

### Step 2: AWS Free Tier

- Many EKS resources are covered by the Free Tier, but **ALWAYS clean up at the end** to avoid charges.
- [Set up AWS billing alerts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-alerts.html) for peace of mind.

### Step 3: Set Up AWS CLI & IAM User

1. **Create an IAM User:**
   - Go to the AWS Console → IAM → Users → Add user.
   - Name: `eks-user`, Access type: **Programmatic access**.
   - Attach policy: `AdministratorAccess` (for learning; use least privilege in production).
   - Save the **Access Key ID** and **Secret Access Key**.
2. **Install AWS CLI:**
   - **macOS:** `brew install awscli`
   - **Windows:** Download from [AWS CLI Installer](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
   - **Linux:**

```sh
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

   - **Verify install:**

```sh
aws --version
```

3. **Configure AWS CLI:**

```sh
aws configure
```

   Enter your Access Key, Secret Key, region (e.g., `us-east-1`), and output format (`json`).

### Step 4: Install eksctl

- **macOS:** `brew tap weaveworks/tap && brew install weaveworks/tap/eksctl`
- **Windows:** `choco install eksctl`
- **Linux:**

```sh
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
```

- **Verify install:**

```sh
eksctl version
```

---

## 4. Setting Up Your Local Machine (System Requirements & Tools)

- **RAM:** At least 8GB recommended (for OpenLens and tools).
- **Disk Space:** 10GB+ free.
- **OS:** Windows, macOS, or Linux.
- **Tools:** AWS CLI, eksctl, kubectl, OpenLens.

### Install kubectl

- **macOS:** `brew install kubectl`
- **Windows:** `choco install kubernetes-cli`
- **Linux:**

```sh
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

- **Verify install:**

```sh
kubectl version --client
```

---

## 5. Provisioning an EKS Cluster with eksctl

### Step 1: Create Your EKS Cluster

```sh
eksctl create cluster \
  --name beginner-cluster \
  --region us-east-1 \
  --nodes 2 \
  --node-type t3.small \
  --with-oidc \
  # Optional: SSH access to nodes
  # --ssh-access \
  # --ssh-public-key <your-ssh-key>
```

- **--name:** Name of your cluster.
- **--region:** AWS region (e.g., `us-east-1`). Not all regions support EKS—see [EKS region availability](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).
- **--nodes:** Number of worker nodes.
- **--node-type:** Instance type (t3.small is Free Tier eligible).
- **--with-oidc:** Enables IAM roles for service accounts.
- **--ssh-access/--ssh-public-key:** Optional, for SSH access to nodes. [How to generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

> **Tip:** Omit `--ssh-access` and `--ssh-public-key` if you don't need SSH access.

### Step 2: Wait for Cluster Creation

- This can take 10–15 minutes. eksctl will update your kubeconfig automatically.

### Step 3: Verify Cluster Connection

```sh
kubectl get nodes
```

You should see your EKS nodes listed.

---

## 6. Deploying Your First Application (Nginx) to EKS

### Step 1: Create a Deployment YAML File

Create a file named `nginx-deployment.yaml` (use a text editor like VS Code, nano, or vim):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

**Explanation:**

- **replicas:** Number of Nginx Pods.
- **image:** Docker image to use.
- **containerPort:** Port exposed by the container.

### Step 2: Apply the Deployment

```sh
kubectl apply -f nginx-deployment.yaml
```

### Step 3: Check Pod Status

```sh
kubectl get pods
```

Wait until STATUS is `Running`. If not, check logs:

```sh
kubectl logs <pod-name>
```

---

## 7. Exposing Your Application to the Internet

### Step 1: Create a Service YAML File

Create a file named `nginx-service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

**Explanation:**

- **type: LoadBalancer:** Provisions an AWS load balancer.
- **selector:** Matches Pods with `app: nginx`.
- **ports:** Exposes port 80.

### Step 2: Apply the Service

```sh
kubectl apply -f nginx-service.yaml
```

### Step 3: Get the Load Balancer URL

```sh
kubectl get service nginx-service
```

Look for the `EXTERNAL-IP` column. It may take a few minutes to appear. If it stays `<pending>`, check your AWS Console for issues (e.g., VPC/subnet setup).
Visit the URL in your browser to see the Nginx welcome page.

---

## 8. Visualizing & Managing with OpenLens

### Why OpenLens?

- **GUI for Kubernetes:** Makes it easy to see and manage your cluster visually.

### Step 1: Install OpenLens

- **macOS:** Download from [OpenLens Releases](https://github.com/MuhammedKalkan/OpenLens/releases)
- **Windows:** Same as above.
- **Linux:** AppImage or .deb/.rpm from the same page.

### Step 2: Open OpenLens & Add Your Cluster

1. Open OpenLens (it may prompt for permissions or updates on first launch).
2. Click **Add Cluster**.
3. Select your kubeconfig file (usually at `~/.kube/config`). This file stores your cluster connection info.
4. Your EKS cluster should appear in the list.

### Step 3: Explore the Interface

- **Dashboard:** Overview of cluster health.
- **Workloads:** View Deployments, Pods, ReplicaSets.
- **Networking:** View Services, Ingresses.
- **Logs:** Click a Pod to see logs.
- **Troubleshooting:**
  - Pending Pods: Check node capacity.
  - Restart Deployments: Right-click → Restart.

> ![OpenLens Dashboard Example](https://raw.githubusercontent.com/MuhammedKalkan/OpenLens/main/docs/images/dashboard.png)

---

## 9. Basic Troubleshooting & Next Steps

### Common Issues

- **ImagePullBackOff:**
  - Check image name/tag.
  - Ensure internet access from nodes.
  - View pod logs: `kubectl logs <pod-name>`
- **Pending Pods:**
  - Not enough resources or nodes.
  - Check node status in OpenLens or with `kubectl get nodes`.
- **Service Not Reachable:**
  - Wait for LoadBalancer EXTERNAL-IP.
  - Check security groups in AWS.
  - Check AWS Console for orphaned resources (EBS volumes, Elastic IPs).

### Where to Go Next

- Try deploying your own app.
- Learn about scaling, rolling updates.
- Explore Helm (Kubernetes package manager).
- Try interactive labs: [Katacoda Kubernetes Scenarios](https://www.katacoda.com/courses/kubernetes), [Play with Kubernetes](https://labs.play-with-k8s.com/)
- Join the [Kubernetes Slack](https://slack.k8s.io/) or [AWS Discussion Forums](https://repost.aws/tags/TAkF1h3Qn2S1yQkQw2XwQw/kubernetes)

---

## 10. Cleaning Up AWS Resources (Avoid Charges)

> **IMPORTANT:** Always delete your EKS cluster and resources when done to avoid charges!

### Step 1: Delete the EKS Cluster

```sh
eksctl delete cluster --name beginner-cluster --region us-east-1
```

This deletes the cluster and all associated AWS resources.

### Step 2: Verify Deletion

- Check the AWS Console (EKS, EC2, CloudFormation, EBS volumes, Elastic IPs) to ensure all resources are gone.
- Review your [AWS billing dashboard](https://console.aws.amazon.com/billing/home) to confirm no ongoing charges.

---

## Congratulations

You’ve deployed your first Kubernetes app on AWS EKS and visualized it with OpenLens. Keep experimenting and learning!

[Back to Table of Contents](#table-of-contents)

---

**Need more help?**

- [Kubernetes Official Docs](https://kubernetes.io/docs/)
- [AWS EKS Docs](https://docs.aws.amazon.com/eks/)
- [OpenLens GitHub](https://github.com/MuhammedKalkan/OpenLens)
- [Kubernetes YouTube Channel](https://www.youtube.com/c/KubernetesCommunity)

---

> **Remember:** Always clean up your resources to avoid unexpected AWS charges!

[Back to Table of Contents](#table-of-contents)
