from pydantic import BaseModel


class BaseResponse(BaseModel):
    message: str
    status: str
    data: dict
    error: dict

#
# DEFAULT_RESPONSE = {
#         "statusCode": 0,
#         "body": "",
#         "isBase64Encoded": True | False,
#         "headers": {
#             "Access-Control-Allow-Headers": "*",
#             "Access-Control-Allow-Origin": "*",
#             "Access-Control-Allow-Methods": "*"
#         }
#     }