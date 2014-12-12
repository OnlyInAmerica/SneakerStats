from django.contrib import admin
from models import Session, Peer, Identity
# Register your models here.

admin.site.register(Peer)
admin.site.register(Session)
admin.site.register(Identity)