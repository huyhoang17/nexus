# markdownify
from django import template
import markdown
import bleach

 
register = template.Library()
 
@register.filter
def markdownify(text, short = "False"):
    text = text
    customcut = False
    if short == "True":
        try:
            if "<!-- more -->" in text:
                text = text.split("<!-- more -->")[0].strip()
                customcut = True
                text += "<div class='clearfix'></div><a class='readmore'> Read more... </a>" 
        except:
            pass
        text = text[:1024]

    html = markdown.markdown(text)

    if short == "True" and not customcut:
        try:
            # Cut after 2nd paragraph
            htmlbefore = html
            sep = '</p>'
            firstparagraphs = html.split(sep, 2)[:2]
            html = ''.join(firstparagraphs)
            if len(html) < len(htmlbefore) - 10:
                html += "<div class='clearfix'></div><a class='readmore'> Read more... </a>"  
        except:
            pass
        
    

    # if short == "True":    
    #     html += "<div class='clearfix'></div><a href='"+post.get_absolute_url()+"' class='readmore'> read more >>>> </a>"

    # linkify_html = bleach.linkify(html)
    # tags = ['img', 'p', 'em', 'strong', 'a', 'span', 'b', 'i', 'blockquote', 'hr'] # bleach.ALLOWED_TAGS
    # attributes = {
    #     '*': ['class', 'style'],
    #     'a': ['href', 'rel'],
    #     'img': ['src', 'alt', 'style'],
    # }
    # styles = ['float','font-weight', 'width']
    
    # clean_html = bleach.clean(linkify_html, styles=styles, tags=tags, attributes=attributes, strip=True)
    return html #clean_html
