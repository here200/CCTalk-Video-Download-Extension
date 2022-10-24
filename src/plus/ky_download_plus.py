from common.download import ky_download


def download(m_lists, index, seq=True):
    # 添加序号
    if seq:
        movie = m_lists[index]
        movie['title'] = str(index + 1) + '_' + movie['title']
    # 下载视频
    ky_download.download_movie(m_lists, index)
