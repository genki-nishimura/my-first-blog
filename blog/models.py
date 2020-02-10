from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    #Postは今回のモデルの名前、大文字で始める。models.ModelはポストがDjango Modelだという意味で、Djangoがこれはデータベースに保存するべきものだと分かるようにしている。
    #↓はプロパティの定義。
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #models.ForeignKey 他のモデルへのリンク
    title = models.CharField(max_length=200)
    #models.CharField 文字数が制限されたテキストを定義するフィールド
    text = models.TextField()
    #models.TextField 制限無しの長いテキスト用。ブログポストのコンテンツとしてとして最適。
    created_date = models.DateTimeField(default=timezone.now)
    #models.DateTimeField 日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)
#Pythonにモデルのメソッドだと伝える為に、classキーワードに続く行ではメソッドをインデントする。
    def publish(self):       #ブログを公開するメソッド
        self.published_date = timezone.now()
        self.save

    def __str__(self):       #ポストのタイトルのテキスト(string)が返ってくる。
        return self.title