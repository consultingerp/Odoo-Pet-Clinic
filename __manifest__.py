# -*- coding: utf-8 -*-
{
    'name': "Pet Clinic",

    'summary': """
       Pet Clinic""",

    'description': """
        Long description of module's purpose
    """,

    'author': "jangakniat",
    'website': "http://www.ubig.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'as_time'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'wizards/views/create_visitation.xml',
        'wizards/views/create_pet.xml',
        'wizards/views/create_service.xml',
        'views/client.xml',
        'views/pet.xml',
        'views/appointment.xml',
        'views/visitation.xml',
        'views/service.xml',
        'views/doctor.xml',
        'views/item.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
