from ..exceptions import except_orm
from ..models import AbstractModel, Model, TransientModel

except_osv = except_orm
osv = Model
osv_memory = TransientModel
osv_abstract = AbstractModel
