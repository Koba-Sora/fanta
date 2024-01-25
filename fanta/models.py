from django.db import models

serect = (
        ('sekai','世界'),
        ('taiki','佐藤大樹'),
        ('sawanatsu','澤本夏輝'),
        ('reiya','瀬口黎弥'),
        ('horinatsu','堀夏喜'),
        ('keito','木村慧人'),
        ('yuse','八木勇征'),
        ('sota','中島颯太'),
        ('shota','中尾翔太')
        )

class Photo(models.Model):
    member = models.CharField(
        max_length = 20,
        choices = serect
    )
    photo = models.ImageField()

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.photo)

class Review(models.Model):
    photo = models.ForeignKey(Photo,on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text