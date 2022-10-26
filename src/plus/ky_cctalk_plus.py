from common.lib import ky_cctalk
from common.util import ky_debugs

# 用来保存获取到的视频标题 和 视频链接
movie_list = []


# 根据课程系列号，获取所有的视频信息
def get_by_course_id(series_id):
    movie_list.clear()
    # 获取课程的所有视频id
    movie_ids = ky_cctalk.get_movie_ids(series_id)
    # 获取所有视频id下的标题和链接
    for movie_id in movie_ids:
        ky_cctalk.get_title_href(movie_id, movie_list)
    ky_debugs.print_container_elements(movie_list)


# 根据单个视频id，获取单个视频信息
def get_by_movie_id(movie_id):
    movie_list.clear()
    ky_cctalk.get_title_href(movie_id, movie_list)
    ky_debugs.print_container_elements(movie_list)
