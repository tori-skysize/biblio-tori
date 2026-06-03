{
    'name': 'Book Library',
    'version': '1.0',
    'category': 'Library',
    'summary': 'Manage your book library',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
    ],
    'installable': True,
    'application': True,
}
