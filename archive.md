---
layout: default
title: Archive
description: Browse all tutorials and articles
permalink: /archive/
---

# Tutorial Archive

Browse our complete collection of tutorials, guides, and insights. Use the categories and tags to find exactly what you're looking for.

<div class="archive-controls">
    <div class="archive-stats">
        <span class="post-count">{{ site.posts | size }} articles published</span>
    </div>
    
    <div class="archive-filters">
        <button class="filter-btn active" data-filter="all">All Posts</button>
        <button class="filter-btn" data-filter="kubernetes">Kubernetes</button>
        <button class="filter-btn" data-filter="gcp">Google Cloud</button>
        <button class="filter-btn" data-filter="aws">AWS</button>
        <button class="filter-btn" data-filter="devops">DevOps</button>
    </div>
</div>

<div class="archive-posts">
    {% for post in site.posts %}
        <article class="archive-post-card" data-tags="{{ post.tags | join: ' ' | downcase }}">
            <div class="post-date">
                <time datetime="{{ post.date | date_to_xmlschema }}">
                    {{ post.date | date: "%b %d, %Y" }}
                </time>
            </div>
            
            <div class="post-content-preview">
                <h3 class="post-title">
                    <a href="{{ post.url }}">{{ post.title }}</a>
                </h3>
                
                {% if post.subtitle %}
                    <p class="post-subtitle">{{ post.subtitle }}</p>
                {% endif %}
                
                <div class="post-excerpt">
                    {{ post.excerpt | strip_html | truncate: 200 }}
                </div>
                
                <div class="post-meta">
                    {% if post.reading_time %}
                        <span class="reading-time">{{ post.reading_time }} min read</span>
                    {% endif %}
                    
                    {% if post.tags.size > 0 %}
                        <div class="post-tags">
                            {% for tag in post.tags limit:3 %}
                                <span class="tag">{{ tag }}</span>
                            {% endfor %}
                        </div>
                    {% endif %}
                </div>
            </div>
        </article>
    {% endfor %}
</div>

{% comment %}
<!-- Archive by Year (Alternative Layout) -->
<div class="archive-by-year" style="display: none;">
    {% for post in site.posts %}
        {% assign currentDate = post.date | date: "%Y" %}
        {% assign postDate = post.date | date: "%Y" %}
        
        {% if currentDate != previousDate %}
            {% unless forloop.first %}</div>{% endunless %}
            <div class="year-group">
                <h2 class="year-heading">{{ currentDate }}</h2>
        {% endif %}
        
        <article class="year-post">
            <time class="post-date" datetime="{{ post.date | date_to_xmlschema }}">
                {{ post.date | date: "%b %d" }}
            </time>
            <h3 class="post-title">
                <a href="{{ post.url }}">{{ post.title }}</a>
            </h3>
            {% if post.subtitle %}
                <p class="post-subtitle">{{ post.subtitle }}</p>
            {% endif %}
        </article>
        
        {% if forloop.last %}</div>{% endif %}
        {% assign previousDate = currentDate %}
    {% endfor %}
</div>
{% endcomment %}

<style>
.archive-controls {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: var(--space-2xl);
    padding: var(--space-lg);
    background: var(--color-background-alt);
    border-radius: var(--radius-lg);
    flex-wrap: wrap;
    gap: var(--space-md);
}

.archive-stats {
    color: var(--color-text-muted);
    font-family: var(--font-secondary);
    font-size: var(--font-size-sm);
}

.archive-filters {
    display: flex;
    gap: var(--space-sm);
    flex-wrap: wrap;
}

.filter-btn {
    padding: var(--space-sm) var(--space-md);
    background: transparent;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-full);
    color: var(--color-text-muted);
    font-family: var(--font-secondary);
    font-size: var(--font-size-sm);
    cursor: pointer;
    transition: all 0.2s ease;
}

.filter-btn:hover,
.filter-btn.active {
    background: var(--color-primary);
    color: white;
    border-color: var(--color-primary);
}

.archive-posts {
    display: flex;
    flex-direction: column;
    gap: var(--space-xl);
}

