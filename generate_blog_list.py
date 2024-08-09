import os
import yaml
from datetime import datetime

def get_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().split('---', 2)
        if len(content) > 1:
            return yaml.safe_load(content[1])
    return None

def generate_blog_list():
    blog_dir = 'content/posts'
    posts = []

    for filename in os.listdir(blog_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(blog_dir, filename)
            metadata = get_metadata(file_path)
            if metadata:
                posts.append({
                    'title': metadata.get('title', 'Untitled'),
                    'date': metadata.get('date', datetime.now()).strftime('%Y-%m-%d'),
                    'tags': metadata.get('tags', []),
                    'url': f'/posts/{os.path.splitext(filename)[0]}/'
                })

    posts.sort(key=lambda x: x['date'], reverse=True)

    with open('content/blog-list.md', 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write('title: "Blog Posts"\n')
        f.write('---\n\n')
        for post in posts:
            f.write(f"- [{post['title']}]({post['url']}) - {post['date']}\n")
            if post['tags']:
                f.write(f"  Tags: {', '.join(post['tags'])}\n")
            f.write('\n')

if __name__ == '__main__':
    generate_blog_list()
