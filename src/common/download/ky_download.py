from common.util import ky_requests
import os


def download_movie(movie_list, index=0):
    movie = movie_list[index]
    # 判断url是否存在
    download_url = movie['url']
    if download_url is None or len(download_url) == 0:
        return
    # 创建文件夹(./data/)
    if not os.path.exists('./data/'):
        os.mkdir('./data/')
    # 拼接文件路径
    file_path = './data/' + movie['title']
    # 判断文件是否存在，存在就不下载
    if os.path.exists(file_path):
        print('>--- 该文件已经存在，不进行下载操作 ---<')
        return

    # 一切就绪，开始下载
    response = ky_requests.get(url=download_url)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    # 下载完成提示
    print(movie['title'] + ' 已经下载完成 --------')
