{
    'name': 'Gestión de RDM',
    'version': '17.0.1.0.0',
    'summary': 'Gestiona requisición de materia prima (RDM)',
    'description': """
        Módulo para gestión completa del proceso de resoluciones de materia prima (RDM), permitiendo solicitud, autorización, seguimiento y archivo documental.
    """,
    'author': 'Alphaqueb Consulting SAS',
    'category': 'Inventory/Purchase',
    'depends': ['base', 'mail', 'product', 'stock'],
    'data': [
        'security/rdm_security.xml',
        'security/ir.model.access.csv',
        'data/rdm_sequence.xml',
        'views/rdm_views.xml',
        'views/rdm_menus.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
