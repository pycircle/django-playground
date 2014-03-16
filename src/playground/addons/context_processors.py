# -*- coding: utf-8 -*-

def custom_proc(request):
    "A context processor that provides 'app' and 'ip_address'."
    return {
        'app': 'Django playground',
        'ip_address': request.META['REMOTE_ADDR']
    }


"""
Zadanie:
Napisz własny context processor który będzie dostarczać
do każdego widoku listę skwadratowanych liczb parzystych od 2 do 100.
"""