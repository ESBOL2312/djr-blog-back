from rest_framework import serializers
from blog.models import article , author, category

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class BlogSerializer(DynamicFieldsModelSerializer):
    authorFn = serializers.ReadOnlyField(source = 'author.full_name', read_only=True)
    category_name = serializers.ReadOnlyField(source = 'category.name', read_only = True)
    class Meta:
        model = article
        read_only_fields = ('id', 'authorFn', 'category_name')
        fields = ('id','created','title','text', 'authorFn','author', 'image', 'category_name')

class BlogAuthorSerializer(serializers.ModelSerializer):
   class Meta:
        model = author
        fields = ['id','full_name']

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id','name']