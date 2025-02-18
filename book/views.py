from django.shortcuts import render, redirect
from .mongodb import book_collection
from .forms import BookForm
from bson.objectid import ObjectId
from decimal import Decimal

def book_list(request):
    books = list(book_collection.find())
    for book in books:
        book['id'] = str(book['_id'])
        book['price'] = Decimal(book['price'])
    return render(request, 'book/book_list.html', {'books': books})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book_data = form.cleaned_data
            book_data['price'] = str(book_data['price'])
            book_collection.insert_one(book_data)
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})

def book_edit(request, pk):
    book = book_collection.find_one({'_id': ObjectId(pk)})
    book['price'] = Decimal(book['price'])
    if request.method == "POST":
        form = BookForm(request.POST, initial=book)
        if form.is_valid():
            book_data = form.cleaned_data
            book_data['price'] = str(book_data['price'])
            book_collection.update_one({'_id': ObjectId(pk)}, {'$set': book_data})
            return redirect('book_list')
    else:
        form = BookForm(initial=book)
    return render(request, 'book/book_form.html', {'form': form})

def book_delete(request, pk):
    book_collection.delete_one({'_id': ObjectId(pk)})
    return redirect('book_list')