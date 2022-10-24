from common.util import ky_requests, ky_jsons


# 根据课程id, 获取课程里边所有的视频id
def get_movie_ids(series_id):
    url = 'https://www.cctalk.com/webapi/content/v1.2/series/all_lesson_list'
    params = {
        'seriesId': series_id
    }
    tmp = ky_requests.decode_response(ky_requests.get(url=url, params=params))
    ky_jsons.cache = ky_jsons.json_string2python_object(tmp)
    # 解析数据，获取每个视频的id号
    return ky_jsons.get_data('$..items..contentId')


# 根据单个movie_id，获取里边的标题和链接，将其存放在movie_list里
def get_title_href(movie_id, movie_list):
    url = 'https://www.cctalk.com/webapi/content/v1.1/video/detail'
    params = {
        'videoId': movie_id
    }
    tmp = ky_requests.decode_response(ky_requests.get(url=url, params=params))
    ky_jsons.cache = ky_jsons.json_string2python_object(tmp)
    movie_title = ky_jsons.get_one_data('$..videoName') + '.mp4'
    movie_href = ky_jsons.get_one_data('$..videoUrl')
    # 保存视频信息
    movie_list.append({"index": len(movie_list), "title": movie_title, "url": movie_href})