.archive-post-card {
    display: flex;
    gap: var(--space-lg);
    padding: var(--space-xl);
    background: var(--color-background);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-lg);
    transition: all 0.2s ease;
    opacity: 1;
    transform: translateY(0);
}

.archive-post-card:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
}

.archive-post-card.hidden {
    opacity: 0;
    transform: translateY(10px);
    pointer-events: none;
    margin: 0;
    padding: 0;
    height: 0;
    overflow: hidden;
}

.post-date {
    flex-shrink: 0;
    width: 100px;
    color: var(--color-text-muted);
    font-family: var(--font-secondary);
    font-size: var(--font-size-sm);
    font-weight: 500;
}

.post-content-preview {
    flex: 1;
}

.archive-post-card .post-title {
    font-size: var(--font-size-xl);
    margin: 0 0 var(--space-sm) 0;
    line-height: var(--line-height-tight);
}

.archive-post-card .post-title a {
    color: var(--color-text);
    text-decoration: none;
    transition: color 0.2s ease;
}

.archive-post-card .post-title a:hover {
    color: var(--color-primary);
}

.archive-post-card .post-subtitle {
    color: var(--color-text-muted);
    font-size: var(--font-size-base);
    margin: 0 0 var(--space-md) 0;
    line-height: var(--line-height-normal);
}

.archive-post-card .post-excerpt {
    color: var(--color-text-muted);
    line-height: var(--line-height-relaxed);
    margin-bottom: var(--space-md);
}

.archive-post-card .post-meta {
    display: flex;
    align-items: center;
    gap: var(--space-md);
    flex-wrap: wrap;
}

.archive-post-card .reading-time {
    color: var(--color-text-muted);
    font-family: var(--font-secondary);
    font-size: var(--font-size-sm);
}

.archive-post-card .post-tags {
    display: flex;
    gap: var(--space-sm);
    flex-wrap: wrap;
}

.archive-post-card .tag {
    background: var(--color-background-alt);
    color: var(--color-text-muted);
    padding: var(--space-xs) var(--space-sm);
    border-radius: var(--radius-full);
    font-size: var(--font-size-xs);
    font-weight: 500;
    font-family: var(--font-secondary);
}

/* Year-based archive layout (alternative) */
.year-group {
    margin-bottom: var(--space-2xl);
}

.year-heading {
    font-size: var(--font-size-2xl);
    color: var(--color-text);
    margin-bottom: var(--space-lg);
    padding-bottom: var(--space-md);
    border-bottom: 2px solid var(--color-border);
}

.year-post {
    display: flex;
    gap: var(--space-lg);
    padding: var(--space-md) 0;
    border-bottom: 1px solid var(--color-border);
}

.year-post:last-child {
    border-bottom: none;
}

.year-post .post-date {
    width: 60px;
    flex-shrink: 0;
}

.year-post .post-title {
    font-size: var(--font-size-lg);
    margin: 0 0 var(--space-xs) 0;
}

.year-post .post-subtitle {
    color: var(--color-text-muted);
    font-size: var(--font-size-sm);
    margin: 0;
}

/* Responsive design */
@media (max-width: 768px) {
    .archive-controls {
        flex-direction: column;
        align-items: flex-start;
    }
    
    .archive-post-card {
        flex-direction: column;
        gap: var(--space-md);
    }
    
    .post-date {
        width: auto;
    }
    
    .year-post {
        flex-direction: column;
        gap: var(--space-sm);
    }
    
    .year-post .post-date {
        width: auto;
    }
}

@media (max-width: 480px) {
    .archive-filters {
        justify-content: center;
        width: 100%;
    }
    
    .filter-btn {
        flex: 1;
        text-align: center;
        min-width: 80px;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const posts = document.querySelectorAll('.archive-post-card');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            const filter = this.dataset.filter;
            
            posts.forEach(post => {
                const tags = post.dataset.tags;
                
                if (filter === 'all' || tags.includes(filter)) {
                    post.classList.remove('hidden');
                } else {
                    post.classList.add('hidden');
                }
            });
        });
    });
});
</script>
