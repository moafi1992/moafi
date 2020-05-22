from django.db import models



class Guest(models.Model):
    session_id=models.CharField(max_length=512)
class Factor(models.Model):
    invoice_number=models.IntegerField(auto_created=True)
    security_code=models.CharField(max_length=64)
    seller_name=models.CharField(max_length=128)
    seller_num=models.CharField(max_length=128)
    seller_add=models.CharField(max_length=512, null=True, blank=True)
    buyer_name=models.CharField(max_length=128)
    buyer_num=models.CharField(max_length=128)
    buyer_add=models.CharField(max_length=512, null=True, blank=True)
    c_date=models.DateTimeField(auto_now_add=True)
    guest=models.ForeignKey(Guest,on_delete=models.CASCADE)

    def __int__(self):
        return (self.id)

class Records(models.Model):
    name=models.CharField(max_length=64)
    code=models.CharField(max_length=64)
    price=models.IntegerField()
    count=models.IntegerField()
    dis_percent=models.IntegerField()
    tax=models.IntegerField()
    factor=models.ForeignKey(Factor,on_delete=models.CASCADE)

    def _total_price(self):
        return self.price*self.count

    total= property(_total_price)


    def __str__(self):
        return (self.name)


