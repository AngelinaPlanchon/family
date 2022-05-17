from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader 



from familia2.models import familia2



def family (self):
     
    family1= familia2(name = 'Maria', 
    last_name  = 'Sosa', 
    profession = 'Doctor', 
    age = 56,
    birthday = '1966-1-27' ,)

    family1.save()

    family2= familia2(name = 'Pablo', 
    last_name  = 'Pereira', 
    profession = 'Architect',
    age = 40, 
    birthday = '1982-3-20',)

    family2.save()
    
    family3= familia2(name = 'Kate', 
    last_name  = 'Perez',
    profession = 'Lawyer', 
    age = 28, 
    birthday = '1997-7-15',)

    family3.save()



    

    dictionary = {
        
        'f1name': family1.name,
        'f1last_name': family1.last_name,
        'f1profession': family1.profession,
        'f1age': family1.age,
        'f1birthday': family1.birthday,
        'f2name': family2.name,
        'f2last_name': family2.last_name,
        'f2profession': family2.profession,
        'f2age': family2.age,
        'f2birthday': family2.birthday,
        'f3name': family3.name,
        'f3last_name': family3.last_name,
        'f3profession': family3.profession,
        'f3age': family3.age,
        'f3birthday': family3.birthday,

    }

    template= loader.get_template('template.html')
    render = template.render(dictionary)
    return HttpResponse(render)
        


