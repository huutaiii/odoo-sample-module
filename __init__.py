
from odoo import models, fields

class TestModel(models.Model):
    _name = "test.model"
    _description = "some model"

    name = fields.Char('some name')
    date = fields.Date()
    i = fields.Integer('some int')
