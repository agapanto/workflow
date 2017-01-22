from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_cellphone = models.CharField(max_length=15)
    contact_email = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Action(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class History(models.Model):
#     actions = Action.
#     # name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.id

class AbstractWorkflow(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Workflow(AbstractWorkflow):

    def __str__(self):
        return self.name

class Task(AbstractWorkflow):
    workflow = models.ForeignKey(Workflow, related_name="workflow_task")
    # nombre del shopper y número de teléfono del shopper
    target_contact_info = models.ForeignKey(ContactInfo, blank=True, null=True)
    # el feedback a entregar
    info = models.TextField()
    # estado actual
    status = models.ForeignKey(Status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

def taskHistoryHandler(sender, instance, created, *args, **kwargs):
    print("taskHistoryHandler")

post_save.connect(taskHistoryHandler, sender=Task)
