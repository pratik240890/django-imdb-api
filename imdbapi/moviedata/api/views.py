from rest_framework.generics import (
        ListAPIView, 
    )
from moviedata.models import Movie
from .pagination import (
        MoviesPageNumberPagination
    )
from .serializers import (
        MovieDetailSerializer,
    )

import omdb
from django.conf import settings


class MovieListAPIView(ListAPIView):
    """
        API class for providing movie information to
        users with filters.
    """
    serializer_class = MovieDetailSerializer
    pagination_class = MoviesPageNumberPagination
    
    def get_movie_by_name(self, name):
        """
            Method searches movie in local database and 
            if the movie not found in database then it
            searches using omdb python library and adds
            movie infomration within database.
            
            param:
                name : name of movie from query string
        """
        movie_list = Movie.objects.filter(title=name)
        if not movie_list:
            omdb.set_default('apikey', settings.OMDB_API_KEY)
            moviedata = omdb.get(title=name)
            movie_obj = Movie(
                        title=moviedata['title'],
                        released_year=moviedata['year'],
                        rating=moviedata['imdb_rating'],
                        movie_id=moviedata['imdb_id'],
                        genres=moviedata['genre'],
                    )
            movie_obj.save()
            movie_list = Movie.objects.filter(title=name)
        return movie_list
    
    def get_queryset(self, *args, **kwargs):
        """
            Method to get all movie data. If the 
            query string provided by user then it
            filters the result based on that criteria.
        """
        movie_list = Movie.objects.all()

        name = self.request.GET.get("name")
        movie_id = self.request.GET.get("id")
        genres = self.request.GET.get("genres")
        year = self.request.GET.get("year")
        higher = self.request.GET.get("higher")
        lower = self.request.GET.get("lower")
        before = self.request.GET.get("before")
        after = self.request.GET.get("after")

        if name:
            movie_list = self.get_movie_by_name(name)

        if movie_id:
            movie_list = movie_list.filter(movie_id=movie_id)
        if genres:
            movie_list = movie_list.filter(genres__icontains=genres)
        if year:
            movie_list = movie_list.filter(released_year=year)
        if before:
            movie_list = movie_list.filter(released_year__lt=before)
        if after:
            movie_list = movie_list.filter(released_year__gt=after)
        if higher:
            movie_list = movie_list.filter(rating__gte=higher)
        if lower:
            movie_list = movie_list.filter(rating__lte=lower)

        return movie_list
