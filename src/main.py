from plus import cctalk_plus, download_plus

if __name__ == '__main__':
    # 第一种使用方法
    cctalk_plus.get_by_course_id('1612582780690810')
    # download_plus.download(cctalk_plus.movie_list, 26)

    # 第二种使用方法
    # cctalk_plus.get_by_movie_id('16444799633133')
    # download_plus.download(cctalk_plus.movie_list, 0, seq=False)
