from django.shortcuts import get_object_or_404, redirect, render
from activity.models import Activity
from cdc.decorator import is_cdc
from django.contrib.auth.decorators import login_required




@login_required(login_url='authentication:login')
@is_cdc
def delete_activity(request, id_activity):
    act = get_object_or_404(Activity, id=id_activity)
    act.file.delete()
    act.delete()
    return redirect('cdc:dashboard')