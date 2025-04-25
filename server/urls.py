from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="index"),
    path("api/sayhi/",views.seyHello , name="hello"),
    path("api/getSiteInfo/",views.getSiteInfo , name="site_info"),
    path("api/getSiteMenu/",views.getSiteMenu , name="site_menu"),
    path("api/getSiteDoc/",views.getSiteDocuments , name="site_images"),
    path("api/getMyInfo/",views.getMyInformation , name="about_me"),
    path("api/getactiveServices/",views.getMyServices , name="about_me"),
    path("api/getactiveClients/",views.getClientslist , name="about_me"),
    path("api/getJobExp/",views.getJobExperience , name="about_me"),
    path("api/getEducationExp/",views.getEducationQuality , name="about_me"),
    path("api/getSkills/",views.getMySkills , name="about_me"),
    path("api/getPortfolios/",views.getMyPortflios , name="about_me"),
    path("api/getPortfoloimgs/",views.getPortfolioImages , name="portfolio"),
    path("api/getPortfoloDetailesById/<int:id>/",views.getPortfolioDetailesById , name="portfolio_detaile"),
    path("api/getcontactinfo/",views.getMyConntactInfo , name="portfolio"),
]