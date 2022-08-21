import imp
from .models import Profile,Follow

def followuser(request):
    profile = Follow.objects.filter(followed_by=request.user.profile)
    profilecount = profile.count()
    return profile,profilecount