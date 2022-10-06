from django.db import models
# from django.contrib.auth.models import User
class BarangWishlist(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.IntegerField()
    deskripsi = models.TextField()