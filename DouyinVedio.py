import re
import urllib
import requests
import json
def Get_Header():
    return{
        "Host": "www.douyin.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Connection": "keep-alive",
        "Cookie": "douyin.com; __ac_referer=https://www.douyin.com/; ttwid=1%7Cch2_aXmBHt5ch_Ou-Bpyz4sNxj6KH6Klq49QEuc_XYE%7C1696044926%7C674e12352f10eb2d39780dbb03e6eb8e89946c1c3dadf286748e255e73c2542c; __live_version__=%221.1.1.4374%22; webcast_local_quality=null; live_can_add_dy_2_desktop=%220%22; msToken=LGs5LKjqGP9Ur_jaZ1jz1okFplYoJX5oP4bEhk1Jy4ujo_0rxkAZA7lohTrKCo5fUYF7mHHvvFj0UEyP4OovCheTUs1B5OW3tTl-bI9s4gkGoBJvOv1pUih_OWFYsT4=; webcast_leading_last_show_time=1696044935651; webcast_leading_total_show_times=1; IsDouyinActive=false; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; passport_csrf_token=eb087fb5d33787434af032fbc1c8d290; passport_csrf_token_default=eb087fb5d33787434af032fbc1c8d290; odin_tt=e11184919b3d57963573ccf93f06f63ea326d0fd0e3981dbf35ec79051a1806b; n_mh=AAhZtlDj_xcTjMpudb8dngMeQGYAPcNWw7xHRdOEkFs; sso_uid_tt=56fa2023b3b4a5fbe7e84c198f214cf9; sso_uid_tt_ss=56fa2023b3b4a5fbe7e84c198f214cf9; toutiao_sso_user=d4d71cf1d91d5a23c40761da4c959665; toutiao_sso_user_ss=d4d71cf1d91d5a23c40761da4c959665; sid_ucp_sso_v1=1.0.0-KDlkMmJiZmJmODZmNDhlNGMxNWJmYjM2MzBhNWZkNjkxNTE1ZWY2ODcKCRCJsN-oBhjvMRoCbHEiIGQ0ZDcxY2YxZDkxZDVhMjNjNDA3NjFkYTRjOTU5NjY1; ssid_ucp_sso_v1=1.0.0-KDlkMmJiZmJmODZmNDhlNGMxNWJmYjM2MzBhNWZkNjkxNTE1ZWY2ODcKCRCJsN-oBhjvMRoCbHEiIGQ0ZDcxY2YxZDkxZDVhMjNjNDA3NjFkYTRjOTU5NjY1; passport_auth_status=844b100135e0343f327e08fc9e2f2e6d%2C; passport_auth_status_ss=844b100135e0343f327e08fc9e2f2e6d%2C; sid_guard=95559f3a22f2211a0f8d234162b2d47b%7C1696061449%7C21600%7CSat%2C+30-Sep-2023+14%3A10%3A49+GMT; uid_tt=df7113f4b93f32dafa9762ba33f92d55; uid_tt_ss=df7113f4b93f32dafa9762ba33f92d55; sid_tt=95559f3a22f2211a0f8d234162b2d47b; sessionid=95559f3a22f2211a0f8d234162b2d47b; sessionid_ss=95559f3a22f2211a0f8d234162b2d47b; sid_ucp_v1=1.0.0-KDUwODQ5YzgxNGRjYjUwNzRlYTI3OGJmZTcwYzczNGZlYmQ1MmZlYTgKCBCJsN-oBhgNGgJsZiIgOTU1NTlmM2EyMmYyMjExYTBmOGQyMzQxNjJiMmQ0N2I; ssid_ucp_v1=1.0.0-KDUwODQ5YzgxNGRjYjUwNzRlYTI3OGJmZTcwYzczNGZlYmQ1MmZlYTgKCBCJsN-oBhgNGgJsZiIgOTU1NTlmM2EyMmYyMjExYTBmOGQyMzQxNjJiMmQ0N2I; publish_badge_show_info=%220%2C0%2C0%2C1696044977052%22; _bd_ticket_crypt_doamin=3; _bd_ticket_crypt_cookie=1ad2d21c1813780b7eb4ecf318761ecd; __security_server_data_status=1; download_guide=%223%2F20230930%2F0%22; douyin.com; device_web_cpu_core=16; device_web_memory_size=-1; architecture=amd64; home_can_add_dy_2_desktop=%220%22; strategyABtestKey=%221696060178.219%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2048%2C%5C%22screen_height%5C%22%3A1280%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A0%2C%5C%22downlink%5C%22%3A%5C%22%5C%22%2C%5C%22effective_type%5C%22%3A%5C%22%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; s_v_web_id=verify_ln5qft85_OFoNdD8t_EodE_4rA5_8pbo_2g7r3dWy73hN; store-region=cn-sd; store-region-src=uid; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAL6fTt5gIF_cxs5SqFaFdwhW7JZmiI37Jxr_varbVBlc%2F1696089600000%2F0%2F0%2F1696062048541%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1696664978639%2C%22type%22%3A1%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.993%7D; csrf_session_id=f6e3c16b4e1c8c7ec0b9bc3b2168f883; LOGIN_STATUS=0; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAL6fTt5gIF_cxs5SqFaFdwhW7JZmiI37Jxr_varbVBlc%2F1696089600000%2F0%2F0%2F1696062648541%22; my_rd=2; __ac_nonce=06517dcc6009920cadd4a; __ac_signature=_02B4Z6wo00f01m3zKFgAAIDApwvqKmM0Q85twyzAAP56MdaZdCNBXFlW4kL6DWtz.aqhj936-bOCEx3IQ6hc2SJH7laYAkJuKSVdXZUqfe2G2vlKuqQGCoGg8d6EoHP4cUbeicIoafRIqbFRa8; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTUdYbGorR0lTRy80UTRQZ29Jakw1K0ZYZndkL2hYZ04vT0EyUXU0VXBtRkphSUVTY3dRS1NnYUtoYzFxZzd0WWxpTmpaWGFQVzM1cnREY0hEOEpQbVU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=qSoMvBrHIT8SeV6ZlVmfnX0kdyNjlfPkd74VZ8ztG-_MMJhyjvkC0S0h2mzbbSt2JuMYKWeKNxrekRdU_Iev5WCKgy3VF0yxg9Ukh8nbRxRYEVxqAf9bS1FVfdrH6sk=; tt_scid=-pdKsh61kI0mPoj4aZH4a7OSo1qI3EHP-RQBvjnYMDVPmVvR9h..saotGnXjKtpx5b4f"
    }
