from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from . import process_data
from drf_spectacular.utils import extend_schema,OpenApiParameter,OpenApiResponse
from drf_spectacular.types import OpenApiTypes
from datetime import datetime
import pandas as pd

def err_func(index):
    Err_info={
        0:'Please input valid search',
        1:'failed to parse data',
        2:'No data available for search',
    }
    return {'Error details':Err_info[index]}

class AllCrashes(ViewSet):
    @extend_schema(
        tags=['Book lib API'],
        description='Get user details',
        summary='get user details',
        methods=['GET'],
        parameters=[
            OpenApiParameter(name='ID',style='form',type=OpenApiTypes.INT,required=True),
            OpenApiParameter(name='profile',style='form',required=True,type=OpenApiTypes.STR)

        ],
        responses={
            (200,'*/*'): OpenApiResponse(200,description='ok'),
            (404,'*/*'):OpenApiResponse(description='Not found'),
            (500,'*/*'):OpenApiResponse(description='Server Internal Error')
        }
    )
    def get_user_data(self,request):
        _type=request.query_params.get('ID',None)
        profile=request.query_params.get('profile',None)
        print(_type,profile)
        response_dict={}
        raw_data=process_data.get_data_from_df(_type,profile)
        resonse_list=raw_data.to_dict(orient='records')
        print(raw_data,resonse_list)
        response_dict['content']=resonse_list
        return Response(response_dict)

    @extend_schema(
        tags=['Book lib API'],
        description='Get book',
        summary='get book',
        methods=['GET'],
        parameters=[
            OpenApiParameter(name='ID',style='form',type=OpenApiTypes.STR,required=True),
            OpenApiParameter(name='booktitle',style='form',required=True,type=OpenApiTypes.STR)

        ],
        responses={
            (200,'*/*'): OpenApiResponse(200,description='ok'),
            (404,'*/*'):OpenApiResponse(description='Not found'),
            (500,'*/*'):OpenApiResponse(description='Server Internal Error')
        }
    )
    def get_borrow_data(self,request):
        _type=request.query_params.get('ID',None)
        booktitle=request.query_params.get('booktitle',None)
        response_dict={}
        raw_data=process_data.borrow_book(_type,booktitle)
        response_dict['content']=raw_data
        return Response(response_dict)

    @extend_schema(
        tags=['Book lib API'],
        description='Return book',
        summary='Return book',
        methods=['GET'],
        parameters=[
            OpenApiParameter(name='ID', style='form', type=OpenApiTypes.STR, required=True),
            OpenApiParameter(name='booktitle', style='form', required=True, type=OpenApiTypes.STR)

        ],
        responses={
            (200, '*/*'): OpenApiResponse(200, description='ok'),
            (404, '*/*'): OpenApiResponse(description='Not found'),
            (500, '*/*'): OpenApiResponse(description='Server Internal Error')
        }
    )
    def get_return_data(self, request):
        _type = request.query_params.get('ID', None)
        booktitle = request.query_params.get('booktitle', None)
        response_dict = {}
        raw_data = process_data.return_book(_type, booktitle)
        response_dict['content'] = raw_data
        return Response(response_dict)

    @extend_schema(
        tags=['Book lib API'],
        description='Renew book',
        summary='Renew book',
        methods=['GET'],
        parameters=[
            OpenApiParameter(name='ID', style='form', type=OpenApiTypes.STR, required=True),
            OpenApiParameter(name='booktitle', style='form', required=True, type=OpenApiTypes.STR)

        ],
        responses={
            (200, '*/*'): OpenApiResponse(200, description='ok'),
            (404, '*/*'): OpenApiResponse(description='Not found'),
            (500, '*/*'): OpenApiResponse(description='Server Internal Error')
        }
    )
    def get_renew_data(self, request):
        _type = request.query_params.get('ID', None)
        booktitle = request.query_params.get('booktitle', None)
        response_dict = {}
        raw_data = process_data.renew_book(_type, booktitle)
        response_dict['content'] = raw_data
        return Response(response_dict)

    @extend_schema(
        tags=['Book lib API'],
        description='Get book history',
        summary='get book history',
        methods=['GET'],
        parameters=[
            OpenApiParameter(name='ID', style='form', type=OpenApiTypes.STR, required=True),
            #OpenApiParameter(name='booktitle', style='form', required=True, type=OpenApiTypes.STR)

        ],
        responses={
            (200, '*/*'): OpenApiResponse(200, description='ok'),
            (404, '*/*'): OpenApiResponse(description='Not found'),
            (500, '*/*'): OpenApiResponse(description='Server Internal Error')
        }
    )
    def get_borrow_history_data(self, request):
        _type = request.query_params.get('ID', None)
        #booktitle = request.query_params.get('booktitle', None)
        response_dict = {}
        raw_data = process_data.check_borrowing_history(_type)
        raw_dict=pd.DataFrame.to_dict(raw_data,orient='records')
        response_dict['content'] = raw_dict
        return Response(response_dict)

    @extend_schema(
        tags=['Book lib API'],
        description='Get library data',
        summary='get library data',
        methods=['GET'],
        parameters=[
            #OpenApiParameter(name='ID', style='form', type=OpenApiTypes.STR, required=True),
            #OpenApiParameter(name='booktitle', style='form', required=True, type=OpenApiTypes.STR)

        ],
        responses={
            (200, '*/*'): OpenApiResponse(200, description='ok'),
            (404, '*/*'): OpenApiResponse(description='Not found'),
            (500, '*/*'): OpenApiResponse(description='Server Internal Error')
        }
    )
    def get_library_data(self, request):
        #_type = request.query_params.get('ID', None)
        #booktitle = request.query_params.get('booktitle', None)
        response_dict = {}
        raw_data = process_data.check_library()
        response_dict['content'] = raw_data
        return Response(response_dict)

    @extend_schema(
        tags=['Book lib API'],
        description='Get book availability',
        summary='get book availability',
        methods=['GET'],
        parameters=[
            #OpenApiParameter(name='ID', style='form', type=OpenApiTypes.STR, required=True),
            OpenApiParameter(name='booktitle', style='form', required=True, type=OpenApiTypes.STR)

        ],
        responses={
            (200, '*/*'): OpenApiResponse(200, description='ok'),
            (404, '*/*'): OpenApiResponse(description='Not found'),
            (500, '*/*'): OpenApiResponse(description='Server Internal Error')
        }
    )
    def get_book_available_data(self, request):
        #_type = request.query_params.get('ID', None)
        booktitle = request.query_params.get('booktitle', None)
        response_dict = {}
        raw_data = process_data.check_book_availability(booktitle)
        response_dict['content'] = raw_data
        return Response(response_dict)