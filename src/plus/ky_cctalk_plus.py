from common.lib import ky_cctalk
from common.util import ky_debugs

# 用来保存获取到的视频标题 和 视频链接
movie_list = []


def get_by_course_id(series_id):
    movie_list.clear()
    # 获取课程的所有视频id
    movie_ids = ky_cctalk.get_movie_ids(series_id)
    # 获取所有视频id下的标题和链接
    for movie_id in movie_ids:
        ky_cctalk.get_title_href(movie_id, movie_list)
    ky_debugs.print_container_elements(movie_list)


def get_by_movie_id(movie_id):
    movie_list.clear()
    ky_cctalk.get_title_href(movie_id, movie_list)
    ky_debugs.print_container_elements(movie_list)
