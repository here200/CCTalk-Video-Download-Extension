from common.util import ky_requests
import os


# 下载视频，并且不会下载重复视频
def download_movie(movie_list, index):
    movie = movie_list[index]
    movie_path = './data/' + movie['title']
    if os.path.exists(movie_path):
        print('>--- 该视频已经存在，不进行下载操作 ---<')
        return
    movie_href = movie['url']
    if movie_href is None or len(movie_href) == 0:
        return
    response = ky_requests.get(url=movie_href)
    with open(movie_path, 'wb') as f:
        f.write(response.content)
    print(movie['title'] + ' 已经下载完成 --------')
