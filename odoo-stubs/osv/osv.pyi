from ..exceptions import except_orm as except_orm
from .orm import AbstractModel as AbstractModel, Model as Model, TransientModel as TransientModel

except_osv = except_orm
osv = Model
osv_memory = TransientModel
osv_abstract = AbstractModel
