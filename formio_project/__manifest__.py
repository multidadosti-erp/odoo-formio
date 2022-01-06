{
    'name': 'Forms | Project',
    'summary': 'Forms integration with Projects',
    'version': '12.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'website': 'www.multidados.tech',
    'category': 'Project',
    'contributors': [
        'Fernando Saeta <fernando.r.saeta@gmail.com>',
    ],
    'depends': ['project',
                'formio',
                'formio_data_api'
    ],
    'data': [
        'data/formio_project_data.xml',
        'views/formio_form_views.xml',
        'views/project_views.xml',
    ],
    'application': True,
    'installable': True,
    'images': [
        'static/description/banner.gif',
    ],
    'description': """
Forms | Project
=============

"""
}
