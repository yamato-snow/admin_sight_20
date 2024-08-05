from django.db import models

class Task(models.Model):
    text = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Standard(models.Model):
    comment = models.TextField()
    template = models.CharField(max_length=50)
    zoom = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.template

class Guestalk(models.Model):
    day = models.CharField(max_length=5, verbose_name='開催日（『4/1』の形式で半角入力）')
    vol = models.CharField(max_length=2, verbose_name='開催回（『vol.〇』の〇のみ半角入力）')
    guest = models.CharField(max_length=50, verbose_name='ゲスト名')
    guest_url = models.CharField(max_length=200, verbose_name='ゲストプロフィールURL')
    theme = models.CharField(max_length=50, verbose_name='お題（『〇〇について聞いてみよう』の〇〇のみ入力）')
    comment = models.TextField(verbose_name='ひとことコメント')
    template = models.CharField(max_length=50, verbose_name='自己紹介テンプレ⑤')
    thumbnail = models.CharField(max_length=150, verbose_name='サムネURL')
    spreadsheet = models.CharField(max_length=150, verbose_name='質問スプシURL')
    zoom = models.CharField(max_length=100, verbose_name='zoomリンク')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.guest