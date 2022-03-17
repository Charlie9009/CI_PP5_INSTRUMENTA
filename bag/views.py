from django.shortcuts import render



def view_bag(request):
    """ A view to show the bag """

    return render(request, 'bag/bag.html')
