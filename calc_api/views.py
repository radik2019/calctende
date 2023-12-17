from rest_framework.response import Response


from calc_api.calc_serializers import CalcFixedFoldSerializer
from rest_framework.generics import CreateAPIView

from core.managers.calculator_manager import FixedFoldManager


class CalcFixedFoldAPIView(CreateAPIView):
    serializer_class = CalcFixedFoldSerializer

    def perform_create(self, serializer):
        print(serializer.data)

    def post(self, request):
        serializer = CalcFixedFoldSerializer(data=request.data)
        if serializer.is_valid():


            fold_approximated = serializer.data.get("fold_approximated")
            interior_fold = serializer.data.get("interior_fold")
            awning_measure = serializer.data.get("awning_measure")
            cloth_measure = serializer.data.get("cloth_measure")
            df = FixedFoldManager(
                fold_approximated, interior_fold, awning_measure, cloth_measure)
            error_message = df.error_message()
            if error_message:
                return Response({'data': serializer.data, 'error_message': error_message}, status=403)
            lst = df.get_measure_list()
            context = {
                'data': serializer.data,
                'info': {
                    'awning_measure': df.awning_measure,
                    'effective_fold': round(df.effective_fold, 2),  # misura piega
                    'cloth_measure': df.cloth_measure,  # misura stoffa
                    'interior_fold': round(df.interior_fold, 2),  # piega dentro
                    'fold_count': int(df.fold_count),
                    'folding_overlay': round((lst[1]['distance'] - lst[0]['distance']) / 2, 2)
                },
                'result': lst
            }

            return Response(context, status=201)

        return Response(serializer.errors, status=400)