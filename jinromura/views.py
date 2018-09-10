from django.shortcuts import render,get_object_or_404
from .models import Village,Character

# Create your views here.
#検索・一覧画面
def index(request):
    village_list = Village.objects.all()
    context={'village_list':village_list}
    return render(request, 'jinromura/index.html',context)

#詳細画面
def detail(request,village_id):
    #オブジェクト（各々の村）取得か４０４エラー
    village = get_object_or_404(Village,pk=village_id)
    return render(request, 'jinromura/detail.html',{'village':village})