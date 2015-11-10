from django.shortcuts import render_to_response
from models import Author,Book


def window(request):
    return render_to_response('book.html')
    
def showlist(request):
    allbook = Book.objects.all()
    return render_to_response('showlist.html',{'allbook':allbook })
    
    
def detail(request,booktitle):
     book = Book.objects.filter(title = booktitle)[0]
     bookisbn=book.ISBN
     publisher=book.Publisher
     publishdate=book.PublishDate
     price=book.Price
     author=book.authorsID
     
     return render_to_response('detail.html',{'bookisbn': bookisbn,'title':booktitle,'price':price,'publishdate':publishdate,'publisher':publisher,'author':author })

def delete(request,booktitle):
     book = Book.objects.filter(title = booktitle)[0]
     book.delete()
     allbook = Book.objects.all()
     return render_to_response('deleted.html',{'allbook':allbook })
     
def redo(request,booktitle):
     book = Book.objects.filter(title = booktitle)[0]
     #book = Book.get(title = booktitle)
     bookisbn=book.ISBN
     publisher=book.Publisher
     publishdate=book.PublishDate
     price=book.Price
     author=book.authorsID
     return render_to_response('redo.html',{'bookisbn': bookisbn,'title':booktitle,'price':price,'publishdate':publishdate,'publisher':publisher,'author':author })     
     
def redone(request):
        book = Book.objects.get(ISBN = request.GET['isbn'])
        #author = Author.objects.get(name = request.GET['authorid'])
        author = Author.objects.get(AuthorID = request.GET['authorid'])
        #author=Author()
        author.name=request.GET['authorname']
        author.age=request.GET['authorage']
        
        author.country=request.GET['authorcountry']
        author.AuthorID=request.GET['authorid']
        author.save()
        
        
        book.title=request.GET['title']
        book.PublishDate=request.GET['publishdate']
        book.Price=request.GET['price']
        book.authorsID=author
       
       
        book.save()
    
    
        return render_to_response('succedredone.html')     
     
     

def gosearch(request):
    return render_to_response('gosearch.html')    

def addbook(request):
    return render_to_response('addbook.html')
def added(request):
    book=Book()
    author_id =  request.GET['authorid']
    i=0
    allauthor = Author.objects.all()
    for perauthor in  allauthor:
      if (author_id == perauthor.AuthorID):
        i=i+1
        book.authorsID=perauthor
        book.ISBN=request.GET['isbn']
        book.title=request.GET['title']
        book.Publisher=request.GET['publisher']
        book.PublishDate=request.GET['publishdate']
        book.Price=request.GET['price']
        book.save()
        break
    
    
    if( i == 0):
      return render_to_response('toaddauthor.html')
    else:
      allbook = Book.objects.all()
      return render_to_response('showlist.html',{'allbook':allbook })
     
  # return render_to_response('book.html',)    
def toaddauthored(request):
        author=Author()
        author.name=request.GET['name']
        author.age=request.GET['age']
        author.country=request.GET['country']
        author.AuthorID=request.GET['authorid']
        author.save()
        return render_to_response('addauthorsucceed.html')  
    
    
    
    
    
    
    
def search(request):
    if 'authorname' in request.GET:
      
        message =  request.GET['authorname']
    else:
        message = 'You submitted an empty form.'
    try:
        person = Author.objects.get(name= message )
        book = person.book_set.all()
        return render_to_response('search.html',  {'bookname':book,'person':person})
    except  Author.DoesNotExist:
        book = None
    
        return render_to_response('search.html',  {'bookname':book})
   