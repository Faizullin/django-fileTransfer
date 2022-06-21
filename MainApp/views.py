from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse , HttpResponseNotFound
from .forms import UploadFileForm
from. models import FileModel

# Create your views here.
def index(request):
	items = FileModel.objects.order_by("-time_update")
	context = {
		'files':items,
		'title':"MAIN"
	}
	return render(request,'index.html',context=context)

def show(request,file_id):
	items = get_object_or_404(FileModel, pk=file_id)
	# if(len(items)==0):
	# 	raise Http404()
	context = {
		'item':items,
		'title':"FILE"
	}
	return redirect(f'/media/{items.file}')
	# return HttpResponse(str(context)+f'<a href="/change_file/{items.pk}">change</a>')

def change_file(request,file_id):
	f = FileModel.objects.get(id=file_id)
	#f.time_update=None
	f.save()
	return redirect("home")

def pageNotFound(request,exception):
	return HttpResponseNotFound("NOT FOUND - 404")
def upload(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)#, request.FILES
		if form.is_valid():
			print(form.cleaned_data)
			try:
				form.save()
				return redirect('home')
			except:
				form.add_error(None,"Ошибка добавления поста")
			return HttpResponse("post upload")
			
		else:
			return HttpResponse("Error: NOT VALID!")
	else:
		form = UploadFileForm()
	context = {'form': form,'title':'UPLOAD'};
	return render(request, 'upload.html', context)




def long_process(request):
	pass


def download():
	return HttpResponse("GOOF")