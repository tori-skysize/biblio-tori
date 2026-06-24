from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    pages = fields.Char()
    pages2 = fields.Char()
    pages4 = fields.Char()
