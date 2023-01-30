from common.lib import ky_cctalk
from common.download import ky_download
from plus import tool


def download(movie_list, index=0, seq=True):
    # 添加序号
    if seq:
        movie = movie_list[index]
        movie['title'] = str(index + 1) + '_' + movie['title']
    # 下载视频
    ky_download.download_movie(movie_list, index)


# 根据课程系列号，获取所有的视频信息
def get_by_course_id(series_id):
    movie_list = []
    # 获取课程的所有视频id
    movie_ids = ky_cctalk.get_movie_ids(series_id)
    # 获取所有视频id下的标题和链接
    for movie_id in movie_ids:
        ky_cctalk.get_title_href(movie_id, movie_list)
    tool.print_container_elements(movie_list)
    return movie_list


# 根据单个视频id，获取单个视频信息
def get_by_movie_id(movie_id):
    movie_list = []
    ky_cctalk.get_title_href(movie_id, movie_list)
    tool.print_container_elements(movie_list)
    return movie_list
