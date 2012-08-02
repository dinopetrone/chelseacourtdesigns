
from django.contrib import admin
from django.db.models.fields.files import ImageField
from www.admin_hared.widgets import AdminImageWidget

class ImageFieldAdmin(admin.ModelAdmin):
	def formfield_for_dbfield(self, db_field, **kwargs):
		if type(db_field) == ImageField:
			request = kwargs.pop("request", None)
			kwargs['widget'] = AdminImageWidget
			return db_field.formfield(**kwargs)
		return super(ImageFieldAdmin,self).formfield_for_dbfield(db_field, **kwargs)