import genshinhelper as gh

cookie = 'account_id=195665277; cookie_token=mlrfyTfnQGtApvS8PlC8Cb49ppNR3Vmwb1nSrKdc'
g = gh.Genshin(cookie)
roles = g.roles_info
print(roles)
