{
    'name': 'Requisición de Liberación de Material (RLM)',
    'version': '17.0.1.0.0',
    'summary': 'RLM (Requisición de Liberación de Material)',
    'description': """
        Módulo para gestión completa del proceso de resoluciones de materia prima (RLM), permitiendo solicitud, seguimiento y archivo documental.
    """,
    'author': 'Alphaqueb Consulting SAS',
    'category': 'Inventory/Purchase',
    'depends': ['base', 'mail', 'product', 'stock'],
    'data': [
        'security/rlm_security.xml',
        'security/ir.model.access.csv',
        'data/rlm_sequence.xml',
        'views/rlm_views.xml',
        'views/rlm_menus.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
