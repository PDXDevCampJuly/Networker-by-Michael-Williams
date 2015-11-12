from django.db import models
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User
from group.models import NetworkerGroup


# helper function for uploading files to username path
def upload_to(instance, filename):
    """ upload images helper function for NetworkerUser """
    return 'images/{}/{}'.format(instance.user_extension.username, filename)


class NetworkerUser(models.Model):
    """ Main table for User """
    user_extension = models.OneToOneField(User)
    membership_list = models.ManyToManyField(NetworkerGroup)

    relationship_to_group = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(
        upload_to=upload_to, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    place_of_birth = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # reorders admin user list by id
    class Meta:
        ordering = ['id', ]

    # converts admin default admin text to custom text
    def __str__(self):
        return "[{}] {}-{} {}".format(self.user_extension.id, self.user_extension.username, self.user_extension.first_name, self.user_extension.last_name)


# ------------------------------------------------------------------categories
class PhoneCategory(models.Model):
    """ Helper table for User_Phone """
    phone_category = models.CharField(max_length=255)

    # converts admin default admin text to custom text
    def __str__(self):
        return self.phone_category


class UserPhone(models.Model):
    """ Sub-table for the User: Phone """
    user_id = models.ForeignKey(NetworkerUser)
    phone_category = models.ForeignKey(PhoneCategory)

    country_code = models.PositiveSmallIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    remove = models.BooleanField(default=False)

    # converts admin default admin text to custom text
    def __str__(self):
        return "{}, {} ({})".format(self.user_id, self.phone_number, self.phone_category_id)


class EmailCategory(models.Model):
    """ Helper table for User_Email """
    email_category = models.CharField(max_length=255)

    # converts admin default admin text to custom text
    def __str__(self):
        return self.email_category


class UserEmail(models.Model):
    """ Sub-table for the User: Email """
    user_id = models.ForeignKey(NetworkerUser)
    email_category = models.ForeignKey(EmailCategory)

    email = models.EmailField()
    remove = models.BooleanField(default=False)

    # converts admin default admin text to custom text
    def __str__(self):
        return "{}, {} ({}) ".format(self.user_id, self.email, self.email_category_id)


class AddressCategory(models.Model):
    """ Helper table for User_Address """
    address_category = models.CharField(max_length=255)

    # converts admin default admin text to custom text
    def __str__(self):
        return self.address_category


class UserAddress(models.Model):
    """ Sub-table for the User: Address """
    user_id = models.ForeignKey(NetworkerUser)
    address_category = models.ForeignKey(AddressCategory)

    street_address_1 = models.CharField(max_length=255)
    street_address_2 = models.CharField(max_length=255, blank=True)
    city_town = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude_api = models.FloatField()
    longitude_api = models.FloatField()
    remove = models.BooleanField(default=False)

    # converts admin default admin text to custom text
    def __str__(self):
        return "{}, {}, {}, {} ({})".format(self.user_id, self.street_address_1, self.postal_code, self.country, self.address_category_id)


class SocialMediaCategory(models.Model):
    """ Helper table for User_Social_Media """
    social_media_category = models.CharField(max_length=255)

    # converts admin default admin text to custom text
    def __str__(self):
        return self.social_media_category


class UserSocialMedia(models.Model):
    """ Sub-table for the User: Social Media """
    user_id = models.ForeignKey(NetworkerUser)
    social_media_category = models.ForeignKey(SocialMediaCategory)

    social_media_url = models.URLField()
    remove = models.BooleanField(default=False)

    # converts admin default admin text to custom text
    def __str__(self):
        return "{}, {} ({})".format(self.user_id, self.social_media_url, self.social_media_category_id)


class JobCategory(models.Model):
    """ Helper table for User_Job """
    job_category = models.CharField(max_length=255)

    # converts admin default admin text to custom text
    def __str__(self):
        return self.job_category


class UserJob(models.Model):
    """ Sub-table for the User: Job """
    user_id = models.ForeignKey(NetworkerUser)
    job_category = models.ForeignKey(JobCategory)

    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    state_province = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    is_current = models.BooleanField(default=True)
    year_started = models.DateField(default=timezone.now)
    year_ended = models.DateField(default=timezone.now)
    remove = models.BooleanField(default=False)

    # converts admin default admin text to custom text
    def __str__(self):
        return "{}, {}, current={} [{}]".format(self.user_id, self.company_name, self.is_current, self.job_category_id)


class EducationCategory(models.Model):
    """ Helper table for User_Education """
    education_category = models.CharField(max_length=255)

    # converts admin default admin text to custom text
    def __str__(self):
        return self.education_category


class UserEducation(models.Model):
    """ Sub-table for the User: Education """
    user_id = models.ForeignKey(NetworkerUser)
    education_category = models.ForeignKey(EducationCategory)

    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    school_name = models.CharField(max_length=255, blank=True)
    is_completed = models.BooleanField(default=False)
    year_started = models.DateField(default=timezone.now)
    year_ended = models.DateField(default=timezone.now)
    remove = models.BooleanField(default=False)

    # converts admin default admin text to custom text
    def __str__(self):
        return "{}, {}, passed={} ({})".format(self.user_id, self.school_name, self.is_completed, self.education_category_id)


class SkillCategory(models.Model):
    """ Helper table for User_Skill """
    skill_category = models.CharField(max_length=255)

    # converts admin default admin text to custom text
    def __str__(self):
        return self.skill_category


class UserSkill(models.Model):
    """ Sub-table for the User: Skill """
    user_id = models.ForeignKey(NetworkerUser)
    skill_category = models.ForeignKey(SkillCategory)
    
    description = models.TextField(blank=True)
    remove = models.BooleanField(default=False)

    # converts admin default admin text to custom text
    def __str__(self):
        return "{}, {} ({})".format(self.user_id, self.skill_description, self.skill_category_id)


