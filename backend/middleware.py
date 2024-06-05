import cProfile
import pstats
import io
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class ProfilerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if settings.DEBUG:
            self.profiler = cProfile.Profile()
            self.profiler.enable()

    def process_response(self, request, response):
        if settings.DEBUG:
            self.profiler.disable()
            s = io.StringIO()
            ps = pstats.Stats(self.profiler, stream=s).sort_stats('cumulative')
            ps.print_stats()
            print(s.getvalue())
        return response
