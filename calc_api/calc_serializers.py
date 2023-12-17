from rest_framework import serializers



class CalcFixedFoldSerializer(serializers.Serializer):
    fold_approximated = serializers.FloatField(required=True, help_text='piega aprossimativa')
    interior_fold = serializers.FloatField(required=True, help_text='piega dentro' )
    awning_measure = serializers.FloatField(required=True, help_text='larghezza tenda')
    cloth_measure = serializers.FloatField(required=True, help_text='larghezza stoffa')


