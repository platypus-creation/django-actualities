Django-Actualities
===============

Blog app

Installation
------------

    pip install git+git://github.com/platypus-creation/django-actualities.git

or:

    git clone git://github.com/platypus-creation/django-actualities.git
    cd django-actualities
    python setup.py install


Add `actualities` to your INSTALLED_APPS

    INSTALLED_APPS = (
        ...
        'actualities',
    )

Create the database table
    
    python manage.py syncdb

or if you are using South (you should)

    python manage.py migrate actualities


You are done
