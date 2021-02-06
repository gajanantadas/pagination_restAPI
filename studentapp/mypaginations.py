#use for per view paginagtion concept
from rest_framework.pagination import PageNumberPagination
class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'q' #for url name q=enter page_number which u want to go
    page_size_query_param = 'record' # enter numeric value for how many record see in page use record=8
    # maximum page setting for pages
    max_page_size = 6
    last_page_strings = 'end' # defualt last is there using this in case of last we put end
