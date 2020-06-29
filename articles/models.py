from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    #image = models.ImageField(blank=True)
    image = ProcessedImageField(
                blank=True,
                processors=[#<- 어떤 가공할지
                    Thumbnail(300,300),    
                ],
                format='JPEG', # 이미지 포멧(jpg or png)
                options={ #이미지 포멧 관련 옵션
                    'quality': 90,
                }
    )
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=m)       
    #like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#1:N Relation
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    # Article: Comment = 1 : N
    # (부모) : (자식)

    # on_delete 옵션
    # 1. CASCADE - 부모가 삭제되면, 자식도 삭제됨 <-- 많이씀
    # 2. PROTECT - 자식이 있으면, 부모 삭제 불가
    # 3. SET_NULL - 부모가 삭제되면, 자식의 FK에 null 할당 <-- 큰 기업들이씀
    # 4. SET_DEFAULT - 부모가 삭제되면, 자식의 FK에 default값 할당
    # 5. DO_NOTHING - , 아무것도 하지 않음

    # 1. Create
    # article = Article.objects.get(pk=1)
    # comment = Comment()
    # comment.content = '첫 댓글 확인용'
    # (comment.article_id=1) 이렇게도 가능
    # comment.save()
    #
    # 2. Read
    # 2-1. 부모로부터 자식들 가져오기
    # aritcle=Article.objects.get(pk=1)
    # commtens = article.comment_set.all()

    # 2-2 자식테이블에서 조건으로가져오기
    # article = Article.objects.get(pk=1)
    # comment=Comment.objects.filter(article=article)
    # (  .filter(article_id=1) )
    # article = comment.article
    # article.comment

# Django Fixtures
# 1. dumpdata
# python manage.py dumpdata articles.article --indent=2 > article.json

# 2. loaddata
# python manage.py loaddata article.json

# 3. csv to fixtures
# https://hpy.hk/c2f

