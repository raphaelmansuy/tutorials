---
layout: default
title: Welcome to Cloud & DevOps Training Hub
description: A comprehensive collection of hands-on tutorials covering cloud computing, DevOps, and modern development practices
keywords: [tutorials, cloud, devops, gcp, aws, kubernetes, docker, ci-cd, programming]
---

# Welcome to Your Learning Journey

Discover our comprehensive collection of hands-on tutorials designed to take you from beginner to expert in cloud computing and DevOps practices.

## 🌟 Featured Tutorials

<div class="featured-posts">
    {% assign featured_posts = site.posts | where: "featured", true | limit: 3 %}
    {% for post in featured_posts %}
        <article class="post-card featured">
            <div class="post-meta">
                <time datetime="{{ post.date | date_to_xmlschema }}">
                    {{ post.date | date: "%B %d, %Y" }}
                </time>
                {% if post.reading_time %}
                    <span class="reading-time">{{ post.reading_time }} min read</span>
                {% endif %}
            </div>
            
            <h2 class="post-title">
                <a href="{{ post.url }}">{{ post.title }}</a>
            </h2>
            
            <div class="post-excerpt">
                {{ post.excerpt | strip_html | truncate: 200 }}
            </div>
            
            <div class="post-footer">
                {% if post.tags.size > 0 %}
                    <div class="post-tags">
                        {% for tag in post.tags limit:3 %}
                            <span class="tag">{{ tag }}</span>
                        {% endfor %}
                    </div>
                {% endif %}
                <a href="{{ post.url }}" class="read-more">Continue reading →</a>
            </div>
        </article>
    {% endfor %}
</div>

## 📚 Browse by Category

### ☁️ Cloud Computing
- **Google Cloud Platform (GCP)** - Master Google's cloud services
- **Amazon Web Services (AWS)** - Learn AWS fundamentals and advanced topics
- **Cloud Architecture** - Design scalable and reliable cloud solutions

### 🚢 Container Orchestration
- **Kubernetes** - Container orchestration at scale
- **Docker** - Containerization fundamentals
- **Container Best Practices** - Security, optimization, and deployment

### 🔄 DevOps & CI/CD
- **GitLab CI/CD** - Automated testing and deployment
- **Infrastructure as Code** - Terraform, CloudFormation, and more
- **Monitoring & Observability** - Keep your systems healthy

### 🤖 AI & Machine Learning
- **Vertex AI** - Google's ML platform
- **AI Agent Development** - Build intelligent applications
- **MLOps** - Machine learning in production

## 📖 Latest Posts

<div class="latest-posts">
    {% for post in site.posts limit:5 %}
        <article class="post-card">
            <div class="post-meta">
                <time datetime="{{ post.date | date_to_xmlschema }}">
                    {{ post.date | date: "%B %d, %Y" }}
                </time>
                {% if post.reading_time %}
                    <span class="reading-time">{{ post.reading_time }} min read</span>
                {% endif %}
            </div>
            
            <h3 class="post-title">
                <a href="{{ post.url }}">{{ post.title }}</a>
            </h3>
            
            <div class="post-excerpt">
                {{ post.excerpt | strip_html | truncate: 150 }}
            </div>
            
            <div class="post-footer">
                {% if post.tags.size > 0 %}
                    <div class="post-tags">
                        {% for tag in post.tags limit:3 %}
                            <span class="tag">{{ tag }}</span>
                        {% endfor %}
                    </div>
                {% endif %}
                <a href="{{ post.url }}" class="read-more">Read more →</a>
            </div>
        </article>
    {% endfor %}
</div>

## 💌 Stay Updated

Never miss a tutorial! Subscribe to our newsletter for weekly updates on new content, industry insights, and exclusive tips.

<div class="newsletter-signup">
    <div class="newsletter-content">
        <h3>Subscribe to {{ site.title }}</h3>
        <p>Get the latest tutorials and insights delivered to your inbox weekly</p>
        
        <!-- Replace with your actual newsletter signup form -->
        <form class="subscription-form" action="#" method="post">
            <div class="form-group">
                <input type="email" name="email" placeholder="Enter your email address" required>
                <button type="submit">Subscribe</button>
            </div>
        </form>
        
        <div class="subscription-stats">
            <span class="subscriber-count">Join our growing community of learners</span>
        </div>
    </div>
</div>

## 🎯 Learning Paths

### For Beginners
1. [Kubernetes for Absolute Beginners](./01_kubernetes_beginner.md) - Start your container journey
2. [How to Install Google Cloud CLI](./03_how_to_install_google_cloud.md) - Set up your development environment
3. [GCP Crash Course](./04_gcp_crash_course.md) - Learn cloud fundamentals

### For Intermediate Learners
1. [Deploying Next.js to GCP](./06_deploy_nextjs_to_gcp.md) - Modern web deployment
2. [CI/CD with GitLab and ECR](./15_ci_cd_gitlab_ecr.md) - Automated workflows
3. [Vertex AI Guide](./05_vertex_ai.md) - Machine learning in the cloud

### For Advanced Practitioners
1. [Migration from HAProxy to AWS](./13_migration_from_haproxy_to_aws_managed_services.md) - Infrastructure modernization
2. [SaaS Development with AWS ECS Fargate](./14_developing_a_saas_using_aws_and_ecs_fargate.md) - Scalable application architecture
3. [Vertex AI & Agent Engine Observability](./31_observability_llm_adk_vertex.md) - Production-grade AI monitoring and alerting
4. [Developing AI Agents with Google ADK](./07_develop_ai_agent_with_google_adk.md) - Advanced AI development

---

<div class="home-footer">
    <p><strong>Ready to start learning?</strong> Pick a tutorial that matches your skill level and dive in. Each tutorial includes hands-on examples, code samples, and step-by-step instructions.</p>
    
    <div class="quick-links">
        <a href="/archive" class="cta-button">Browse All Tutorials</a>
        <a href="/about" class="cta-button secondary">About This Site</a>
    </div>
</div>

<style>
.featured-posts .post-card.featured {
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    border: 2px solid var(--color-primary);
    border-radius: var(--radius-lg);
    padding: var(--space-xl);
    margin-bottom: var(--space-xl);
}

.home-footer {
    text-align: center;
    padding: var(--space-2xl) 0;
    border-top: 1px solid var(--color-border);
    margin-top: var(--space-2xl);
}

.quick-links {
    display: flex;
    justify-content: center;
    gap: var(--space-md);
    margin-top: var(--space-lg);
    flex-wrap: wrap;
}

.cta-button {
    display: inline-block;
    padding: var(--space-md) var(--space-xl);
    background: var(--color-primary);
    color: white;
    text-decoration: none;
    border-radius: var(--radius-md);
    font-weight: 600;
    font-family: var(--font-secondary);
    transition: all 0.2s ease;
}

.cta-button:hover {
    background: #e55a0f;
    transform: translateY(-1px);
}

.cta-button.secondary {
    background: transparent;
    color: var(--color-primary);
    border: 2px solid var(--color-primary);
}

.cta-button.secondary:hover {
    background: var(--color-primary);
    color: white;
}

@media (max-width: 768px) {
    .quick-links {
        flex-direction: column;
        align-items: center;
    }
    
    .cta-button {
        width: 200px;
        text-align: center;
    }
}
</style>
