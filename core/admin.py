from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from chat.models import Chat
from friends.models import Friends
from like.models import Like
from message.models import Message
from post.models import Post
from query_friend.models import QueryFriend
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    pass

admin.site.register(Post)
admin.site.register(Friends)
admin.site.register(QueryFriend)
admin.site.register(Message)
admin.site.register(Like)
admin.site.register(Chat)
