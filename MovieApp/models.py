from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)               # 제목
    genres = models.CharField(max_length=50)               # 장르
    overview = models.TextField()                          # 개요
    adult = models.BooleanField(default=False)             # 성인 요소
    production = models.CharField(max_length=60)  # 제작사
    runtime = models.IntegerField(default=0)             # 상영시간
    release = models.DateField(max_length=20)            # 출시일
    budget = models.IntegerField(default=0)             # 예산
    voteAver = models.FloatField(default=0)           # 투표 평균
    voteCount = models.IntegerField(default=0)          # 투표 개수
    status = models.CharField(max_length=20)     # 상영상태
    video = models.URLField()                # 영화 예고편 영상 링크
    poster = models.URLField()               # 영화 포스터 링크
    backdrop = models.URLField()              # 배경 사진 링크
    cast = models.TextField()                 # 배우들
    director = models.CharField(max_length=30)  # 감독

    def __str__(self):
        return self.title


class User(models.Model) :
    nickname = models.CharField(max_length=50, primary_key=True, default=False)
    password = models.CharField(max_length=100, default=False)
    pushedGood = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)

    def str(self):
        return self.nickname


class Opinion(models.Model) :
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # 무비 테이블과 연동
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 테이블 연동
    name = models.CharField(max_length=50, primary_key=True)   # 유저 네임
    content = models.TextField()    # 댓글 내용
    push = models.IntegerField(default=0)    # 추천수
    create_date = models.DateTimeField(auto_now_add=True)   # 댓글 날짜

    def str(self):
        return self.content