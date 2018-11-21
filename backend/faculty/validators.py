def validate_pdf(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions or value.read(4)[1:] != b'PDF':
        raise ValidationError(u'File is not a valid PDF.')
