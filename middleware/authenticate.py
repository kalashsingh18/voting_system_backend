from rest_framework_simplejwt.tokens import RefreshToken,UntypedToken,AccessToken
from django.http import HttpResponseRedirect
from login_apis.models import users
def login_check(get_response):
    def middleware(request):
        paths=["/manage_election/create","/manage_election/select_election","/manage_election/extract"]
        print(request.path)
        if request.path in paths:
            auth_header = request.headers.get('Authorization')
            if auth_header :
                    print(auth_header)
                    token = auth_header.split(' ')[1].strip()
                    token=token[0:-1]
                    try :
                        access_token = AccessToken(token)
                    except:
                        try :
                            refresh_token=refresh_token(token)
                            if refresh_token:
                                access_token=refresh_token
                        except:
                            return HttpResponseRedirect("/")
                        return HttpResponseRedirect('/') 
                    user_id = access_token['user_id']
                    # print(user_id,user_id)
                    user=users.objects.filter(id=user_id).first()
                    if user:
                       pass
                    else: 
                        return HttpResponseRedirect('/')  
            else:
                    return HttpResponseRedirect('/') 
        print("server_starts")
        request_data={
                "data":dir(request),
                "ip":request.META.get('REMOTE_ADDR'),
                "path":request.path
        }
        print(request_data)
        Response=get_response(request)
        return Response
    return middleware