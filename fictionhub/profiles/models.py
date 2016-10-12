from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import permalink

from posts.models import Post
from comments.models import Comment
from hubs.models import Hub


from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# from imageresize import imageresize


def resize_image(image, width):
    # Open image
    image_obj = Image.open(image)
    w, h = image_obj.size
    # If it hasn't been resized
    if w != width:
        # Proportional resize
        # Determine what percentage desired width is of original width
        wpercent = (width/float(image_obj.size[0]))
        # Multiply original height by that percentage to figure out proportional height
        hsize = int((float(image_obj.size[1])*float(wpercent)))
        # Resize image
        image_resized = image_obj.resize((width, hsize), Image.ANTIALIAS)

        # BytesIO magic to save it properly
        image_io  = BytesIO()
        image_resized.save(image_io, format='JPEG', quality=90)
        
        temp_name = image.name
        image.delete(save=False)  
        
        image.save(
            temp_name,
            content=ContentFile(image_io.getvalue()),
            save=False
        )

    
class User(AbstractUser):  
    about = models.TextField(max_length=512, blank=True)
    website = models.CharField(max_length=64, blank=True)
    karma = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


    avatar = models.ImageField(upload_to='profiles/avatars', default=None,blank=True, null=True)
    background = models.ImageField(upload_to='profiles/backgrounds', default=None,blank=True, null=True)        
    subscribed_to = models.ManyToManyField('User', related_name="subscribers", blank=True)
    subscribed_to_hubs = models.ManyToManyField('hubs.Hub', related_name="subscribers", blank=True)

    upvoted = models.ManyToManyField('posts.Post', related_name="upvoters", blank=True)
    reposted = models.ManyToManyField('posts.Post', related_name="reposters", blank=True) 
    
    # shadowban = models.BooleanField(default=False)
    # approved = models.BooleanField(default=False)

    new_notifications = models.BooleanField(default=False)    

    # Email notifications
    # email_subscriptions = models.BooleanField(default=True,
    # verbose_name='Send me email notifications when someone I follow publishes a new story')
    # email_comments = models.BooleanField(default=True,
    # verbose_name='Send me email notifications when someone replies to my story or comment')
    # email_messages = models.BooleanField(default=True,
    # verbose_name='Send me email notifications when someone sends me a personal message.')
    # email_subscriber_notifications = models.BooleanField(default=True,
    # verbose_name='Send me email notifications when someone subscribes to my stories.')
    # email_upvotes = models.BooleanField(default=True,
    # verbose_name='Send me email notifications when someone upvotes my story.')
    # email_messages = models.BooleanField(default=True,
    # verbose_name='Send me email notifications when someone sends me a personal message.')
    
    # email_messages = models.BooleanField(default=False)                            


    def save(self, *args, **kwargs):
        if self.avatar:
            resize_image(self.avatar, 160)

        if self.background:
            resize_image(self.background, 480)        
        super(User, self).save(*args, **kwargs)
    
    @permalink
    def get_absolute_url(self):
        return ('user_profile', None, {'username': self.username })        


# Email subscriber
class Subscriber(models.Model):
    email = models.CharField(max_length=64, blank=True)    
    subscribed_to = models.ManyToManyField('User', related_name="email_subscribers", blank=True)

    def __str__(self):
        return self.email
