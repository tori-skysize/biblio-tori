from odoo import models, fields
wewe

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
