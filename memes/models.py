# from django.db import models
# # Create your models here.


# class Meme(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # img = models.ImageField(
#     #     _(""), upload_to=None, height_field=None, width_field=None, max_length=None)


# class Comment(models.Model):
#     text = models.CharField(max_length=254)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     meme = models.ForeignKey(Meme, on_delete=models.CASCADE)


# class Like(models.Model):
#     Meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
