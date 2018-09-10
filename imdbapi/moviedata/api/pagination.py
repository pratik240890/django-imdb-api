from rest_framework.pagination import (
        LimitOffsetPagination,
        PageNumberPagination,
    )


class MoviesLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class MoviesPageNumberPagination(PageNumberPagination):
    page_size = 25
