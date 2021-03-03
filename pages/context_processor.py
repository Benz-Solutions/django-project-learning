from pages.models import Page

def get_pages(request):
    
    pages = Page.objects.filter(visible=True).values_list('id', 'title', 'slug').order_by('order')
    #pages = Page.objects.values_list('title', flat=True)

    return {
        'pages': pages
    }

