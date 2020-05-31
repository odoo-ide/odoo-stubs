from ..exceptions import UserError
from ..models import AbstractModel, Model, TransientModel

except_osv = UserError
osv = Model
osv_memory = TransientModel
osv_abstract = AbstractModel
