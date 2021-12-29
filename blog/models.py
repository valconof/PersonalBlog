from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	post_title = models.CharField('заголовок вопроса', max_length=50)
	post_text = models.TextField('текст вопроса')
	pub_date = models.DateTimeField('дата публикации')
	author_first_name = models.CharField('имя', max_length=50)
	author_last_name = models.CharField('фамилия', max_length=50)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

class Comment(models.Model):
	author_first_name = models.CharField('имя', max_length=50)
	author_last_name = models.CharField('фамилия', max_length=50)
	comment_text = models.CharField('текст комментария', max_length = 200)
	post = models.ForeignKey(Post, on_delete = models.CASCADE)

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'

class AdminInformation(models.Model):
	text_information = models.CharField('текст информации', max_length=50)

	class Meta:
		verbose_name = 'Информация админа'
		verbose_name_plural = 'Информация админа'