from django.contrib import admin


class SiteAdmin(admin.AdminSite):
    site_header = "PairCodeTests Administration"
    index_title = "PairCodeTests Administration"
    site_title = "Administration"
