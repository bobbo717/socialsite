from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from facebook.models import UserFollows, FacebookFriends

def home(request):
    flist = UserFollows.objects.filter(user=request.user)
    ulist = User.objects.exclude(id=flist.values('id'))
    return render_to_response('home.html',{'follow_list':flist,
                                           'user_list':ulist,
                                           },
                              context_instance=RequestContext(request))
def fb_friends(request):
    #    facebook_friends = request.user.get_profile().get_facebook_friends()
    facebook_friends = FacebookFriends.objects.filter(user=request.user)[:20]
    flist = UserFollows.objects.filter(user=request.user)
    ulist = User.objects.exclude(id=flist.values('id'))
    return render_to_response('friends.html',
                              { 'facebook_friends': facebook_friends,
                                'follow_list': flist,
                                'user_list':ulist,
                                },
                              context_instance=RequestContext(request))

def follow_list(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    flist = UserFollows.objects.filter(user=u.id)
    return render_to_response('account/follows.html', {'follow_list': flist})

def user_follow(request, user_id,following_id):
    u = get_object_or_404(User, pk=user_id)
    f = get_object_or_404(User, pk=following_id)
    print UserFollows.objects.create(user=u,following=f)
    return render_to_response('account/account.html', {'u': u})

def available_users(request):
    ulist = User.objects.exclude(id=request.user.id)
    return render_to_response('account/accounts.html', {'user_list': ulist })

def user(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    uf_list = UserFollows.objects.filter(user=user_id)

    flist = UserFollows.objects.filter(user=request.user)
    ulist = User.objects.exclude(id=flist.values('id'))
    return render_to_response('account/account.html',
                              {'u': u,
                               'follow_list': flist,
                               'user_list': ulist,
                                  },
                              context_instance=RequestContext(request))
