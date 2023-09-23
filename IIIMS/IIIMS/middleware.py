# middleware.py
from django.shortcuts import redirect
from django.urls import reverse

# class AdminAccessMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.path.startswith(reverse('admin:index')):
#             # Add your custom access conditions here
#             if not request.user.is_authenticated or not request.user.is_staff:
#                 return redirect('home')  # Redirect to your desired URL
#         return self.get_response(request)
class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Exclude admin login page from access condition
        if request.path == reverse('admin:login'):
        # if request.path.startswith(reverse('admin:login')):
            # user = request.user
            # if not request.user.is_authenticated or not request.user.is_staff:
            #     return redirect('index')  # Redirect to your desired URL
            return self.get_response(request)

        # Check access conditions for other admin pages
        # if request.path.startswith(reverse('admin:index')):
        #     # Add your custom access conditions here
        #     if not request.user.is_authenticated or not request.user.is_staff:
        #         return redirect('index')  # Redirect to your desired URL

        return self.get_response(request)
