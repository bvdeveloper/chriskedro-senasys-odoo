from odoo import api, fields, models, _

class CatlogSection(models.Model):
    _name ='catalog.section'
    _description = "Catlogtion Sec"
    name = fields.Char(string="Catalog Section",required=True)