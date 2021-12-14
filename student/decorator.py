from django.shortcuts import redirect

def is_student(view_func):
	def wrapper(request, *args, **kwargs):
		if hasattr(request.user, 'student'):
			return view_func(request, *args, **kwargs)
		else:
			return redirect('authentication:index')
	return wrapper