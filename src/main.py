from common import ky_cctalk

# 用来保存获取到的视频标题 和 视频链接
movie_list = []


def print_container_elements(container):
    for el in container:
        print(el)
    print()


def get_by_course_id(series_id):
    # 获取课程的所有视频id
    movie_ids = ky_cctalk.get_movie_ids(series_id)
    movie_list.clear()
    # 获取所有视频id下的标题和链接
    for movie_id in movie_ids:
        ky_cctalk.get_title_href(movie_id, movie_list)
    print_container_elements(movie_list)


def get_by_movie_id(movie_id):
    movie_list.clear()
    ky_cctalk.get_title_href(movie_id, movie_list)
    print_container_elements(movie_list)


def download(m_lists, index, seq=True):
    # 添加序号
    if seq:
        movie = m_lists[index]
        movie['title'] = str(index + 1) + '_' + movie['title']
    # 下载视频
    ky_cctalk.download_movie(m_lists, index)


if __name__ == '__main__':
    # 第一种使用方法
    get_by_course_id('1612582780690810')
    download(movie_list, 0)

    # 第二种使用方法
    # movie_list = get_by_movie_id('16444799633133')
    # download_movie(movie_list, 0)
