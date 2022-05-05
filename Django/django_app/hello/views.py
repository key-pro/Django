
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
from .models import Friend
#from .models import Friend, Message
#from .forms import FriendForm, MessageForm
from django.db.models import QuerySet
from .forms import FriendForm
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Min, Max
from .forms import CheckForm
from django.core.paginator import Paginator

"""def index(request):
    return HttpResponse("Hello Django!!")
    if 'msg' in request.GET:
        msg = request.GET['msg']
        result = 'you typed: "' + msg + '".'
    else:
        result = 'please send msg parameter!'
    return HttpResponse(result)
"""
"""def index(request, id, nickname):
    result = 'your id: ' + str(id) + ', name: "' \
    + nickname + '".'
    return HttpResponse(result)
"""

"""def index(request, nickname, age):
    result = 'your account: ' + nickname + '" (' + str(age) + ').'
    return HttpResponse(result)
"""

"""def index(request):
    return render(request, 'hello/index.html')
"""

"""def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next',
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'これは、もう１つのページです。',
        'goto':'index',
    }
    return render(request, 'hello/index.html', params)
"""

"""def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'お名前は？',
    }
    return render(request, 'hello/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'Hello/Form',
        'msg':'こんにちは、' + msg + 'さん。',
    }
    return render(request, 'hello/index.html', params)
"""

"""def index(request):
    params = {
        'title':'Hello',
        'message':'your data:',
        'form':HelloForm()
    }
    if(request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name'] + \
        '<br>メール：' + request.POST['mail'] + \
        '<br>年齢：' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html', params)
"""

"""class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello',
            'message':'your data',
            'form':HelloForm()
        }
    
    def get(self, request):
        return render(render, 'hello/index.html', self.params)
    
    def post(self, request):
        msg = 'あなたは、<b>' + request.POST['name'] + \
        '(' + request.POST['age'] + \
        ') <b>さんですね。<br> メールアドレスは <b> ' + request.POST['mail'] + \
        '<b>ですね。'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
"""

"""class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello',
            'form':HelloForm(),
            'result':None
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)
    
    def post(self, request):
        if('check' in request.POST):
            self.params['result'] = 'Checked!!'
        else:
            self.params['result'] = 'not checked...'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
"""

"""class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello',
            'form':HelloForm(),
            'result':None
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)
    
    def post(self, request):
        chk = request.POST['check']
        self.params['result'] = 'you selected: "' + chk + '".'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
"""

"""class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'form': HelloForm(),
            'result':None
        }
    
    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        ch = request.POST['choice']
        self.params['result'] = 'selected: "' + ch + '".'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
"""

"""class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'form': HelloForm(),
            'result':None
        }
    
    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        ch = request.POST['choice']
        self.params['result'] = 'selected: "' + ch + '".'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
"""

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello',
            'form':HelloForm(),
            'result':None
        }
    
    def get(self, request):
        return render(request, 'hello/index.html', self.params)
    
    """def post(self, request):
        ch = request.POST.getlist('choice')
        self.params['result'] = 'selected: ' + str(ch) + '.'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
    """

    def post(self, request):
        ch = request.POST.getlist('choice')
        result = '<ol class="list-group"><b>selected:</b>'
        for item in ch:
            result += '<li class="list-group-item">' + item + '</li>'
        result +='</ol>'
        self.params['result'] = result
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)

"""def index(request):
    data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':'all friends.',
        'data': data,
    }
    return render(request, 'hello/index.html', params)
"""

"""def index(request):
    params = {
        'title':'Hello',
        'message':'all friends',
        'form':HelloForm(),
        'data': [],
    }

    if(request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    return render(request, 'hello/index.html', params)
"""

"""def index(request):
    data = Friend.objects.all()
    params = {
        'title':'Hello',
        'data':data,
    }
    return render(request, 'hello/index.html', params)
"""

"""def index(request):
    data = Friend.objects.all().values()
    params = {
        'title':'Hello',
        'data':data,
    }
    return render(request, 'hello/index.html', params)
"""

