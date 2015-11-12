from django.contrib import admin

from .models import *


# --------------------------------------------------admin inline NetworkerUser
class CategoriesInline_1(admin.StackedInline):
    model = UserAddress
    extra = 0


class CategoriesInline_2(admin.TabularInline):
    model = UserPhone
    extra = 0


class CategoriesInline_3(admin.TabularInline):
    model = UserEmail
    extra = 0


class CategoriesInline_4(admin.StackedInline):
    model = UserJob
    extra = 0


class CategoriesInline_5(admin.StackedInline):
    model = UserEducation
    extra = 0


class CategoriesInline_6(admin.TabularInline):
    model = UserSkill
    extra = 0


class CategoriesInline_7(admin.TabularInline):
    model = UserSocialMedia
    extra = 0


class UsersAdmin(admin.ModelAdmin):
    inlines = [
        CategoriesInline_1,
        CategoriesInline_2,
        CategoriesInline_3,
        CategoriesInline_4,
        CategoriesInline_5,
        CategoriesInline_6,
        CategoriesInline_7,
    ]

# ---------------------------------------------------------------NetworkerUser
admin.site.register(NetworkerUser, UsersAdmin)


# ------------------------------------------------------------------categories
admin.site.register(SkillCategory)
admin.site.register(AddressCategory)
admin.site.register(EmailCategory)
admin.site.register(PhoneCategory)
admin.site.register(SocialMediaCategory)
admin.site.register(JobCategory)
admin.site.register(EducationCategory)


