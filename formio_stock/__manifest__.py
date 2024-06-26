{
    'name': 'Forms | Stock',
    'summary': 'Forms integration with Stock',
    'version': '12.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'website': 'www.multidados.tech',
    'category': 'Stock',
    'contributors': [
        'Augusto Costa <gustotc@gmail.com>',
    ],
    'depends': ['stock',
                'formio',
                'formio_data_api'
    ],
    'data': [
        'data/formio_stock_data.xml',
        'views/formio_form_views.xml',
        'views/stock_picking_view.xml',
    ],
    'application': True,
    'installable': True,
    'images': [
        'static/description/banner.gif',
    ],
    'description': """
Forms | Stock
=============

"""
}