"""def index(request):
    data = Friend.objects.all().values('id', 'name')
    params = {
        'title':'Hello',
        'data':data,
    }
    return render(request, 'hello/index.html', params)
"""

"""def index(request):
    data = Friend.objects.all().values_list('id', 'name', 'age')
    params = {
        'title':'Hello',
        'data':data,
    }
    return render(request, 'hello/index.html', params)
"""

"""def index(request):
    num = Friend.objects.all().count()
    first = Friend.objects.all().first()
    last = Friend.objects.all().last()
    data = [num, first, last]
    params = {
        'title':'Hello',
        'data':data,
    }
    return render(request, 'hello/index.html', params)
"""

"""def __new_str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
        result += '</td>'
    return result

QuerySet.__str__ = __new_str__

def index(request):
    data = Friend.objects.all().values('id', 'name', 'age')
    params = {
        'title':'Hello',
        'data':data,
    }
    return render(request, 'hello/index.html', params)
"""

"""def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)
"""

# create model
def create(request):
    params = {
        'title': 'Hello',
        'form': HelloForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        gender = 'gender' in request.POST
        age = int(request.POST['age'])
        birth = request.POST['birthday']
        friend = Friend(name=name,mail=mail,gender=gender,\
                age=age,birthday=birth)
        friend.save()
        return redirect(to='/hello')
    return render(request, 'hello/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

"""def find(request):
    if(request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Friend.objects.filter(name=find)
        msg = 'Result: ' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'form':form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)
"""

"""def find(request):
    if(request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        #data = Friend.objects.filter(name__contains=find)
        #data = Friend.objects.filter(name__iexact=find)
        data = Friend.objects.filter(age__lte=int(find))
        msg = 'Result: ' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)
"""

"""def find(request):
    if(request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        val = find.split()
        #data = Friend.objects.filter(age__gte=val[0], age__lte=val[1])
        data = Friend.objects \
        .filter(age__gte=val[0]) \
        .filter(age__lte=val[1])
        msg = 'Result: ' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)
"""

"""def find(request):
    if(request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Friend.objects.filter(Q(name__contains=find)|Q(mail__contains=find))
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)
"""

"""def find(request):
    if(request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        find = request.POST['find']
        list = find.split()
        data = Friend.objects.filter(name__in=list)
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)
"""

"""def index(request):
    data = Friend.objects.all().order_by('age')
    params = {
        'title':'Hello',
        'message':'',
        'data':data,
    }
    return render(request, 'hello/index.html', params)
"""

"""def index(request):
    data = Friend.objects.all().order_by('age').reverse()
    params = {
        'title':'Hello',
        'message':'',
        'data':data,
    }
    return render(request, 'hello/index.html', params)
"""

"""def find(request):
    if(request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        find = request.POST['find']
        list = find.split()
        data = Friend.objects.all()[int(list[0]):int(list[1])]
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)
"""

"""def index(request):
    data = Friend.objects.all()
    re1 = Friend.objects.aggregata(Count('age'))
    re2 = Friend.objects.aggregata(Sum('age'))
    re3 = Friend.objects.aggregata(Avg('age'))
    re4 = Friend.objects.aggregata(Min('age'))
    re5 = Friend.objects.aggregata(Max('age'))
    msg = 'count: ' + str(re1['age__count']) \
        + '<br>Sum: ' + str(re2['age__sum']) \
        + '<br>Average: ' + str(re3['age__avg']) \
        + '<br>Min: ' + str(re2['age__min']) \
        + '<br>Max: ' + str(re2['age__max']) 
    params = {
        'title':'Hello',
        'message':msg,
        'data':data,
    }
    return render(request, 'hello/index.html',params)
"""

def find(request):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from hello_friend'
        if (msg != ''):
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data =Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form':form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)

def check(request):
    params = {
        'title':'Hello',
        'message':'check validation',
        'form':CheckForm(),
    }
    if(request.method == 'POST'):
        form = CheckForm(request.POST)
        params['form'] = form
        if(form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/check.html', params)

def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        'title': 'Hello',
        'message':'',
        'data': page.get_page(num),
    }
    return render(request, 'hello/index.html', params)

"""def message(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'hello/message.html', params)
"""