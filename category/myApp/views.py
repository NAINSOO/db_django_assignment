from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db import connection
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

output1 = []
output2 = []
output3 = []
output4 = []

def display(request):

    if request.method == "POST":
        laptopForm = LaptopForm(request.POST)
        if laptopForm.is_valid():
            laptopForm.save()
    else:
        laptopForm = LaptopForm()



    outputProduct = []
    outputPrinter = []
    outputPc = []
    outputLaptop = []
    with connection.cursor() as cursor:
        sqlQueryProduct = "SELECT maker, model, type FROM product;"
        cursor.execute(sqlQueryProduct)
        fetchResultProduct = cursor.fetchall()

        sqlQueryPrinter = "SELECT model, color, type, price FROM printer;"
        cursor.execute(sqlQueryPrinter)
        fetchResultPrinter = cursor.fetchall()

        sqlQueryPc = "SELECT model, speed, ram, hd, price FROM pc;"
        cursor.execute(sqlQueryPc)
        fetchResultPc = cursor.fetchall()

        sqlQueryLaptop = "SELECT * FROM laptop;"
        cursor.execute(sqlQueryLaptop)
        fetchResultLaptop = cursor.fetchall()

    connection.commit()
    connection.close()

    for temp in fetchResultProduct:
        eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
        outputProduct.append(eachRow)

    for temp in fetchResultPrinter:
        eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
        outputPrinter.append(eachRow)

    for temp in fetchResultPc:
        eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
        outputPc.append(eachRow)

    for temp in fetchResultLaptop:
        eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4], 'screen': temp[5]}
        outputLaptop.append(eachRow)

    return render(request, 'myApp/index.html', {"product": outputProduct, "printer": outputPrinter, "pc": outputPc, "laptop": outputLaptop,
                                                 'laptopForm': laptopForm,
                                                'query1': output1, 'query2': output2, 'query3': output3, 'query4': output4})


def getProduct(request):
    x = request.POST['maker']
    y = request.POST['model']
    z = request.POST['type']

    product = Product(maker=x, model=y,type=z)
    product.save()
    return HttpResponseRedirect(reverse('index'))

def addProduct(request):
    template = loader.get_template('myApp/addproduct.html')
    return HttpResponse(template.render({}, request))

def getPrinter(request):
    x = request.POST['model']
    y = request.POST['color']
    z = request.POST['type']
    w = request.POST['price']

    printer = Printer(model=x, color=y, type=z, price =w)
    printer.save()
    return HttpResponseRedirect(reverse('index'))

def addPrinter(request):
    template = loader.get_template('myApp/addprinter.html')
    return HttpResponse(template.render({}, request))

def getPC(request):
    x = request.POST['model']
    y = request.POST['spedd']
    z = request.POST['ram']
    w = request.POST['hd']
    v = request.POST['price']
    pc = Pc(model=x, speed=y, ram=z, hd =w, price=v)
    pc.save()
    return HttpResponseRedirect(reverse('index'))

def addPC(request):
    template = loader.get_template('myApp/addpc.html')
    return HttpResponse(template.render({}, request))

def deletePc(request, id):
  pc = Pc.objects.get(model=id)
  pc.delete()
  return HttpResponseRedirect(reverse('index'))

def deleteProduct(request, id):
  product = Product.objects.get(model=id)
  product.delete()
  return HttpResponseRedirect(reverse('index'))

def deletePrinter(request, id):
  printer = Printer.objects.get(model=id)
  printer.delete()
  return HttpResponseRedirect(reverse('index'))

def deleteLaptop(request, id):
  laptop = Laptop.objects.get(model=id)
  laptop.delete()
  return HttpResponseRedirect(reverse('index'))

def query1(request):
    output1.clear()
    if request.method == "GET":
        with connection.cursor() as cursor:
            sqlQuery1 = "SELECT AVG(hd) FROM pc;"
            cursor.execute(sqlQuery1)
            fetchResult1 = cursor.fetchall()
        connection.commit()
        connection.close()
        for temp in fetchResult1:
            eachRow = {'average': temp[0]}
            output1.append(eachRow)
    return HttpResponseRedirect(reverse('index'))

def query2(request):
    output2.clear()
    if request.method == "GET":
        with connection.cursor() as cursor:
            sqlQuery2 = "SELECT maker, AVG(speed) FROM laptop INNER JOIN product ON laptop.model = product.model GROUP BY maker ;"
            cursor.execute(sqlQuery2)
            fetchResult2 = cursor.fetchall()
        connection.commit()
        connection.close()
        for temp in fetchResult2:
            eachRow = {'maker': temp[0], 'average': temp[1]}
            output2.append(eachRow)
    return HttpResponseRedirect(reverse('index'))

def query3(request):
    output3.clear()
    if request.method == "GET":
        with connection.cursor() as cursor:
            sqlQuery3 = "SELECT R.maker,R.model,price FROM laptop, (SELECT product.model, product.maker FROM product WHERE type='laptop' GROUP BY(maker) HAVING(count(type='laptop')=1)) R WHERE laptop.model = R.model ;"
            cursor.execute(sqlQuery3)
            fetchResult3 = cursor.fetchall()
        connection.commit()
        connection.close()
        for temp in fetchResult3:
            eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
            output3.append(eachRow)
    return HttpResponseRedirect(reverse('index'))

def query4(request):
    output4.clear()
    if request.method == "GET":
        with connection.cursor() as cursor:
            sqlQuery4 = "SELECT maker,printer.model, MAX(price) FROM categorydb.printer INNER JOIN categorydb.product ON printer.model = product.model GROUP BY maker;"
            cursor.execute(sqlQuery4)
            fetchResult4 = cursor.fetchall()
        connection.commit()
        connection.close()
        for temp in fetchResult4:
            eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
            output4.append(eachRow)
    return HttpResponseRedirect(reverse('index'))



def inputData(request):
    if request.method == "POST":
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriesForm()
    return render(request, "myApp/input.html", {'form':form})
