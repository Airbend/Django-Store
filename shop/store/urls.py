from django.urls import path
from .views.home import HomeView
from .views.user_account import register, login, logout, dashboard, activate, forgotPassword, resetPassword, resetpassword_validate, my_orders, edit_profile, change_password, order_detail
from .views.cart import cart, add_cart, remove_cart, remove_cart_item, checkout, _cart_id
from .views.orders import place_order, payments, order_complete
from .views.store import StoreView, ProductDetailView, SearchView, SubmitReviewView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cart/', cart, name='cart'),
    path('store/', StoreView.as_view(), name='store'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),

    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('forgotPassword/', forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', resetPassword, name='resetPassword'),

    path('my_orders/', my_orders, name='my_orders'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),

    path('add_cart/<int:product_id>/', add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', remove_cart_item, name='remove_cart_item'),

    path('checkout/', checkout, name='checkout'),

    path('place_order/', place_order, name='place_order'),
    path('payments/', payments, name='payments'),
    path('order_complete/', order_complete, name='order_complete'),

    path('category/<slug:category_slug>/', StoreView.as_view(), name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('submit_review/<int:product_id>/', SubmitReviewView.as_view(), name='submit_review')


]