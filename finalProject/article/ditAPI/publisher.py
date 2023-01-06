news=[
    #press,img = get 필요
    {"name":"naver",
    "press":[".media_end_head_top_logo_img","title"],
    "title":".media_end_head_headline",
    "contents":"._article_content",
    "img":["#img1","data-src"],
    "time":[".media_end_head_info_datestamp_time","data-date-time"],
    "reporter":".media_end_head_journalist_name",
    },
    {"name":"daum",
    "press":["#kakaoServiceLogo","data-tiara"],
    "title":".tit_view",
    "contents":".article_view > section >[dmcf-ptype='general']",
    "img":[".thumb_g_article","src"],
    "time":".num_date",
    "reporter":".info_view > span:first-child"
    }
]


