# Your App secret key
SECRET_KEY = "TXxWqZHAILwElJF2bKR8"

DEFAULT_FEATURE_FLAGS: Dict[str, bool] = {
    # Note that: RowLevelSecurityFilter is only given by default to the Admin role
    # and the Admin Role does have the all_datasources security permission.
    # But, if users create a specific role with access to RowLevelSecurityFilter MVC
    # and a custom datasource access, the table dropdown will not be correctly filtered
    # by that custom datasource access. So we are assuming a default security config,
    # a custom security config could potentially give access to setting filters on
    # tables that users do not have access to.
    "ROW_LEVEL_SECURITY": True,
}

SUPERSET_WEBSERVER_PORT = 8088

FAVICONS = [{"href": "/static/assets/images/favicon.png"}]
APP_ICON = "/static/assets/images/superset-logo-horiz.png"
APP_ICON_WIDTH = 126

# When using LDAP Auth, setup the LDAP server
# AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
# OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://open.login.yahoo.com/' },
#    { 'name': 'Flickr', 'url': 'https://www.flickr.com/<username>' },

# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = "en"
# Your application default translation path
BABEL_DEFAULT_FOLDER = "superset/translations"
# The allowed translation for you app
LANGUAGES = {
    "en": {"flag": "us", "name": "English"},
    "es": {"flag": "es", "name": "Spanish"},
    "it": {"flag": "it", "name": "Italian"},
    "fr": {"flag": "fr", "name": "French"},
    "zh": {"flag": "cn", "name": "Chinese"},
    "ja": {"flag": "jp", "name": "Japanese"},
    "de": {"flag": "de", "name": "German"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "pt_BR": {"flag": "br", "name": "Brazilian Portuguese"},
    "ru": {"flag": "ru", "name": "Russian"},
    "ko": {"flag": "kr", "name": "Korean"},
}
# Turning off i18n by default as translation in most languages are
# incomplete and not well maintained.
LANGUAGES = {}

# Default cache timeout (in seconds), applies to all cache backends unless
# specifically overridden in each cache config.
CACHE_DEFAULT_TIMEOUT = 60 * 60 * 24  # 1 day

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'mysql://root:Password1!@10.10.2.1/superset'

# Requires on MySQL
# CREATE USER 'superset'@'%' IDENTIFIED BY '8opNioe2ax1ndL';
# GRANT ALL PRIVILEGES ON *.* TO 'superset'@'%' WITH GRANT OPTION;