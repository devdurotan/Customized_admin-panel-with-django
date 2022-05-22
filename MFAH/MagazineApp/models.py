from django.db import models
from colorfield.fields import ColorField
from django.utils.html import mark_safe



# Create your models here.
class MagazineCategory(models.Model):
    CategoryName = models.CharField(max_length=255)
    CategoryIcon = models.ImageField(upload_to='Images/Category_Icon/',null=True, blank=True)
    CategoryColor = ColorField(default="#FF0000")

    def image_tag(self):
        return mark_safe('<img src="/%s" width="50" height="50" >' % (self.CategoryIcon))

    image_tag.short_description = 'Selected Image'

    def color_tag(self):
        return mark_safe(f'<span style="background-color:%s; border-radius:30px; padding:8px;">{self.CategoryColor}</span>' % (self.CategoryColor))

    color_tag.short_description = 'Color'
    



    def __str__(self):
        return self.CategoryName

class MagazineDetails(models.Model):
    MagazineName = models.CharField(max_length=255)
    CoverImage = models.ImageField(upload_to='Megazine_Cover/')
    MagazineIssueDate = models.DateField(auto_now=False, auto_now_add=False)
    MagazineCategory = models.ForeignKey(MagazineCategory, on_delete=models.CASCADE)
    RentPrice = models.IntegerField()
    BuyPrice = models.IntegerField()
    MagazineDescription = models.TextField(max_length=500)
    Rating = models.IntegerField(default=0)
    IsPromoted = models.BooleanField(default=False)
    Background = ColorField(default='#ff0000')

class MegazinePages(models.Model):
    PageNumber = models.IntegerField()
    Pages = models.FileField(upload_to=f'PageNumber/')
    ChooseMagazine = models.ForeignKey(MagazineDetails,on_delete=models.CASCADE)
