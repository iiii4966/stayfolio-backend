from django.db import models


class Magazines(models.Model):
    title = models.CharField(max_length=100)
    title_image_url = models.URLField(max_length=400)
    title_text_image_url = models.URLField(max_length=400)	
    identifier = models.CharField(max_length=100)	
    description = models.TextField()
    intro = models.CharField(max_length=200)	
    main_image_url = models.URLField(max_length=400)	
    footer_image_url = models.URLField(max_length=400, null=True)		
    link_btn_title = models.CharField(max_length=100, null=True) 
    link_btn_url = models.URLField(max_length=400, null=True)
    logo_url = models.URLField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'magazines'

class Contents(models.Model):
    content_type = models.CharField(max_length=100)
    header = models.CharField(max_length=100,)
    description = models.TextField()
    image_url = models.URLField(max_length=400, null=True)
    magazine = models.ForeignKey(Magazines, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contents'
