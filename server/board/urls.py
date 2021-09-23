from django.urls import path
from . import views

urlpatterns = [
    path('store', views.StoreList.as_view(), name='store_list'),
    path('store/<int:pk>', views.StoreDetail.as_view(), name='store_detail'),
    path('store-img', views.StoreImg.as_view(), name='store_img'),

    path('review', views.ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
    path('review-img', views.ReviewImg.as_view(), name='review_img'),

    path('tag', views.TagList.as_view(), name='tag_list'),
    path('tag/<int:pk>', views.TagDetail.as_view(), name='tag_detail'),

    path('menu', views.MenuList.as_view(), name='menu_list'),
    path('menu/<int:pk>', views.MenuDetail.as_view(), name='menu_detail'),
    path('menu-img', views.MenuImg.as_view(), name='menu_img'),

    # 사업자 등록번호 검증 API
    path('biz-auth/<int:pk>', views.BizAuth.as_view(), name='biz_auth'),

]
