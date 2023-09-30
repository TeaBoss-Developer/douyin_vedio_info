# douyin_vedio_info
Get the information of the Douyin vedio through the Douyin web page

DouyinVedio.py文件里,有以下几个函数.

Get_Header

Rexp_get_httpURL

Get_Vedio_ID

Get_Vedio_Json 

Get_Vedio_Info

用途和用法:

Get_Header
获取Header以及Cookie,Requests要用.
(内部函数,可忽视.)

Rexp_get_httpURL
通过正则表达式来获取HTTPURL,剔除抖音识别码获取分享链接.
(内部函数,但是可复用.)

Get_Vedio_ID
通过分享链接获取视频ID,好进行爬取视频信息.
(内部函数,可复用获取视频ID.)

Get_Vedio_Json
通过Vedio_ID来获取视频信息的Json
(内部函数,可复用.)

Get_Vedio_Info
通过分享字符串来调用内部方法进行解析,上面所有方法都是为了这个方法服务.
返回格式(Python对象):
title,user_id,direct_url,bg_music,cover_img,like_count,share_count,love_count,comment_count
标题,用户ID,无水印直链,背景音乐,封面图,点赞数,分享数,收藏数,评论数
