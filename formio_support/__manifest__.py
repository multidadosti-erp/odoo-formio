{
    'name': 'Forms | Ticket',
    'summary': 'Forms integration with Support Ticket',
    'version': '12.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'category': 'Others',
    'contributors': [
        'Fernando Saeta <fernando.r.saeta@gmail.com>',
    ],
    'depends': ['website_helpdesk_support_ticket',
                'formio',
                'formio_data_api'
    ],
    'data': [
        'data/formio_helpdesk_support_data.xml',
        'views/formio_form_views.xml',
        'views/helpdesk_support_view.xml',
    ],
    'application': True,
    'installable': True,
    'images': [
        'static/description/banner.gif',
    ],
    'description': """
Forms | Ticket
=============

"""
}
