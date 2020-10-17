from django.db import models
from django.utils.text import slugify

# Create your models here.

class Anbar(models.Model):
    name_kala = models.CharField(max_length=50)
    tedad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Car(models.Model):
    """Model definition for Car."""

    Name = models.CharField(max_length=30)
    Famil = models.CharField(max_length=50)
    mobile=models.CharField(max_length=13)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True, allow_unicode=True)
    Type_Car = models.CharField(max_length=50)
    Number_Car = models.CharField(max_length=50)
    Plak_Car = models.CharField(max_length=50)
    Model_Car = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Car."""

        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        """Unicode representation of Car."""
        return self.Name + ' ' + self.Famil + '' + self.Type_Car

    def save(self, *args, **kwargs):
        value = self.Name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class FirstBazdid(models.Model):
    SALEM = 'SA'
    MAYOB = 'MA'
    DARAD = 'DA'
    NADARAD = 'NA'
    TYPE_CHOICES = [
        (SALEM, 'سالم'),
        (MAYOB, 'معیوب'),
        (DARAD, 'دارد'),
        (NADARAD, 'ندارد'),
    ]
    car = models.OneToOneField(Car,primary_key=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    shisheh = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    chragh_jelo = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    chragh_aghab = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    chragh_rahnama = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    arm = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    lastik = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    camarband = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    tormoz = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    tormoz_dasti = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    bogh = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    barf = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    ayneh_rast = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    ayneh_chap = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    bogh_aghab = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    sensor = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    khamoshkon = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    box_komak = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    parcham = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    chragh_gardon = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)
    zanjir = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=SALEM)

class MonthBazdid(models.Model):
    SALEM = 'SA'
    MAYOB = 'MA'
    DARAD = 'DA'
    NADARAD = 'NA'
    TAVIZ='TA'
    TYPE_CHOICES = [
        (SALEM, 'سالم'),
        (MAYOB, 'معیوب'),
        (DARAD, 'دارد'),
        (NADARAD, 'ندارد'),
        (TAVIZ,'تعویض شد')
    ]
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    chragh_jolo_rahnama = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    chragh_khatar = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    shisheh = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    barf = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    shisheh_shoo = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    bogh = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    sandali = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    charkh = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    lastik = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    tormoz = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    tormoz_dasti = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    bedeneh_darb = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    nezafat = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    motor_girbox = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    parcham = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    chragh_gardon = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    sensor = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)
    roghan = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SALEM)


