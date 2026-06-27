from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    pages = fields.Char()
    pages2 = fields.Char()
    pages4 = fields.Char()
    pages5 = fields.Char()
    pages6 = fields.Char()
    pages7 = fields.Char()
    pages8 = fields.Char()
