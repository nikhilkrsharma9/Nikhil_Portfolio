from django.shortcuts import render, redirect

def portfolio(request):
    # Define projects directly in the view
    projects = [
        {
            'title': 'Doctor’s Appointment Booking System',
            'description': 'A virtual showcase of contemporary artwork',
            'icon': 'image'
        },
        {
            'title': 'Cricket Management System',
            'description': 'Interactive web experiences with fluid animations',
            'icon': 'shapes'
        },
        {
            'title': 'Color Theory App',
            'description': 'Educational tool for understanding color harmonies',
            'icon': 'palette'
        },
        {
            'title': 'Code Portfolio',
            'description': 'Collection of programming projects and experiments',
            'icon': 'code'
        }
    ]
    
    skills = [
        {'name': 'Django', 'level': 75},
        {'name': 'Python', 'level': 80},
        {'name': 'MongoDb', 'level': 60},
        {'name': 'Html/Css/JS', 'level': 80}
    ]

    context = {
        'name': 'Your Name',
        'email': 'nikhilkumar09012002@gmail.com',
        'projects': projects,  # Add projects to context
        'skills': skills      # Add skills to context
    }
    return render(request, 'portfolio/portfolio.html', context)

def contact(request):
    if request.method == 'POST':
        # Handle form submission here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Add your email sending logic here
        return redirect('portfolio')
    return redirect('portfolio')