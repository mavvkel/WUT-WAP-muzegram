from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Profile
from .forms import PostForm, MyUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class FeedView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'Platform/feed.html'
    context_object_name = 'followed_posts'
    form = PostForm()
    extra_context = {'form': form}
    login_url = '/login/'

    def get_queryset(self):
        return Post.objects.filter(
            owner__profile__in=self.request.user.profile.follows.all()
        ).order_by('-publication_date')

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('Platform:feed')
        else:
            return render(request, self.template_name, {'form': form})


@login_required(login_url='/login/')
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'Platform/profile-list.html', {'profiles': profiles})


@login_required(login_url='/login/')
def profile(request, pk):
    # guard checking if the logged user does not have a Profile
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    current_user_profile = request.user.profile
    current_profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        data = request.POST
        action = data.get('follow')

        if action == 'follow':
            current_user_profile.follows.add(current_profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(current_profile)

        current_user_profile.save()
        return redirect('Platform:profile', current_profile.id)
    return render(request, 'Platform/profile.html', {'profile': current_profile,
                                                     'accessing_profile': request.user.profile,
                                                     })


def register(request):
    form = MyUserCreationForm(request.POST or None)
    form.label_suffix = ''
    if request.method == 'GET':
        return render(
            request,
            'register.html',
            {'form': MyUserCreationForm}
        )
    elif request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Platform:feed')
        else:
            return render(request, 'register.html', {'form': form})
