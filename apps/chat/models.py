from django.db import models

from apps.common.models import BaseModel
from apps.common.utils import uuid4_generator
from apps.product.models import Product
from apps.user.models import Account


def upload_to_s3_chat(instance: models.Model, filename: str) -> str:
    # 파일명은 랜덤한 8자리의 문자열과 업로드한 파일이름을 조합해서 만듦(유일성 보장)
    return f"images/chat/{uuid4_generator(length=8)} + {filename}"


class Chatroom(models.Model):
    borrower = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="borrower")
    lender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="lender")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    borrower_status = models.BooleanField(default=True)
    lender_status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"판매자: {self.borrower.nickname}, 대여자: {self.lender.nickname}의 채팅방"


class Message(BaseModel):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to=upload_to_s3_chat, null=True, blank=True)
    status = models.BooleanField(default=True)  # 메시지의 읽음 여부를 처리

    def __str__(self) -> str:
        return f"{self.sender} : {self.text[:30]}.."
