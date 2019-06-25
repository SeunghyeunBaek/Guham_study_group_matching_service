from django import template

register = template.Library()


@register.filter
def hash_tag_link(post):
    hash_tags = post.hash_tag.all()
    for hash_tag in hash_tags:
        hash_tag.content = f'<a href="match/1/matched_users/{hash_tag.id}/hash_tagged_posts">{hash_tag.content}</a>'
    return hash_tags
