from rest_framework.serializers import ModelSerializer

from moviedata.models import Movie


class MovieDetailSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'title',
            'released_year',
            'rating',
            'movie_id',
            'genres',
        ]
        ordering = ['id', '-rating', 'released_year']