from django.shortcuts import render


# get listing from Favourite model
def get_listing(request):
    user = User.objects.all(username=request.user.username)
    user_favourite_list = Favourite.objects.filter(user=user)

# add listing to Favourite model



# remove listing from Favourite model