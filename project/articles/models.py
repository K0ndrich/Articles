from django.db import models


class Articles(models.Model):
    # auto_now автоматически записываеться значение создания записи в таблице
    create_date = models.DateTimeField(
        auto_now=True,
    )
    name = models.CharField(max_length=200, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")

    # указывает какие данные будут выводиться , когда берем одну запись
    def __str__(self):
        # ""%s: %s-%s," улучшеная копия f-строки
        return "%s: %s-%s" % (self.data, self.name, self.text)

    # class Meta позволяет изменять представлнение данных из нашей таблици
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
