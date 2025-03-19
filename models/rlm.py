from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class RlmSolicitud(models.Model):
    _name = 'rlm.solicitud'
    _description = 'Solicitud RLM'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Folio del RLM', required=True, copy=False, index=True, default='Nuevo', readonly=True)
    fecha_solicitud = fields.Date(string='Fecha de Solicitud', default=fields.Date.context_today, required=True)
    fecha_requerida = fields.Date(string='Liberar antes del', required=True)
    almacen_id = fields.Many2one('stock.warehouse', string='Almacén', required=True)
    solicitante_id = fields.Many2one('res.users', string='Solicitante', default=lambda self: self.env.user, required=True)
   

    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('revision', 'En Revisión'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('liberado', 'Liberado')],
        string='Estado del RLM', default='borrador', tracking=True)

    linea_ids = fields.One2many('rlm.solicitud.linea', 'solicitud_id', string='Líneas de solicitud')

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('rlm.solicitud') or 'Nuevo'
        return super(RlmSolicitud, self).create(vals)
    
    # Agrega al final dentro de class RlmSolicitud(models.Model):

    def action_enviar_revision(self):
        self.write({'estado': 'revision'})

    def action_aprobar(self):
        self.write({'estado': 'aprobado'})

    def action_rechazar(self):
        self.write({'estado': 'rechazado'})

    def action_marcar_liberado(self):
        self.write({'estado': 'liberado'})

    def action_reset_borrador(self):
        self.write({'estado': 'borrador'})



class RlmSolicitudLinea(models.Model):
    _name = 'rlm.solicitud.linea'
    _description = 'Línea de solicitud RLM'

    solicitud_id = fields.Many2one('rlm.solicitud', string='Solicitud RLM', required=True)
    product_id = fields.Many2one('product.product', string='Producto a Liberar', required=True)
    cantidad_solicitada = fields.Float(string='Cantidad a Liberar', required=True)
    uom_id = fields.Many2one('uom.uom', string='Unidad de Medida', related='product_id.uom_id', readonly=True, store=True)
