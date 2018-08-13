from django.urls import path
from django.conf.urls import url
from .views import stub_view
from .views import list_view
from .views import detail_view

urlpatterns = [path('', list_view, name="blog_index"),
               path('posts/<int:post_id>/', detail_view, name="blog_detail"),
               path('posts/<int:post_id>/', stub_view, name="blog_detail")
               ]

# urlpatterns = [path('', list_view, name="blog_index"),
#                path('posts/<int:post_id>/', stub_view, name="blog_detail")
#                ]

# urlpatterns = [url(r'^$', list_view, name="blog_index"),
#                url(r'^posts/(\d+)/$', stub_view, name="blog_detail"),
#                ]