# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

{
    'name': 'Forms | Purchase',
    'summary': 'Forms integration with Purchase Orders',
    'version': '1.0',
    'license': 'LGPL-3',
    'author': 'Nova Code',
    'website': 'https://www.novacode.nl',
    'live_test_url': 'https://demo14.novacode.nl',
    'category': 'Inventory/Purchase',
    'depends': ['purchase', 'formio', 'formio_data_api'],
    'data': [
        'data/formio_purchase_data.xml',
        'data/formio_demo_data.xml',
        'views/formio_form.xml',
        'views/purchase_order.xml',
    ],
    'application': True,
    'images': [
        'static/description/banner.gif',
    ],
    'description': """
Form fields and counters are restricted to Forms users. Purchase users do not
need access to forms to read or update orders. Renaming an order synchronizes
the linked forms' record names without granting access to their contents.
"""
}
