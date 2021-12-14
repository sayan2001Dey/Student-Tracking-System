from django.shortcuts import redirect

def is_cdc(view_func):
	def wrapper(request, *args, **kwargs):
		if not hasattr(request.user, 'teacher') and not hasattr(request.user, 'student'):
			return view_func(request, *args, **kwargs)
		else:
			return redirect('authentication:index')
	return wrapper