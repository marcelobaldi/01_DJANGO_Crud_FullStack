from django.shortcuts import render, redirect
from django.db.models.functions import Lower
from django.core.validators import validate_email
from django.contrib import messages
from .models import Custumer

global codForm, id, name, age, email, passw

def findByEmail(email):
    custumers = Custumer.objects.filter(email__iexact=email)
    if custumers:
        return True

def lastIdRegistered():
    return Custumer.objects.latest('id').id

def quantTotalRegister():
    return Custumer.objects.count()


def save(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age').replace(" ", "")
        email = request.POST.get('email').replace(" ", "")
        passw = request.POST.get('passw').replace(" ", "")

        if not name or not age or not email or not passw:
            messages.warning(request, 'Há Campos Vazios')
            return render(request, 'custumers/create.html')

        try:
            validate_email(email)
        except:
            messages.warning(request, 'E-Mail Inválido!')
            return render(request, 'custumers/create.html')

        age = int(age)

        if len(passw) < 6:
            messages.warning(request, 'A Senha Deve Ter No Mínimo 6 Caracteres')
            return render(request, 'custumers/create.html')

        if not id:
            if findByEmail(email):
                messages.warning(request, 'Email Já Existente')
                return render(request, 'custumers/create.html')

            custumer = Custumer(name=name, age=age, email=email, passw=passw)
            custumer.save()

            messages.success(request, str('Sucesso - Código: ') + str(lastIdRegistered()))
            return redirect('Save')
        else:
            custumer = Custumer(id=id, name=name, age=age, email=email, passw=passw)
            custumer.save()

            messages.success(request, 'Alterado Com Sucesso!')
            return redirect('Read')

    return render(request, 'custumers/create.html')


def read(request):
    listCustumers = Custumer.objects.order_by('id').reverse()[:50]

    if request.method == 'POST':
        codForm = request.POST.get('codForm')

        if codForm == "1":
            id = request.POST.get('id')
            if not id:
                messages.warning(request, 'Há Campos Vazios')
                return render(request, 'custumers/read.html')

            listId = Custumer.objects.filter(id=id)

            if not listId:
                messages.warning(request, 'Id Não Encontrado!')
                return render(request, 'custumers/read.html')

            return render(request, 'custumers/read.html', {
                'keyCustumerId': listId,
                'KeyCustumerFinded': len(listId),
                'keyCustumerTotal': quantTotalRegister(),
            })

        elif codForm == "2":
            name = request.POST.get('name')
            if not name:
                messages.warning(request, 'Há Campos Vazios')
                return render(request, 'custumers/read.html')

            listNames = Custumer.objects.order_by(Lower('name')).filter(name__icontains=name)

            if not listNames:
                messages.warning(request, 'Nome Não Encontrado!')
                return render(request, 'custumers/read.html')

            return render(request, 'custumers/read.html', {
                'keyCustumerName': listNames,
                'KeyCustumerFinded': len(listNames),
                'keyCustumerTotal': quantTotalRegister()
            })

        elif codForm == "3":
            age1 = request.POST.get('age1')
            age2 = request.POST.get('age2')

            if not age1 or not age2:
                messages.warning(request, 'Há Campos Vazios')
                return render(request, 'custumers/read.html')

            listAges = Custumer.objects.filter(age__range=(age1, age2))

            if not listAges:
                messages.warning(request, 'Faixa Etária Não Encontrada!')
                return render(request, 'custumers/read.html')

            return render(request, 'custumers/read.html', {
                'keyCustumerAge': listAges,
                'KeyCustumerFinded': len(listAges),
                'keyCustumerTotal': quantTotalRegister()
            })

    else:
        return render(request, 'custumers/read.html', {
            'keyCustumerAll': listCustumers,
            'KeyCustumerFinded': len(listCustumers),
            'keyCustumerTotal': quantTotalRegister(),
        })


def sendUpdate(request, idRoute):
    custumer = Custumer.objects.get(id=idRoute)

    return render(request, 'custumers/update.html', {
        'keyCustumer': custumer
    })


def sendDelete(request, idRoute):
    custumer = Custumer.objects.get(id=idRoute)

    return render(request, 'custumers/delete.html', {
        'keyCustumer': custumer,
    })


def delete(request):
    action = request.POST.get('action')
    id = request.POST.get('id')

    if action == "1":
        custumer = Custumer(id=id)
        custumer.delete()
        messages.success(request, 'Deletado com Sucesso!')
        return redirect('Read')

    if action == "2":
        return redirect('SendUpdate', idRoute=id)