def Rexp_get_httpURL(str1):
    return(re.search("[a-zA-z]+://[^\s]*",str1).group())
def Get_Vedio_ID(url):
    return(str(requests.get(url=url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}, allow_redirects=False).text).split("share/video/")[1].split('/')[0])
def Get_Vedio_Json(VID):
    result=requests.get("https://www.douyin.com/user/self?modal_id="+VID,headers=Get_Header(),allow_redirects=False)
    return(urllib.parse.unquote(result.text.split('RENDER_DATA\" type=\"application/json\">')[1].split("</script><script type=\"text/javascript\" async=\"\"")[0], encoding='utf-8', errors='replace'))
def Get_Vedio_Info(string):
    ss = json.loads(Get_Vedio_Json(Get_Vedio_ID(Rexp_get_httpURL(string))))
    title=ss['app']['videoDetail']['desc']
    user_id=ss['app']['videoDetail']['authorUserId']
    direct_url ="https:"+ ss['app']['videoDetail']['video']['playAddr'][0]['src']
    bg_music=ss['app']['videoDetail']['music']['playUrl']['uri']
    cover_img="https:" + ss['app']['videoDetail']['video']['originCover']
    like_count=ss['app']['videoDetail']['stats']['diggCount']
    share_count=ss['app']['videoDetail']['stats']['shareCount'] 
    love_count=ss['app']['videoDetail']['stats']['collectCount']   
    comment_count=ss['app']['videoDetail']['stats']['commentCount']  
    return(title,user_id,direct_url,bg_music,cover_img,like_count,share_count,love_count,comment_count)