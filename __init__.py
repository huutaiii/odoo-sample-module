
from odoo import models, fields, exceptions, api
from random import randint

class TestModel(models.Model):
    _name = "test.model"
    _description = "some model"

    name = fields.Char('some name', required=True)
    date = fields.Date()
    i = fields.Integer('some int')
    tag_ids = fields.Many2many("test.tag", string="tags")
    random = fields.Integer('random number', compute="_compute_random")

    def _compute_random(self):
        for record in self:
            record.random = randint(0, 100000)

class Tag(models.Model):
    _name = "test.tag"
    _description = " "
    
    name = fields.Char()