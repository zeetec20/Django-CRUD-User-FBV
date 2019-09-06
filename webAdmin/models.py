from django.db import models
from django.utils.text import slugify


class Goods(models.Model):

    def upload_path_handler(self, filename):
        return ("post_" + slugify(self.nameGoods) + "/images/" + filename)

    path = "path/"

    nameGoods           = models.CharField(max_length = 50)

    descriptionGoods    = models.TextField(max_length = 500)

    typeGoods           = models.CharField(max_length = 20)

    conditionGoods      = models.CharField(max_length = 20)

    priceGoods          = models.IntegerField()

    imagesGoods         = models.ImageField(upload_to = upload_path_handler)

    datePostGoods       = models.DateTimeField(auto_now_add=True)

    rateGoods           = models.IntegerField(blank=True, null=True)

    slugifyGoods        = models.CharField(max_length = 80)

    def save(self):
        self.slugifyGoods = slugify(self.nameGoods)
        super(Goods, self).save()
    
    def __str__(self):
        return "{}. {} | {}".format(self.id, self.nameGoods, self.datePostGoods)