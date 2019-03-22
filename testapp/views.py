from django.shortcuts import render
import requests

# Create your views here.
def get_geographic_info(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR','') or request.META.get('REMOTE_ADDR')
    resp=requests.get('http://api.ipstack.com/'+str(ip)+'?access_key=f4ba4c232d730f863e9708d0d44c7dc5')
    data=resp.json()
    print(data)
    return render(request,'testapp/info.html',data)
"""
x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
if x_forwarded_for:
    ip = x_forwarded_for.split(',')[-1].strip()
else:
    ip = request.META.get('REMOTE_ADDR')
return ip"""
