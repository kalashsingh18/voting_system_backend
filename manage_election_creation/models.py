from django.db import models
from login_apis import models as mdd

    # name = models.CharField(max_length=123, default="None")
    # position = models.CharField(max_length=123, default="None")  # Fixed default value
    # number_of_votes = models.IntegerField(default=0)

    # def __str__(self):
    #     return f"{self.name} - {self.position}"
class create_election(models.Model):
    organizer = models.ForeignKey(mdd.users, on_delete=models.CASCADE)
    title = models.TextField(default="")
    number_of_candidates = models.IntegerField(default=0)
    unique_id=models.CharField(max_length=250)
class candidate(models.Model):
    name = models.CharField(max_length=121, default="None")
    position = models.CharField(max_length=123, default="None")  # Fixed default value
    number_of_votes = models.IntegerField(default=0)

   

    


