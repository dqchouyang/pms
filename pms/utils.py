from adminlte.utils import RootMenu, AdminLTEBaseView
from django.contrib.auth.models import AnonymousUser


def admin_config(request):
    if request.resolver_match:
        avatar_url = '/static/adminLTE/img/avatar5.png'
        if isinstance(request.user, AnonymousUser):
            name = '游客'
            date_joined = None
        else:
            name = request.user.username
            date_joined = request.user.date_joined

        return {
            "ROOT_MENU": RootMenu(current_view_name=request.resolver_match.view_name,
                                  init_menus=AdminLTEBaseView.menus(request.user)),
            "current_user": {
                "nickname": name,
                "avatar_url": avatar_url,
                "date_joined": date_joined,
            },
        }
