# from django.shortcuts import redirect
#
# class RequireProfileMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         if request.user.is_authenticated:
#             if not request.user.profile_verified and request.path != '/setup-profile/':
#                 return redirect('setup_profile')
#         return self.get_response(request)