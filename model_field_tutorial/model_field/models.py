from django.db import models

# Create your models here.

class model_fields(models.Model):
    ''' A class for storing the Model field 
    '''

    # **********----- Integer(Number) Field ----------***********#
    integer = models.IntegerField()
    biginteger = models.BigIntegerField()
    # decimal = models.DecimalField(max_digits=None,decimal_places=None)
    positive = models.PositiveIntegerField()
    small = models.SmallIntegerField()
    positivesmall = models.PositiveSmallIntegerField()
    floatfield = models.FloatField()

    # ***********-------Text(Character Related Field) ---------******#

    character = models.CharField(max_length=200)
    text = models.TextField()

    # ********----------Time and Date field --------**********

    time = models.TimeField(auto_now=False)
    date = models.DateField(auto_now=False)
    datetime = models.DateTimeField(auto_now=False)
    duration = models.DurationField()
    # ************----------File and other Related Field ----------**********

    binary = models.BinaryField()
    filefield = models.FileField(max_length=100,upload_to=None)
    # image = models.ImageField(max_length=100,upload_to=None)
    emailfield = models.EmailField(max_length=100)
    url = models.URLField(max_length=200)
    slug = models.SlugField(max_length=200)
    boolean = models.BooleanField()
    nullboolean = models.NullBooleanField()


    def __str__(self):
        return self.character



