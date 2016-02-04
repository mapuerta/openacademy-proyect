
from openerp import fields, models

class Partner(models.Model):
   _inherit = 'res.partner'

   instructor = fields.Boolean(default=False)
   session_ids = fields.Many2many('openacademy.session',
                                  string="Session as instructor",
                                  readonly=True)

