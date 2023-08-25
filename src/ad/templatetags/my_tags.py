from django import template
from ad import models
from django.db.models import Q

register = template.Library()

@register.filter
def borrowing(user):
    return models.LoanTransaction.objects.all().filter(user = user, returned = '0').count()

@register.filter
def returned(user):
    return models.LoanTransaction.objects.all().filter(user = user, returned = '1').count()

@register.filter
def overdued(user):
    return models.LoanTransaction.objects.all().filter(user = user, overdue = '1').count()

@register.filter
def loan(user):
    try:
        return models.LoanTransaction.objects.all().filter(user = user, returned = '0')[0:2]
    except:
        return None

@register.filter
def nocomma(i, length):
    return i < len(length)

@register.filter
def bookcount(category):
    return models.Book.objects.all().filter(category = category).count()

@register.filter
def booknum(i):
    return models.Book.objects.all().count()


@register.filter
def categorynum(i):
    return models.Category.objects.all().count()

@register.filter
def languagenum(i):
    return models.Language.objects.all().count()

@register.filter
def sourcetypenum(i):
    return models.SourceType.objects.all().count()

@register.filter
def adnum(i):
    return models.Profile.objects.all().filter(role = "ADMIN").count()

@register.filter
def libnum(i):
    return models.Profile.objects.all().filter(role = "LIBRARIAN").count()

@register.filter
def readernum(i):
    return models.Profile.objects.all().filter(role = "READER").count()

@register.filter
def book_requests(i):
    return models.BookRequest.objects.all().filter(status = '1').order_by('date_added')

@register.filter
def reader_requests(i):
    return models.ReaderRequest.objects.all().filter(status = '1').order_by('date_added')

@register.filter
def book_responses(i):
    return models.BookRequest.objects.all().filter(Q(status = '2') | Q(status = '3')).order_by('date_added')

@register.filter
def reader_responses(i):
    return models.ReaderRequest.objects.all().filter(Q(status = '2') | Q(status = '3')).order_by('date_added')

@register.filter
def adnoti(i):
    return models.BookRequest.objects.all().filter(status = '1').count() + models.ReaderRequest.objects.all().filter(status = '1').count()

@register.filter
def libnoti(i):
    return models.BookRequest.objects.all().filter(Q(status = '2') | Q(status = '3')).count() + models.ReaderRequest.objects.all().filter(Q(status = '2') | Q(status = '3')).count()

@register.filter
def bookavai(i):
    return models.Book.objects.all().filter(status = '1').count()

@register.filter
def bookunavai(i):
    return models.Book.objects.all().filter(status = '2').count()

@register.filter
def bookbeingborrowed(i):
    return models.LoanTransaction.objects.all().filter(returned = '0').count()

@register.filter
def bookrequest(i):
    return models.BookRequest.objects.all().filter(status = '1').count()

@register.filter
def readerrequest(i):
    return models.ReaderRequest.objects.all().filter(status = '1').count()

@register.filter
def bookborrowed(id):
    return models.LoanTransaction.objects.all().filter(user = id).count()