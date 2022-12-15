{
    'name': 'Forms | Service Contract',
    'summary': 'Forms Integration with Service Contract',
    'version': '12.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'website': 'www.multidados.tech',
    'category': 'Forms/Forms',
    'contributors': [
        'Fernando Saeta <fernando.r.saeta@gmail.com>',
    ],
    'depends': ['service_contract_line_event',
                'formio',
                'formio_data_api'
    ],
    'data': [
        'data/formio_contract_data.xml',
        'views/formio_form_views.xml',
        'views/service_contract.xml',
    ],
    'application': True,
    'installable': True,
    'images': [
        'static/description/banner.gif',
    ],
    'description': """
Forms | Service Contract
=============

"""
}
