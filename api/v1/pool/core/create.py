# from datetime import datetime
# from typing import Any
#
# from pydantic.v1 import ValidationError
#
# from api.v1.pool.core.models import CreatePoolRequest, Pool
# from api.v1.dependencies.interfaces import FactoryInterface
# import uuid
# from ..core.data import PoolModel
#
#
# def _generate_unique_id() -> uuid.UUID:
#     while True:
#         _id = uuid.uuid4()
#         try:
#             PoolModel.get(hash_key=_id)
#             continue
#         except PoolModel.DoesNotExist:
#             return _id
#
#
# class RootPoolFactory(FactoryInterface):
#     def __init__(self, request: CreatePoolRequest):
#         self.request = request
#
#     def _validate(self, pool_item: dict, *args, **kwargs):
#         return Pool(**pool_item)
#
#     def create(self) -> PoolModel:
#         pool_id = _generate_unique_id()
#         _pool_dict = self.request.model_dump()
#
#         _pool_dict['created_date'] = datetime.now().date().__str__()
#         _pool_dict['updated_date'] = datetime.now().date().__str__()
#         if self.request.hierarchy_level == "root":
#             _pool_dict["top_level_pool_id"] = pool_id
#
#
#         pool_data[pool_id] =
#         return pool_id
